<?php
/*
Plugin Name: My frist Plugin
Description: this is my first pluging and it will create an admin bar and also add an inactive role
Author: Erik Solveson
*/
 
// Include mfp-functions.php, use require_once to stop the script if mfp-functions.php is not found
require_once plugin_dir_path(__FILE__) . 'includes/ep-functions.php';

register_activation_hook( __FILE__, 'inactive_add_roles' );

register_deactivation_hook( __FILE__, 'inactive_remove_roles' );