#fix Apache 500 error by fixing typo in wordpress
file { '/var/www/html/wp-settings.php':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => template('module/wp-settings.erb'),
}

exec { 'restart Apache':
  command     => '/usr/sbin/service httpd restart',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
