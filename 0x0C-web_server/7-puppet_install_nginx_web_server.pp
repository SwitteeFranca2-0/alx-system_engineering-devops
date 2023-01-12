#install nginx on a server

exec {
    provider => shell,
    command => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.html; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.istockphoto.com\/photos\/horror permanent;/" /etc/nginx/sites-availabe/default ; sudo service nginx start',
}
