<?php
	function tokenize_outers($line) {
        $line_new = trim(str_replace('[', '|', $line));
		$line_new = str_replace(']', '|', $line_new);
		$outers = explode('|', $line_new);
		
		//outside or inside square brackets?
		$inners = array();
		$starter = ($line[0]==='[')? 0 : 1;
		for ($i=$starter; $i<count($outers); $i+=2) {
			$inners[] = $outers[$i];
			unset($outers[$i]);		
		} 
	    $outers = array_values($outers);
	    $inners = array_values($inners);
		return array( "inners" => $inners, "outers" => $outers );
	}

	function isABBA($str) {
		for ($i=0; $i<strlen($str)-3; ++$i) {
			if ( $str[$i] === $str[$i+3] 
				 && $str[$i+1] === $str[$i+2]
				 && $str[$i] !== $str[$i+1] )
				 return true; 
		} 
		return false;	
	}
	
	function isTLS($address) {
		$outers = tokenize_outers($address)["outers"];
		$inners = tokenize_outers($address)["inners"];
		
		foreach ($inners as $str) {
			if (isABBA($str)) 
				return false;
		}
		
		foreach ($outers as $str) {
			if (isABBA($str)) {
				echo "\t !!!!!!".$str." is ABBA: \n";
				return true;
			}
		//	else 
		//		echo $str." is NOT ABBA \n";
			
		}
		return false;

	}
	
	$count = 0;
	$filename = "test_case_7-1.txt";
	$fp = fopen($filename, "r")
	  or die("Can not open ".$filename);	
	
	while (!feof($fp)) {
		
		$line = trim(fgets($fp));
		if (strlen($line) == 0)
			return;
					
		if (isTLS($line)) {	
			echo "$line supports TLS\n";
			++$count;
		    echo "TLS support count: ".$count."\n";
		}
	//	else
	//		echo "$line not supports TLS\n";
	}
	fclose($fp);
?>
