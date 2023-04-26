#!/usr/bin/env bash
# Install Nginx web server with puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Start and enable Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80;
      server_name _;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 https://allysynergy.tech /;
      }
    }
  ",
  require => Package['nginx'],
}

# Create symbolic link to enable Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service when configuration changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Apply the puppet manifest
sudo puppet apply 7-puppet_install_nginx_web_server.pp
