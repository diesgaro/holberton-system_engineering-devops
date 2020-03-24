# Kill the process killmenow with puppet
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin']
}
