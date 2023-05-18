# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
file_line { 'increase-hard-file-limit-for-holberton-user':
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 50000',
  match   => 'holberton hard nofile',
  ensure  => present,
  before  => Exec['reload-limits-config'],
}

# Increase soft file limit for Holberton user.
file_line { 'increase-soft-file-limit-for-holberton-user':
  path    => '/etc/security/limits.conf',
  line    => 'holberton soft nofile 50000',
  match   => 'holberton soft nofile',
  ensure  => present,
  before  => Exec['reload-limits-config'],
}

# Reload the limits configuration.
exec { 'reload-limits-config':
  command     => 'sudo sysctl --system',
  refreshonly => true,
}
