file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('your_module/nginx.conf.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  restart   => '/usr/sbin/service nginx reload',
  subscribe => File['/etc/nginx/nginx.conf'],
}
