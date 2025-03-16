# Password-manager-desktop
 Desktop Password Manager  💻🔑


# Password Manager

## Description

This is a simple, yet effective password manager application built using Python and Tkinter. It allows users to:

*   Generate strong, random passwords.
*   Securely store website credentials (username/email and password).
*   Search for stored credentials by website name.
*   Copy generated passwords to the clipboard.

The application stores data in a `data.json` file, ensuring persistence between sessions.

## Technologies Used

*   **Python:** The core programming language.
*   **Tkinter:**  GUI library for creating the user interface.
*   **pyperclip3:**  Used for copying generated passwords to the clipboard.
*   **json:**  Used for storing and retrieving data from the `data.json` file.
*   **random:** Used for generating random passwords.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Install dependencies:**

    ```bash
    pip install pyperclip3
    ```

## Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  **Enter Website:**  Type the website name in the "Website" field.
3.  **Enter Username/Email:**  Enter your username or email address.
4.  **Generate Password (Optional):** Click the "Generate Password" button to create a strong password.
5.  **Add/Save:** Click the "Add" button to save the credentials.  A confirmation message will appear.
6.  **Search:** To retrieve stored credentials, enter the website name in the "Website" field and click the "Search" button.  A message box will display the username/email and password.

## File Structure

*   `main.py`:  The main Python script containing the application logic.
*   `logo.png`: The application logo. (Ensure this file is present in the same directory)
*   `data.json`:  The file where the password data is stored.  This file will be created automatically when you save your first password.

## Security Considerations

*   **Data Storage:** The `data.json` file stores passwords in plain text.  **This is not a secure method for long-term password storage.**  For a production-level password manager, consider using encryption and a more robust database solution.
*   **Clipboard:** Copying passwords to the clipboard can be a security risk. Be mindful of what other applications have access to your clipboard.
*   **This application is intended for educational purposes and should not be used to store sensitive passwords in a production environment.**

## Future Enhancements

*   **Encryption:** Implement encryption to protect the passwords stored in `data.json`.
*   **Master Password:** Add a master password to encrypt the `data.json` file.
*   **GUI Improvements:** Enhance the user interface for a more polished experience.
*   **Password Strength Indicator:**  Add a visual indicator to show the strength of generated passwords.
*   **Database Integration:** Replace `data.json` with a more robust database system (e.g., SQLite, PostgreSQL).
