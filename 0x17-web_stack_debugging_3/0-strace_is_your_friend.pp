# Fixes bad `phpp` extensions to `php`
# Requirement
# Your 0-strace_is_your_friend.pp file must contain Puppet code
# You can use whatever Puppet resource type you want for you fix

exec { 'fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}