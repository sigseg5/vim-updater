from webbrowser import open_new_tab


def open_browser(url):
    """
    Function to open browser
    :param url: String url value
    """
    try:
        open_new_tab(url)
    except AttributeError:
        print("AttributeError\nCan't open browser")
        print("Open link to download git for you system\nLink: http://git-scm.com/")
