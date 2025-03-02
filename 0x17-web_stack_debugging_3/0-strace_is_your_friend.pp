# Ensure the index.php file exists with expected content
file { '/var/www/html/index.php':
  ensure  => file,
  mode    => '0644',
  content => '<html><head><title>ALX</title></head><body><p>Yet another bug by an ALX student</p></body></html>',
}

# Fix permissions and restart Apache if needed
exec { 'fix-permissions':
  command => 'chmod 755 /var/www/html && chmod 644 /var/www/html/index.php',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test ! -r /var/www/html/index.php',
  notify  => Service['apache2'],
}

# Ensure Apache is running
service { 'apache2':
  ensure    => running,
  enable    => true,
  provider  => 'systemd',
  subscribe => File['/var/www/html/index.php'],
}
