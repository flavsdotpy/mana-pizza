import boto3
import json
import os

from mana_pizza.commons.log import get_logger


class LocalDB:

    __loaded = False
    __db = None

    def __load_db_from_s3(self):
        get_logger().info("Loading db from s3...")
        s3_client = boto3.client("s3")
        with open(os.getenv("DB_LOCAL_FILE_PATH"), "wb") as f:
            s3_client.download_fileobj(os.getenv("DB_S3_BUCKET"), os.getenv("DB_S3_KEY"), f)

    def load(self):
        if not self.__loaded:
            get_logger().info("Loading local db...")
            if not int(os.getenv("SKIP_S3_DOWNLOAD", "0")):
                self.__load_db_from_s3()
            with open(os.getenv("DB_LOCAL_FILE_PATH")) as db_content:
                self.__db = json.load(db_content)
            self.__loaded = True

    def get_card_by_name(self, card_name: str, supress_error: bool = False):
        try:
            return self.__db["cards"][card_name.upper()]
        except KeyError:
            if supress_error:
                return None
            raise Exception(f"Card {card_name} not found in the internal Database")
        
    def get_last_updated(self):
        return self.__db["last_updated"]


local_db = LocalDB()
