#This Puppet manifest fixes a typo in the wp-settings.php file of a WordPress installation.

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
