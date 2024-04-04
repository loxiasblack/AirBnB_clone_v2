#!/usr/bin/env bash
#setup my web server to deploy web_static

if command -v nginx > /dev/null; then
    echo "Nginx is already installed"
else
    sudo apt-get update
    sudo apt-get install -y nginx
fi

DIRS=(
    "/data/web_static/releases"
    "/data/web_static/shared"
    "/data/web_static/releases/test"
)

for dir in "${DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        sudo mkdir -p "$dir"
    else
        echo "Directory $dir already exists."
    fi
done


HTML_FILE="/data/web_static/releases/test/index.html"
echo "<!DOCTYPE html>
<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    Hello, Nginx!
  </body>
</html>" | sudo tee $HTML_FILE
SYMLINK_TARGET="/data/web_static/releases/test"
SYMLINK="/data/web_static/current"
if [ -L "$SYMLINK" ]; then
    sudo rm "$SYMLINK"
fi
sudo ln -s "$SYMLINK_TARGET" "$SYMLINK"
sudo chown -R ubuntu:ubuntu /data/

NGINX_CONF="/etc/nginx/sites-available/default"
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static { alias /data/web_static/current/; }' $NGINX_CONF

sudo systemctl restart nginx
exit 0

