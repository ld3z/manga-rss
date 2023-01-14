import requests
import json
import re
import os


def get_latest():
    link = 'https://api.comick.app/chapter/?page=1&order=new&accept_mature_content=true'

    response = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}).json()

    return [
        [
            '{}/{}'.format(x['md_comics'], x['slug']),
            x['status'],
            x['chap']
        ] for x in response['data']
    ]


def generate_rss():
    rss = f"""
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>ComicK - RSS Feed</title>
<link>https://github.com/ld3z/manga-rss</link>
<description>A simple RSS feed for ComicK!</description>
"""

    for item in get_latest():
        rss += """
<item>
    <title>{}</title>
    <link>{}</link>
    <description>{} by {}</description>
</item>
""".format(f"{item[2]} - Chapter {item[1]}", "https://comick.app/comic/" + item[0], f"Chapter {item[1]} of {item[2]} by {item[2]} is out!")

    rss += '\n</channel>\n</rss>'
    return rss


try:
    filename = f'./comick/comick-rss.xml'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as f:
        f.write(generate_rss().strip())
except:
    print('Comick failed.')