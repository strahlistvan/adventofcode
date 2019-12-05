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
			else
				$counts[$index] = 1;
		}
		$max_v = max($counts);
		$max_i = array_keys($counts, $max_v)[0];
		echo $max_i;
	}
	echo "\n";
	fclose($fp);
?>
