import typing
from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(
    args: typing.Dict[str, typing.Any]
) -> typing.List[typing.Dict[str, typing.Any]]:
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    def filter_search(
        records: typing.List[typing.Dict[str, typing.Any]], key: str, val: str
    ) -> typing.List[typing.Dict[str, typing.Any]]:

        if isinstance(val, int) or isinstance(val, float):
            return list(filter(lambda record: record[key] == val, records))

        if isinstance(val, str):
            return list(filter(lambda record: val in str(record[key]).lower(), records))

    raw_search_result: typing.List[typing.Dict[str, typing.Any]] = []
    final_search_result: typing.List[typing.Dict[str, typing.Any]] = []

    param_id = args.get("id")
    if param_id != None:
        # Search Spec #2
        raw_search_result += filter_search(USERS, "id", str(param_id))

    param_name = args.get("name")
    if param_name != None:
        # Search Spec #3
        raw_search_result += filter_search(USERS, "name", str(param_name).lower())

    param_age = args.get("age")
    if param_age != None:
        # Search Spec #4
        raw_search_result += filter_search(USERS, "age", int(param_age))
        raw_search_result += filter_search(USERS, "age", int(param_age) + 1)
        raw_search_result += filter_search(USERS, "age", int(param_age) - 1)

    param_occupation = args.get("occupation")
    if param_occupation != None:
        # Search Spec #5
        raw_search_result += filter_search(
            USERS, "occupation", str(param_occupation).lower()
        )

    # Search Spec #6
    for each_element in raw_search_result:
        if each_element not in final_search_result:
            final_search_result.append(each_element)

    # Bonus Challenge
    # ...

    if len(final_search_result) > 0:
        return final_search_result
    else:
        return USERS
