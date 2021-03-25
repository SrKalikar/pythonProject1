from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "https://en.wikipedia.org/wiki/Main_Page"
page = urlopen(url)
print(page)

# this will give is getresponse object
html_bytes = page.read()
html1 = html_bytes.decode('utf-8')
#title_index = html.find("<title>")
#start_index = title_index + len("<title>")
#end_index = html.find("</title>")
#title = html[start_index:end_index]

#html = page.read().decode("utf-8")
soup = BeautifulSoup(html1, "html.parser")
t = []
x = soup.get_text()
for i in x:
    if i == "From":
        t = i
    elif i == "Recently featured":
        break




