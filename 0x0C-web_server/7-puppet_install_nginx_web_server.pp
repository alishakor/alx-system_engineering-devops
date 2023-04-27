#!/usr/bin/env bash
# A Script to Install Nginx web server with puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Execute the Installation instructions
exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation /
         \/redirect_me {\\n\\t\\treturn 301 https:\/\/redirect_me.allysnergy.com\/;\\n\\t}/" /
         /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
