# debug Nginx to accept a number of requets at the same time
exec {'reqload':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/15/3000/g' /etc/default/nginx |  sudo service nginx restart",
}