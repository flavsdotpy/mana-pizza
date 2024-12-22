from mana_pizza.commons.exceptions import WrongColorIdentitiesException

class ManaPizzaValidator:

    @staticmethod
    def validate_color_identity(deck_color_identity: set[str], deck_color_pips: dict[str, float]):
        for pip, count in deck_color_pips.items():
            if count > 0 and pip not in deck_color_identity:
                raise WrongColorIdentitiesException(f"{pip} is not in your commander's colors!")
