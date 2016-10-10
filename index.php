<?php



// Array
$data = array(
    "gantryAngle"  => 100,
    "collAngle" => 100,
    "couchAngle" => 100,
    "SAD" => 100,
   
);

// Executar Python Script e enviar dados JSON
$result = shell_exec('python coordinates2.py ' . escapeshellarg(json_encode($data)));

// Decodificar o Resultado 
$resultData = json_decode($result, true);

// Plotar na Tela o Resultado
print_r($resultData);
