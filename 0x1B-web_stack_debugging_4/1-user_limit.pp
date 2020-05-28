# fix
exec {'holberton_hard':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => "sudo sed -i  's/holberton hard nofile 5/holberton hard nofile  65534/g' /etc/security/limits.conf; /sbin/sysctl -p",
}
exec {'holberton_soft':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => "sudo sed -i  's/holberton soft nofile 4/holberton soft nofile  65534/g' /etc/security/limits.conf; /sbin/sysctl -p",
}