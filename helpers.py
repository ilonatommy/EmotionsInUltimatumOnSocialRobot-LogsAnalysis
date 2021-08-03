from enums.gameVersionEnum import GameVersionEnum

from datetime import datetime


def timestamp2str(timestamp):
    return timestamp.strftime('%Y-%b-%d_%H:%M:%S')

def str2timestamp(string):
    return datetime.strptime(string, '%Y-%b-%d_%H:%M:%S')

def version2str(game_version_enum):
    if game_version_enum == GameVersionEnum.EMPHATIC:
        return "+"
    if game_version_enum == GameVersionEnum.EGOISTIC:
        return "-"
    return ""

def str2version(string):
    if string == "+":
        return GameVersionEnum.EMPHATIC
    if string == "+":
        return GameVersionEnum.EGOISTIC
    return GameVersionEnum.UNDEFINED
