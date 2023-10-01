from bs4 import BeautifulSoup


def clean_html(raw_html):
    return BeautifulSoup(raw_html, "html.parser").text
