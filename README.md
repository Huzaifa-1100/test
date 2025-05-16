# 🛡️ Secure Data Encryption System
# 📚 Overview
The Secure Data Encryption System is a Python-based web application built using Streamlit that allows users to securely store and retrieve encrypted data. This system uses advanced cryptographic techniques to ensure data confidentiality and integrity. Users can store sensitive information with a unique passkey and retrieve it by providing the correct passkey.

Perfect for learning how to build secure web applications with Streamlit and cryptography!

# 🚀 Features

In-Memory Storage : Data is stored securely in memory without external databases.

Encryption & Decryption : Uses the cryptography library for secure encryption and decryption.

Hashed Passkeys : Passkeys are hashed using SHA-256 for added security.

Reauthorization : Redirects to the login page after 3 failed passkey attempts.

Sidebar Navigation : Provides an intuitive sidebar for easy navigation between pages.

Error Handling : Displays clear error messages for invalid inputs and failed attempts.

User Authentication : Simple login system to restrict access to the application.

# 🔧 Code Explanation

Encryption : Uses Fernet from the cryptography library for secure encryption and decryption.

Passkey Hashing : Passkeys are hashed using SHA-256 before storing.

Session State : Manages user authentication and navigation between pages.

Error Handling : Displays error messages for invalid inputs and failed attempts.

# 📋 Requirements

To run this project, you need the following:

Python 3.8+

Required Python libraries:

streamlit

cryptography


Install the required libraries using the following command:

pip install streamlit cryptography

# 🚀 How to Run

Clone the Repository :

Install Dependencies 

Run the App :

Open the App :

After running the command, Streamlit will provide a local URL (e.g., http://localhost:8501).

Open the URL in your browser to use the app.

# 🛠️ Usage Instructions

1. Login

Use the default credentials:

Username: admin

Password: password

2. Store Data

Navigate to the "Store New Data" page from the sidebar.

Enter the text you want to store and a passkey.

Click "Store Data" to encrypt and save the data.

3. Retrieve Data

Navigate to the "Retrieve Data" page from the sidebar.

Select the stored data from the dropdown.

Enter the correct passkey and click "Decrypt Data" to retrieve the original text.

4. Security Features

If you enter an incorrect passkey 3 times, the system will log you out automatically.

All data is encrypted and decrypted securely using the cryptography library.

# 🌟 Future Enhancements

Persistent Storage : Save data to a file or database for persistence.

Multi-User Support : Allow multiple users with separate accounts.

Advanced Encryption : Use more advanced encryption algorithms.

Styling : Add custom CSS for better aesthetics.

Export/Import Data : Allow users to export and import encrypted data files.

# 📜 License

This project is licensed under the MIT License .

# 📧 Contact

For questions, feedback, or collaboration, feel free to reach out:

Email: asadhussainshad@gmail.com

GitHub: https://github.com/Huzaifa-1100

# 🙏 Acknowledgments

Streamlit : For providing an easy-to-use framework for building web apps.

Cryptography Library : For enabling secure encryption and decryption.

SHA-256 Hashing : For ensuring passkey security.





"# secure_data_encryption" 
"# test" 
