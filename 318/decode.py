import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    decoded_data = base64.b64decode(data).decode("utf-8")
    reader = csv.reader(decoded_data.splitlines())
    next(reader)  # skip header
    return [row[2] for row in reader]
