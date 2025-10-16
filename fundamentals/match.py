from enum import Enum


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not foud"
        case 401 | 403:
            return "Not allowed"
        case _:
            return "Other error"


print(http_error(400))
print(http_error(404))
print(http_error(401))
print(http_error(403))
print(http_error(999))


class Color(Enum):
    RED = "red"
    GREEN = "green"


def match_color(color):
    match color:
        case Color.RED:
            return "red"
        case Color.GREEN:
            return "green"


print(match_color(Color("red")))
print(match_color(Color("green")))
