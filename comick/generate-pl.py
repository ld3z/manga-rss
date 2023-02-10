import requests
import os


def generate_rss_nsfw(data):
    rss = """\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>ComicK - Polish RSS Feed</title>
<link>https://github.com/ld3z/manga-rss</link>
<description>A simple RSS feed for ComicK!</description>
"""

    for i in data:
        c = i["md_comics"]

        rss += """\
<item>
    <title>{}</title>
    <link>{}</link>
    <description>{}</description>
</item>
""".format(
            f"{c['title']} - Chapter {i['chap']}".replace("&","and"),
            f"https://comick.app/comic/{c['slug']}",
            f"Chapter {i['chap']} of {c['title']} is now available on ComicK!".replace("&","and"),
        )

    rss += "\n</channel>\n</rss>"
    return rss


def generate_rss_sfw(data):
    rss = """\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>ComicK - Polish RSS Feed</title>
<link>https://github.com/ld3z/manga-rss</link>
<description>A simple RSS feed for ComicK!</description>
"""

    for i in data:
        c = i["md_comics"]

        rss += """\
<item>
    <title>{}</title>
    <link>{}</link>
    <description>{}</description>
</item>
""".format(
            f"{c['title']} - Chapter {i['chap']}".replace("&","and"),
            f"https://comick.app/comic/{c['slug']}",
            f"Chapter {i['chap']} of {c['title']} is now available on ComicK!".replace("&","and"),
        )

    rss += "\n</channel>\n</rss>"
    return rss


url_nsfw = "https://api.comick.app/chapter/?lang=pl&page=1&order=new&accept_mature_content=true"
url_sfw = "https://api.comick.app/chapter/?lang=pl&page=1&order=new&accept_mature_content=false"

data_nsfw = requests.get(url_nsfw).json()
data_sfw = requests.get(url_sfw).json()

filename_nsfw = f"./comick/comick-rss-pl-nsfw.xml"
filename_sfw = f"./comick/comick-rss-pl-sfw.xml"

os.makedirs(os.path.dirname(filename_nsfw), exist_ok=True)
os.makedirs(os.path.dirname(filename_sfw), exist_ok=True)

with open(filename_nsfw, "w", encoding="utf-8") as f_out:
    print(generate_rss_nsfw(data_nsfw), file=f_out)

with open(filename_sfw, "w", encoding="utf-8") as f_out:
    print(generate_rss_sfw(data_sfw), file=f_out)