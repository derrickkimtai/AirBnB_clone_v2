#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
if [ ! -x "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

if  [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data

config_content="
server {
    listen 80;
    listen [::]:80;

    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}"
echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo service nginx restart

exit 0
