from sys import exit as sys_exit

from src.Utilities.os_checker import check_os
from src.Utilities.git_checker import check_git_on_device
from src.Utilities.git_downloader import openBrowser


UPDATER_VER = "0.0.0"
OS_TYPE = check_os()
GIT_STATUS = check_git_on_device()
GIT_DOWNLOAD_PAGE = "http://git-scm.com/"

print("""
    VIM updater {updater_version}
    OS: {os_type}
    Git status: {git_status}
""".format(updater_version=UPDATER_VER,
           os_type=OS_TYPE,
           git_status=GIT_STATUS))

if str(GIT_STATUS).count("git version") != 1:
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)
