<?php
	$door_id = "uqwqemis";
	$i = 0;
	$result_password = "--------"; //8 characters
	for ($k=0; strpos($result_password, "-")!== false; ++$k) {
		$hash = $door_id.$i;
		while (substr($hash, 0, 5) !== "00000") {
			$hash = md5($door_id.$i);
			$i++;
			$pos = $hash[5];
		}
		if ($pos >= '0' && $pos <= '7'
			&& $result_password[$pos] === '-') 
		{
			echo $door_id.($i-1).":".$hash."\n";
			$result_password[$pos] = $hash[6];
			echo $result_password."\n";
		}
		else 
			echo $i.":".$hash." is ignored\n";
	}
	echo "The password is: ".$result_password."\n";

?>
