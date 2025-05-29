# 🚀 AutoBrowserLLM

**AutoBrowserLLM** is a lightweight utility that lets you open multiple popular web browsers with a single command. It's designed for simplicity and efficiency—perfect for developers, testers, or anyone who frequently uses multiple browsers.

---

## 📦 What's Included

- **`AutoBrowserLLM.py`**: The Python script that launches the browsers.
- **`open_browsers.bat`**: The batch file to run the Python script.
- **`README.md`**: This documentation file – you’re reading it now!

---

## 🛠️ How to Use

### 1. Clone/Download the Repository

*   **Option A: Clone with Git:**  This is the recommended method for contributing and keeping your project up-to-date.
    ```bash
    git clone https://github.com/anirudhsiddula/AutoBrowserLLM.git
    cd AutoBrowserLLM
    ```

*   **Option B: Download ZIP:**  Download the ZIP archive from the GitHub repository and extract it to a folder on your computer.

### 2. Extract Files

Unzip the downloaded folder to a convenient location.

### 3. Run the Script

Double-click `open_browsers.bat`. This will execute the Python script and open your browsers automatically.

#### Requirements

*   **Python:** Make sure Python is installed. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
    *   ✅ During installation, *check the box to Add Python to PATH*. This is crucial for the script to run correctly.
*   **Windows OS:** This tool is designed specifically for Windows only. It will not work on macOS or Linux without modification.

#### Customization

*   **Change the Browser:** By default, the script uses Microsoft Edge. To use a different browser:
    1.  Locate the path to your browser's executable (e.g., `chrome.exe`, `firefox.exe`).
    2.  Open `AutoBrowserLLM.py`.
    3.  Modify the `edge_path` variable to point to your desired browser.

*   **File Location:** Ensure that both `AutoBrowserLLM.py` and `open_browsers.bat` are in the same folder. If not, update the paths in the batch file accordingly.

#### Troubleshooting

*   ✅ Confirm Python is installed and added to your system PATH.
*   ✅ Ensure both `.py` and `.bat` files are in the same directory.
*   ❌ Still not working? Try running the `.bat` file from a terminal (Command Prompt or PowerShell) to see any error messages. This can provide more detailed information about what's going wrong.

---

**Additional Notes for GitHub:**

*   **Contributing:**  If you’d like to contribute to this project, please fork this repository and submit a pull request with your changes.
*   **Issues:**  Report any bugs or feature requests as issues on the GitHub repository: [https://github.com/anirudhsiddula/AutoBrowserLLM](https://github.com/anirudhsiddula/AutoBrowserLLM)