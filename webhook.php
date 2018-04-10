<?php

//webhook.php は pythonに変数を与えるだけ。右手は添えるだけ。

//コンテンツの取得
$json_string = file_get_contents('php://input');

$Path = 'python ./core/call.py ' + $json_string;

exec($Path);

?>
