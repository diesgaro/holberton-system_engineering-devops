# Set ULIMIT to default value
file { 'Set ULIMIT Value':
    ensure  => present,
    path    => '/etc/default/nginx',
    content => 'ULIMIT="-n 4096"',
}
# Restart Nginx
exec { 'Restart Nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
