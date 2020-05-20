# debugging and fixing

exec { 'fixing WordPress':
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => 'shell',
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
}