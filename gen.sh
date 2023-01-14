#!/bin/sh

#header
printf '<?xml version="1.0" encoding="UTF-8" ?>\n<rss version="2.0">\n\n<channel>\n<title>9anime - RSS Feed</title>\n<link>https://github.com/ld3z/anime-rss</link>\n<description>A simple RSS feed for 9anime!</description>\n' > anime.xml

#content
for i in $(curl -s "https://9anime.to/updated" -A uwu | sed -nE 's|.*href="(/watch/[^"]*)" class.*|\1|p')
do
	grep -q "$i" anime.xml || printf '\n<item>\n<title>%s</title>\n<link>%s</link>\n<description>A simple RSS feed for 9anime!</description>\n</item>\n' "$(printf "%s" "$i" | cut -d'/' -f4- | tr '[:punct:]' ' ' )" "https://9anime.to${i}" >> anime.xml
done

#footer
printf "\n</channel>\n</rss>" >> anime.xml
