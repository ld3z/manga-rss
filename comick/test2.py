import requests
import json
import os

def get_latest():
    link = "https://api.comick.app/chapter/?page=1&order=new&accept_mature_content=true"
    response = requests.get(
        link,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
        },
    )
    if response.status_code != 200:
        raise Exception(
            f"Error getting data from {link}. Status code: {response.status_code}"
        )
    data = json.loads(response.text)["data"]
    chapters = {}
    for item in data:
        if "md_comics" in item and "title" in item and "chap" in item:
            title = item.get("title")
            slug = item["md_comics"]["slug"]
            chapter = item.get("chap")
            chapters[f"{slug}-{chapter}"] = {"title":title,"slug":slug,"chapter":chapter}
    return chapters


def generate_rss(chapters):
    rss = f"""
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>ComicK - RSS Feed</title>
<link>https://github.com/ld3z/manga-rss</link>
<description>A simple RSS feed for ComicK!</description>
"""

    for key, value in chapters.items():
        rss += """
<item>
    <title>{}</title>
    <link>{}</link>
    <description>{} by {}</description>
</item>
""".format(
            f"{value['title']} - Chapter {value['chapter']}",
            "https://comick.app/comic/{}".format(value['slug']),
            f"Chapter {value['chapter']} of {value['title']} is now available on ComicK!"
        )

    rss += "\n</channel>\n</rss>"
    return rss

try:
    chapters = get_latest()
    rss = generate_rss(chapters)
    filename = f"./comick/comick-rss.xml"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w") as f:
        f.write(rss.strip())
except Exception as e:
    print(f"Comick failed: {e}")
