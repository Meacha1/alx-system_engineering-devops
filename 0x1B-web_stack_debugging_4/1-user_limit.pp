# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sudo sed -i "s/holberton hard .*/holberton hard nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sudo sed -i "s/holberton soft .*/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin',
}
