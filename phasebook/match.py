import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (set_matcher(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "searchTime": end - start}, 200


def set_matcher(fave_numbers_1, fave_numbers_2):
    num_set_1 = set(fave_numbers_1)
    num_set_2 = set(fave_numbers_2)

    return all(number in num_set_1 for number in num_set_2)