# configuring a custom HTTP header with Puppet

exec { 'update':
  path    => '/usr/bin:/bin',
  command => 'apt-get update',
}

exec { 'install nginx':
  path    => '/usr/bin:/bin',
  command => 'apt-get install nginx -y',
}

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

file_line { '404':
  path  => '/etc/nginx/sites-enabled/default',
  after => 'server_name _;',
  line  => '        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file_line { 'redirect':
  path  => '/etc/nginx/sites-enabled/default',
  after => 'server_name _;',
  line  => '        error_page 404 /custom_404.html;',
}

file_line { 'header':
  path  => '/etc/nginx/sites-enabled/default',
  after => 'server_name _;',
  line  => '        add_header X-Served-By $hostname always;',
}

exec {'/usr/bin/env service nginx restart':}