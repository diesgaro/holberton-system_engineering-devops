# Modify ssh config file using puppet and stdlib module
include stdlib

file_line { 'Set IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}

file_line { 'Set PasswordAuthentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
