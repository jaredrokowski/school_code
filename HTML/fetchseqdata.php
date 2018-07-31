
<?php
	$searchtxt = $_GET['searchstring'] ;
	
	$link = mysql_connect('localhost', 'jrokowski', 'caterpillar') or die( 'could not connect') ;
	mysql_select_db('tgfbeta') or die('Could not select database');
	
	$sql = "SELECT DISTINCT uniprotid FROM sequence_name WHERE name like '%" . $searchtxt . "%'" ;
	
	$result = mysql_query($sql) or die('Query failed: ' . mysql_error());
	
	$arr = array() ;
	
	while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
		foreach ($line as $col_value) {
						$arr[] = $col_value ;
	  		}
	}
	
	header('Content-type: application/json');
	echo json_encode( $arr );
?>