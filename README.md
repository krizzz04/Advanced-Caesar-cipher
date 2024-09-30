# Advanced Caesar Cipher Tool

The **Advanced Caesar Cipher Tool** combines the classic Caesar Cipher with AES encryption for enhanced security. This hybrid approach allows you to securely encrypt and decrypt messages through a user-friendly GUI built with Tkinter or via a RESTful API using Flask.

## Features

- **Hybrid Encryption**: Combines Caesar Cipher with AES for dual-layer security.
- **GUI Interface**: A modern Tkinter interface with options to encrypt, decrypt, copy results, and access help.
- **Flask API**: RESTful API for integrating encryption and decryption into other applications.
- **Cross-Platform**: Runs on both Windows and Linux.

## Requirements

- Python 3.7+
- `cryptography` library
- `flask` library
- Tkinter (included with Python on Windows, install separately on Linux)

## Installation

### Windows

1. **Clone the repository**:
    ```bash
    git clone https://github.com/krizz04/Advanced-Caesar-cipher.git
    cd Advanced-Caesar-cipher
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the GUI application**:
    ```bash
    python main.py
    ```

5. **Run the Flask server** (for API use):
    ```bash
    python -c "from advanced_caesar_cipher_tool import run_server; run_server()"
    ```

### Linux

1. **Clone the repository**:
    ```bash
    git clone https://github.com/krizz04/Advanced-Caesar-cipher.git
    cd Advanced-Caesar-cipher
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tkinter (if not already installed)**:
    ```bash
    sudo apt-get install python3-tk
    ```

5. **Run the GUI application**:
    ```bash
    python3 main.py
    ```

## Usage

python main.py

## Contributing

Feel free to contribute by submitting pull requests or reporting issues.


