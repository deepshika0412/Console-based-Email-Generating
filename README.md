# Console-based-Email-Generating
This is a simple Python console-based application that generates a One-Time Password (OTP) and sends it via email for verification. It uses the smtplib library for sending emails and MIME (Multipurpose Internet Mail Extensions) to format messages.

🔑 Features
Generates a 6-digit OTP using Python’s random module.
Sends OTP securely via SMTP with TLS encryption.
Uses MIME to create structured email messages.
Prompts the user to enter the OTP for verification.
Verifies if the entered OTP matches the generated one.

🛠️ Technologies Used
Python 3
smtplib (for email sending)
email.mime (for email formatting)
random (for OTP generation)

🚀 How It Works
The program generates a random OTP.
It sends the OTP to the entered receiver email ID using Gmail SMTP.
The receiver enters the OTP in the console.
The program verifies the OTP and displays whether verification was successful or failed.
