$file_content = 'I love Puppet'

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => inline_template("<%= CGI.escape(@file_content) %>"),
}
