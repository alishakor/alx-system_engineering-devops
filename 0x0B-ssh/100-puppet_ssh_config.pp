#!/usr/bin/env bash
# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set
# up your client SSH configuration file so that you can connect to a server without typing a password.

# Requirements:

#Your SSH client configuration must be configured to use the
#private key ~/.ssh/school
#Your SSH client configuration must be configured to refuse
#to authenticate using a password

file { 'config':
  ensure  => present,
  owner   => 'root',
  path    => '/etc/ssh/ssh_config',
  content => 'Host 100.25.163.126\n User ubuntu\n IdentityFile ~/.ssh/school\n PasswordAuthentication no'
}
