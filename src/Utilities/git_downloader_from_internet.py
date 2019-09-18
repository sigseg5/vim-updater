from webbrowser import open_new_tab


def openBrowser(url):
    try:
        open_new_tab(url)
    except AttributeError:
        print("AttributeError\nCan't open browser")
        print("Open link to download git for you system\nLink: http://git-scm.com/")
