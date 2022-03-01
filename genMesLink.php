<?php 
    if (isset($_POST['encryptText'])) {
        $messageText = $_POST['encryptText'];
        echo $messageText;

        $servername = "localhost";
        $username = "Colin";
        $password = "colin";
    
        try {
            $conn = new PDO("mysql:host=$servername;dbname=message", $username, $password);
                // set the PDO error mode to exception
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            echo "Connected successfully";

            // prepare sql and bind parameters
            $stmt = $conn->prepare("INSERT INTO messages (message, id)
            VALUES (:message, :id)");
            $stmt->bindParam(':message', $message);
            $stmt->bindParam(':id', $id);

            // insert a row
            $message = $messageText;
            $id = uniqid();
            $stmt->execute();

        } catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }


    }
    else {
        echo "Please enter a message";
    }

?>