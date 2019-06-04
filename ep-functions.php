<?php
/*
 * Add my new menu to the Admin Control Panel
 */

 
// Hook the 'admin_menu' action hook, run the function named 'mfp_Add_My_Admin_Link()'
add_action( 'admin_menu', 'mfp_Add_My_Admin_Link' );
 
// Add a new top level menu link to the ACP
function mfp_Add_My_Admin_Link()
{
    //die("NOOOOOOO1 stop");
     add_menu_page(
        'My First Page', // Title of the page
        'My First Plugin', // Text to show on the menu link
        'manage_options', // Capability requirement to see the link
        '../wp-content/plugins/ep-inactive-user/includes/ep-first-acp-page.php' // The 'slug' - file to display when clicking the link
    );
}


// this is the function to add the roles "inactive" and "Custom User"
function inactive_add_roles(){
    //die("NOOOOOOO2 stop");
        add_role('inactive_user',
          __( 'inactive' ), 
            array(
                'read'       => true,
                'edit_posts' => true,
                )
          );

          add_role('test_user',
          __( 'Custom User' ), 
            array(
                'read'       => true,
                'edit_posts' => true,
         ));
        }
        

// this should remove the roles when the plugin in removed        
function inactive_remove_roles() {
        if( get_role('inactive_user')){
            remove_role('inactive_user');
        }
        if( get_role('test_user')){
            remove_role('test_user');
        }
        }

        ?>