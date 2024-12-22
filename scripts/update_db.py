import logging
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime
from math import inf

import boto3
import requests


TMP_LOCAL_FILE_PATH = os.getenv("TMP_LOCAL_FILE_PATH")
TMP_LOCAL_DOWNLOAD_PATH = os.getenv("TMP_LOCAL_DOWNLOAD_PATH")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")


def config_log() -> logging.Logger:
    formatter = logging.Formatter(
        "[%(levelname)s][%(asctime)s][%(filename)-15s][%(lineno)3d] - %(message)s"
    )
    formatter.converter = time.gmtime

    logger = logging.getLogger(__name__)
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
    channel = logging.StreamHandler(sys.stdout)

    channel.setFormatter(formatter)
    logger.addHandler(channel)
    return logger


def download_file(url):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(TMP_LOCAL_DOWNLOAD_PATH, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)


def get_file_link():
    _DB_TYPE = "default_cards"
    res = requests.get("https://api.scryfall.com/bulk-data")
    res.raise_for_status()
    for d in res.json()["data"]:
        if d["type"] != _DB_TYPE:
            continue
        return d["download_uri"]
    

def upload_file_to_s3():
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
    )
    s3_client.upload_file(TMP_LOCAL_FILE_PATH, S3_BUCKET, S3_KEY)


def backup_old_file():
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
    )
    s3_client.copy_object(
        Bucket=S3_BUCKET, CopySource=f"{S3_BUCKET}/{S3_KEY}", Key=f"{S3_KEY}.old"
    )


def parse_db():
    _INVALID_FLAGS = ["digital"]
    _INVALID_SETS = ["sum"]
    _INVALID_SET_TYPES = [
        "alchemy", "minigame", "memorabilia", "token",
        "vanguard", "treasure_chest"
    ]

    db_full = defaultdict(dict)
    with open(TMP_LOCAL_DOWNLOAD_PATH) as db_content:
        db_json = json.load(db_content)
        for card in db_json:
            if any([card.get(flag) for flag in _INVALID_FLAGS]):
                continue
            if card.get("set") in _INVALID_SETS or len(card.get("set")) > 3:
                continue
            if card.get("set_type") in _INVALID_SET_TYPES:
                continue

            card_name = card.get("flavor_name", card["name"])

            lowest_price = inf
            for cur, value in card.get("prices", dict()).items():
                if cur.startswith("usd") and value and float(value) < lowest_price:
                    lowest_price = float(value)

            db_full[card_name.upper()][f'{card["set"]}#{card["collector_number"]}'] = {
                "price": lowest_price if lowest_price != inf else 1000.0,
                "name": card_name,
                "color_identity": card.get("color_identity"),
                "colors": card.get("colors"),
                "cmc": card.get("cmc"),
                "mana_cost": card.get("mana_cost"),
                "type_line": card.get("type_line"),
            }
    del db_json

    cards = dict()
    for card_name, editions in db_full.items():
        cheapest_edition = None
        cheapest_price = inf
        for edition, card in editions.items():
            if card["price"] <= cheapest_price:
                cheapest_price = card["price"]
                cheapest_edition = edition
        cards[card_name] = db_full[card_name][cheapest_edition]
    del db_full

    db = {
        "last_updated": str(datetime.now().date()),
        "cards": cards
    }
    with open(TMP_LOCAL_FILE_PATH, "w") as db_file:
        json.dump(db, db_file)


def main():
    logger = config_log()

    logger.info("Started processing...")

    logger.info("Looking for latest file at Scryfall...")
    url = get_file_link()

    logger.info("Downloading file from Scryfall...")
    download_file(url)

    logger.info("Parsing file...")
    parse_db()

    logger.info("Backuping old s3 file...")
    backup_old_file()

    logger.info("Uploading new file...")
    upload_file_to_s3()

    logger.info("Finished processing!")

if __name__ == "__main__":
    main()
