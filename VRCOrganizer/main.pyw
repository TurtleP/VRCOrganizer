import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

import pymsgbox


def get_stat_value(stat_info: float) -> str:
    """
    Grab the stat info and format it into a date time string.
    Something that we can properly parse.
    """

    __timestamp = datetime.fromtimestamp(stat_info)

    return __timestamp.strftime("%Y-%m-%d")


def get_date(file_path: Path) -> str | None:
    """
    Get the date on the file. If it isn't named 'VRChat_WIDTHxHEIGHT_YYYY-MM-*, use ctime.
    If c(reation)_time does not match, use m(odified)_time. Otherwise, return None
    """

    __match = None

    __file_stat = file_path.stat()
    __datas = [file_path.name, get_stat_value(__file_stat.st_ctime),
               get_stat_value(__file_stat.st_mtime)]

    for item_searcher in __datas:
        __match = re.search(r"([0-9]{4}-[0-9]{2})", item_searcher)

        if __match is not None:
            return __match.group(0)

    return None


def main(args=None):
    __cwd = Path().cwd()

    if __cwd.name != "VRChat":
        return pymsgbox.alert(f'Please run this in the VRChat photos directory!', 'Error')

    for item in __cwd.glob("*.png"):
        __item_date = get_date(item)

        if __item_date is not None:
            __folder = Path(__item_date)

            if not __folder.exists():
                __folder.mkdir()

            if __item_date in item.name:
                shutil.move(str(item), __folder)


if __name__ == "__main__":
    main(sys.argv)
