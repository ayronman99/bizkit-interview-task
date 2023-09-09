from flask import Blueprint, request, jsonify

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """
    Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: int
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    user_list = []

    get_user_id = query_by_id()
    get_user_name = query_by_name()
    get_user_age = query_by_age()

    user_list.extend(get_user_id)
    user_list.extend(get_user_name)
    # user_list.extend(get_user_age)

    if len(user_list) == 0 or user_list[0] is None:
        user_list = USERS

    return user_list


def query_by_id():
    user_id = request.args.get("id")

    if user_id:
        query_user_id = [next((user for user in USERS if user["id"] == user_id), None)]
        if query_user_id:
            return query_user_id
        else:
            return []



def query_by_name():
    user_name = request.args.get("name")

    if user_name:
        query_user_names = [
            user for user in USERS if user_name.lower() in user.get("name").lower()
        ]
        if query_user_names:
            return query_user_names
    else:
        return []


def query_by_age():
    user_age = request.args.get("age")

    if user_age:
        query_user_age = [
            user
            for user in USERS
            if user["age"] in (int(user_age), int(user_age) - 1, int(user_age) + 1)
        ]
        if query_user_age:
            return query_user_age
        else:
            return []
        

# def query_by_occupation: unimplemented
