j@ansible:~$ cat /var/www/html/index.php 
<?php
	if(!isset($_GET['node'])){
		exit();
	}
	header('Content-Type: text/plain');
	if($_GET['node'] == 'distrobution:ge-0/0/0.0:ZTP'){
		readfile('example.conf');
	}else{
		echo '
            system {
                /* trying to get: /?node=' . $_GET['node'] . ' */
                host-name config-not-found;
                root-authentication {
                    encrypted-password "$5$61bN944W$32RNzUePYKo66AXKB.JnLOcaTIv/lMG3V4BE28zgOA3"; ## SECRET-DATA
                }
            }
        ';
	}
?>

