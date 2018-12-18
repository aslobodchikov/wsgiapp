sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo service gunicorn restart
sudo rm /etc/nginx/sites-enabled/default
gunicorn -b 0.0.0.0:8080 hello:app
