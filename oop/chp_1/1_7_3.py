from re import fullmatch

class CardCheck:

    @staticmethod
    def check_card_number(number):
        return fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', number) is not None

    @staticmethod
    def check_name(name):
        return fullmatch(r'[A-Z]+ [A-Z]+', name) is not None