import requests
import json
import re
import os

def get_latest():
    link = 'https://api.comick.app/chapter/?page=1&order=new&accept_mature_content=true'
    response = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}).json()
    data = response['data']
    chapters = []
    for item in data:
        title = item.get('md_comics').get('title')
        slug = item.get('md_comics').get('slug')
        chapter = item.get('chap')
        chapters.append([slug, chapter, title])
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

    for item in chapters:
        rss += """
<item>
    <title>{}</title>
    <link>{}</link>
    <description>{} by {}</description>
</item>
""".format(f"{item[2]} - Chapter {item[1]}", "https://comick.app/comic/{}".format(item[0]), f"Chapter {item[1]} of {item[2]} is now available on ComicK!")

    rss += '\n</channel>\n</rss>'
    return rss

try:
    chapters = get_latest()
    print(chapters)
    rss = generate_rss(chapters)
    filename = f'./comick/comick-rss.xml'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as f:
        f.write(rss.strip())
except:
    print('Comick failed.')
