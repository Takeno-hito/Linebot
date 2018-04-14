<?php

//webhook.php は pythonに変数を与えるだけ。右手は添えるだけ。

//コンテンツの取得
$json_string = file_get_contents('php://input');

$Path = 'python2.7 /home/kusanagi/WordPress/DocumentRoot/bot/line/dev/linebot/call.py \''.$json_string.'\'';

exec($Path, $stdout, $return);

echo $return.'<br>';

echo $Path."<br>";

echo $stdout.'<br>';

var_dump($stdout);

echo '<br>';


echo count($stdout).'<br>';

foreach($stdout as $str){
	echo $stdout[$str];
}

?>
