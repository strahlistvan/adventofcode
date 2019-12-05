<?php
	
	function print_display(array $display) {
		print "\n";
		for ($i=0; $i<count($display); ++$i){
			for ($j=0; $j<count($display[$i]); ++$j) {
				print $display[$i][$j]." ";
			}
		print "\n";
		}
		print "\n";
	}
	
	function rect(array &$display, $rows, $cols) {
		for ($i=0; $i<$rows; ++$i) {
			for ($j=0; $j<$cols; ++$j) {
				$display[$i][$j] = "#";
			}
		}
	}

	function rotate_column(array &$display, $x, $offset) {
		$row_count = count($display);
		for ($k=0; $k<$offset; ++$k) {
			$col_arr = array();
			$col_arr[0] = $display[$row_count-1][$x];
			for ($i=0; $i<$row_count-1; ++$i) {
				$col_arr[$i+1] = $display[$i][$x];
			}
			for ($i=0; $i<$row_count; ++$i) {
				$display[$i][$x] = $col_arr[$i];
			}
		}	
	}
	
	function rotate_row(array &$display, $y, $offset) {
		$col_count = count($display[$y]);
		for ($k=0; $k<$offset; ++$k) {
			$col_arr = array();
			$col_arr[0] = $display[$y][$col_count-1];
			for ($i=0; $i<$col_count-1; ++$i) {
				$col_arr[$i+1] = $display[$y][$i];
			}
			for ($i=0; $i<$col_count; ++$i) {
				$display[$y][$i] = $col_arr[$i];
			}
		}	
	}	
	
	function count_of_lights(array $display) {
		$counter = 0;
		for ($i=0; $i<count($display); ++$i) {
			for ($j=0; $j<count($display[$i]); ++$j) {
				if ($display[$i][$j] == "#")
					++$counter;
			}
		}
		return $counter;
	}
	
	//$inputfile = "test_case_8-1.txt";
	$inputfile = "input.txt";
	$fp = fopen($inputfile, "r")
	or die("Can not open $inputfile\n");
	
	$row_count = 6; $col_count = 50;
	$display = array_fill(0, $row_count, array_fill(0, $col_count, '.') );
//	print_r($display);
	print_display($display);
	
	while (!feof($fp)) {
		
		$line = trim(fgets($fp));
		$arr = explode(" ", $line);
	//	print_r($arr);	
		if ($arr[0] === "rect") {
			preg_match_all("/[0-9]+/", $arr[1], $matches);
			$cols = (int) $matches[0][0];
			$rows = (int) $matches[0][1];
			echo "rect $rows X $cols\n";
			rect($display, $rows, $cols);
		//	print_display($display);
			
		}
		elseif ($arr[0] === "rotate" && $arr[1] === "column") {
			preg_match_all("/[0-9]+/", $arr[2], $matches);
			$x = (int) $matches[0][0];
			$offset = (int) $arr[4];
			echo "rotate_column $x by $offset\n";
			rotate_column($display, $x, $offset);
		//	print_display($display);	
		}
		elseif ($arr[0] === "rotate" && $arr[1] === "row") {
			preg_match_all("/[0-9]+/", $arr[2], $matches);
			$y = (int) $matches[0][0];
			$offset = (int) $arr[4];
			
			echo "rotate_row $y by $offset\n";
			rotate_row($display, $y, $offset);
		//	print_display($display);
		}
		
	}
	echo "Count of lights: ".count_of_lights($display)."\n";
	print_display($display);
	fclose($fp);
?>
