#!/bin/sh

#header
printf '<?xml version="1.0" encoding="UTF-8" ?>\n<rss version="2.0">\n\n<channel>\n<title>Allanime (Sub) - RSS Feed</title>\n<link>https://github.com/coolnsx/anime-rss</link>\n<description>A simple RSS feed for allanime!</description>\n' > allanime.xml

#content
for i in $(curl -s "https://allanime.site/anime" -A uwu | sed -nE 's|.*href="(/watch/[^"]*)" class.*|\1|p')
do
	grep -q "$i" allanime.xml || printf '\n<item>\n<title>%s</title>\n<link>%s</link>\n<description>A simple RSS feed for allanime!</description>\n</item>\n' "$(printf "%s" "$i" | cut -d'/' -f4- | tr '[:punct:]' ' ' )" "https://allanime.site${i}" >> allanime.xml
done

#footer
printf "\n</channel>\n</rss>" >> allanime.xml
