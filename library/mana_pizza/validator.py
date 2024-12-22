class ManaPizzaValidator:

    @staticmethod
    def validate_color_identity(
        errors: list[str], deck_color_identity: set[str], deck_color_pips: dict[str, float], card_name: str = None
    ):
        for pip, count in deck_color_pips.items():
            if count > 0 and pip not in deck_color_identity:
                errors.append(
                    f"{card_name if card_name else pip} is not in your commander's colors!"
                )
                break
