<?php
session_start();

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate form fields
    $email = $_POST['email'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    if (empty($email) || empty($password) || empty($confirm_password)) {
        // If any field is empty, display an error message
        $error_message = "Veuillez remplir tous les champs.";
    } elseif ($password !== $confirm_password) {
        // If passwords do not match, display an error message
        $error_message = "Les mots de passe ne correspondent pas.";
    } elseif (strlen($password) < 3) {
        // If password length is less than 3, display an error message
        $error_message = "Le mot de passe doit avoir au moins trois caractères.";
    } else {
        // All fields are valid, proceed with further checks

        // Connect to the database
        $conn = new mysqli('localhost', 'root', '', 'utilisateurs');

        // Check for connection errors
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Escape user inputs for security
        $email = $conn->real_escape_string($email);

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $error_message = "Adresse email invalide.";
        } else {
            // Check if email already exists in the database
            $sql = "SELECT * FROM Utilisateurs WHERE email='$email'";
            $result = $conn->query($sql);

            if ($result->num_rows > 0) {
                // Email already exists, display an error message
                $error_message = "Cet email est déjà enregistré.";
            } else {
                // Email is unique, proceed with user registration

                // Encrypt the password (consider using password_hash() instead)
                $hashed_password = md5($password);

                // Insert new user into the database
                $sql = "INSERT INTO Utilisateurs (email, pass) VALUES ('$email', '$hashed_password')";
                if ($conn->query($sql) === TRUE) {
                    // Registration successful, redirect to login page
                    header("Location: index.php?success=registration");
                    exit();
                } else {
                    // Error occurred while inserting user, display an error message
                    $error_message = "Erreur lors de l'inscription: " . $conn->error;
                }
            }
        }

        // Close database connection
        $conn->close();
    }

    // Display error message above the form
    echo "<p style='color: red;'>$error_message</p>";
}
?>
