import webbrowser


def openBrowser(url):
    try:
        webbrowser.open_new_tab(url)
    except AttributeError:
        print("AttributeError\nCan't open browser")
