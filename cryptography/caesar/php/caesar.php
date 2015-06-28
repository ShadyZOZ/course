<html>
<body>

<form action="caesar.php" method="post">
<h2>The Caesar Cipher</h2>
step(default: 3): <input type="number" name="step"><br>
plaintext: <input type="text" name="plaintext"><br>
ciphertext: <input type="text" name="ciphertext"><br>
<input type="checkbox" name="numbers" />
include numbers
<br />
<input type="checkbox" name="punctuations" />
include punctuations
<br />
<input type="submit" name="action" value='encrypt'>
<input type="submit" name="action" value='decrypt'>
</form>

</body>
</html>
<?php
function test_input($data) {
	$data = trim($data);
	$data = stripslashes($data);
	$data = htmlspecialchars($data);
	return $data;
}
$action = $_POST['action'];
$step = $_POST['step'];
$numbers = $_POST['numbers'];
$punctuations = $_POST['punctuations'];
$plaintext = test_input($_POST['plaintext']);
$ciphertext = test_input($_POST['ciphertext']);
if(!empty($action))
{
    if(empty($step))
    {
        $step = 3;
    }
    if($action == 'encrypt')
    {
        if(!empty($plaintext))
        {
            $ciphertext = '';
            $arr = str_split($plaintext);
            foreach($arr as $plainchar)
            {
                if($plainchar>='a' && $plainchar<='z')
                {
                    $ciphertext .= chr(97 + ((ord($plainchar)+$step) - 97)%26);
                }
                if($plainchar>='A' && $plainchar<='Z')
                {
                    $ciphertext .= chr(65 + ((ord($plainchar)+$step) - 65)%26);
                }
				if($numbers)
				{
	                if($plainchar>='0' && $plainchar<='9')
	                {
	                    $ciphertext .= chr(48 + ((ord($plainchar)+$step) - 48)%10);
	                }
				}
				if($punctuations)
				{
					if($plainchar>='!' && $plainchar<='/')
	                {
	                    $ciphertext .= chr(33 + ((ord($plainchar)+$step) - 33)%15);
	                }
	                if($plainchar>=':' && $plainchar<='@')
	                {
	                    $ciphertext .= chr(58 + ((ord($plainchar)+$step) - 58)%7);
	                }
	                if($plainchar>='[' && $plainchar<='`')
	                {
	                    $ciphertext .= chr(91 + ((ord($plainchar)+$step) - 91)%6);
	                }
	                if($plainchar>='{' && $plainchar<='~')
	                {
	                    $ciphertext .= chr(123 + ((ord($plainchar)+$step) - 123)%4);
	                }
				}
            }
            echo "<h4>ciphertext(step: $step):</h4>";
        	echo "<h4>$ciphertext</h4>";
            unset($plainchar);
        }
        else
        {
            echo 'nothing to encrypt';
        }
    }
    elseif($action == 'decrypt')
    {
        if(!empty($ciphertext))
        {
            $plaintext = '';
            $arr = str_split($ciphertext);
            foreach($arr as $cipherchar)
            {
                if($cipherchar>='a' && $cipherchar<='z')
                {
                    $plaintext .= chr(122 - (122 - (ord($cipherchar)-$step))%26);
                }
                if($cipherchar>='A' && $cipherchar<='Z')
                {
                    $plaintext .= chr(90 - (90 - (ord($cipherchar)-$step))%26);
                }
				if($numbers)
				{
	                if($cipherchar>='0' && $cipherchar<='9')
	                {
	                    $plaintext .= chr(57 - (57 - (ord($cipherchar)-$step))%10);
	                }
				}
				if($punctuations)
				{
	                if($cipherchar>='!' && $cipherchar<='/')
	                {
	                    $plaintext .= chr(47 - (47 - (ord($cipherchar)-$step))%15);
	                }
	                if($cipherchar>=':' && $cipherchar<='@')
	                {
	                    $plaintext .= chr(64 - (64 - (ord($cipherchar)-$step))%7);
	                }
	                if($cipherchar>='[' && $cipherchar<='`')
	                {
	                    $plaintext .= chr(96 - (96 - (ord($cipherchar)-$step))%6);
	                }
	                if($cipherchar>='{' && $cipherchar<='~')
	                {
	                    $plaintext .= chr(126 - (126 - (ord($cipherchar)-$step))%4);
	                }
				}
            }
            echo "<h4>plaintext(step: $step):</h4>";
        	echo "<h4>$plaintext</h4>";
            unset($cipherchar);
        }
        else
        {
            echo 'nothing to decrypt';
        }
    }
    else
    {
    	echo 'what have you done';
    }
}
else
{
	echo 'nothing to do, please input';
}
?>
