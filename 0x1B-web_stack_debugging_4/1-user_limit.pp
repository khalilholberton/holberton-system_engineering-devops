# fix
exec { 'holberton_hard':
path     => ['/bin', '/usr/bin', '/usr/sbin'],
command  => "sudo sed -i  's/holberton hard nofile 5/holberton hard nofile  4000/g' /etc/security/limits.conf; /sbin/sysctl -p",
}
exec { 'holberton_soft':
path     => ['/bin', '/usr/bin', '/usr/sbin'],
command  => "sudo sed -i  's/holberton soft nofile 4/holberton soft nofile  4000/g' /etc/security/limits.conf; /sbin/sysctl -p",
}