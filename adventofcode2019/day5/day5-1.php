<?php
	$door_id = "uqwqemis";
	$i = 0;
	$result_password = "";
	for ($k=0; $k<8; ++$k) {
		$hash = $door_id.$i;
		while (substr($hash, 0, 5) !== "00000") {
			$hash = md5($door_id.$i);
			$i++;
		}
		echo $door_id.($i-1).":".$hash."\n";
		$result_password.=$hash[5];
	}
	echo "The password is: ".$result_password."\n";

?>
