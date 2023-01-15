import requests
import os

def generate_rss(data):
    rss = """\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>ComicK - RSS Feed</title>
<link>https://github.com/ld3z/manga-rss</link>
<description>A simple RSS feed for ComicK!</description>
"""

    for i in data:
        c = i['md_comics']

        rss += """\
<item>
    <title>{}</title>
    <link>{}</link>
    <description>{}</description>
</item>
""".format(
            f"{c['title']} - Chapter {i['chap']}",
            f"https://comick.app/comic/{c['slug']}",
            f"Chapter {i['chap']} of {c['title']} is now available on ComicK!",
        )

    rss += "\n</channel>\n</rss>"
    return rss

url = "https://api.comick.app/chapter/?page=1&order=new&accept_mature_content=true"
data = requests.get(url).json()

filename = f"./comick/comick-rss.xml"

with open(filename, 'w', encoding="utf-8") as f_out:
    print(generate_rss(data), file=f_out)