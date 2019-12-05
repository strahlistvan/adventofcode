<?php
	$code = array();
	$fp = fopen("input.txt", "r");
	while (!feof($fp)) {
		$code[] = fgets($fp); 	
	}
	for ($j=0; $j<strlen($code[0]); ++$j) {
		$counts = array();
		for ($i=0; $i<count($code); ++$i) {
			$index = $code[$i][$j];
			if (isset($counts[$index])) {
				$counts[$index]++;		
			}
			else if (ctype_alpha($index)) {
				$counts[$index] = 1;
			}
		}
	//	print_r($counts);
		if (count($counts) > 0) {
			$min_v = min($counts);
			$min_i = array_keys($counts, $min_v)[0];
			echo $min_i;
		}
	}
	echo "\n";
	fclose($fp);
?>
