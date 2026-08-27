FROM caddy:2-alpine

COPY Caddyfile /etc/caddy/Caddyfile
COPY index.html /srv/index.html
COPY 404.html /srv/404.html
COPY robots.txt /srv/robots.txt
COPY sitemap.xml /srv/sitemap.xml
COPY diensten-online.html /srv/diensten-online.html
COPY diensten-teams.html /srv/diensten-teams.html
COPY diensten-testing.html /srv/diensten-testing.html
COPY privacy.html /srv/privacy.html
COPY resultaten.html /srv/resultaten.html
COPY nl/ /srv/nl/
COPY en/ /srv/en/
COPY de/ /srv/de/
COPY assets/ /srv/assets/

EXPOSE 8080

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
