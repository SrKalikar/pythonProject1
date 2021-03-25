from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"
page = urlopen(url)
# print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
# print(title_index)

start_index = title_index + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
print(title)


def wiki():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text())


wiki()


# by the above code we get whole text from page.
