import re


def check_date(date):
    """
        Regex to check if a date is on the good format
    """
    date_find = re.findall(r"\d{2}/\d{2}/\d{2,4}", date)

    if date_find:
        return True
    else:
        return False
