file { '/path/to/file':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => template('module/file.erb'),
}
