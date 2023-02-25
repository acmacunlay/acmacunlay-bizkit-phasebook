import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2) -> bool:
    """
    The function should return `True` when all numbers in `fave_numbers_2`
    can be found in `fave_numbers_1`. Otherwise, it should return False.
    """

    set_fave_numbers_1: set = set(fave_numbers_1)
    set_fave_numbers_2: set = set(fave_numbers_2)
    return set_fave_numbers_2.issubset(set_fave_numbers_1)

    # NOTE: Old code below. Commented out for comparison.

    # for number in fave_numbers_2:
    #     if number not in fave_numbers_1:
    #         return False

    # return True
