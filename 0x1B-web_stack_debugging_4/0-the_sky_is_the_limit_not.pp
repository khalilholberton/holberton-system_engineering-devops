# debug Nginx to accept a number of request at the same time
exec {'req':
path    => ['/usr/bin', '/bin'],
command => "sudo sed -i 's/15/3000/g'  /etc/default/nginx;  sudo service nginx restart",
}