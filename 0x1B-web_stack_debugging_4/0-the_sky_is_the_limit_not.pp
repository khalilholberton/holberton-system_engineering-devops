# debug Nginx to accept a number of  requests simultaneously

exec {'reqload':
path     => ['/bin', '/usr/bin', '/usr/sbin'],
command  => "sudo sed -i 's/15/3000/g'  /etc/default/nginx;  sudo service nginx restart",
}