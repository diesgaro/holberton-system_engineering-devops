# Install puppet-linter version 2.1.1 with puppet
package { 'puppet-lint':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}
