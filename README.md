# BeyondTrust PasswordSafe - Check In All Requests

This Python script automates the process of checking in **all open BeyondTrust PasswordSafe requests** via the BeyondTrust Public API.

## 🔧 What It Does

- Authenticates to the BeyondTrust API
- Fetches all open privileged access requests
- Sends a check-in request for each one
- Handles API response status and logs the result

---

## 🚀 Demo Mode (No Real API Required)

This version is fully **mocked** using Python’s `unittest.mock`. It simulates API behavior without needing real credentials or BeyondTrust access.

## 📁 File Structure

├── checkin_script.py # Main script (mocked)
├── config_template.py # Example config file
├── .gitignore # Git ignore rules
└── README.md # This file
---

## 📦 Requirements

- Python 3.7+
- `requests` module

Install dependencies:
```bash
pip install requests

## 🧪 How to Run the Script
Just run the script in your terminal:

python checkin_script.py

You’ll see mocked check-in messages logged to the console.

🔒 Secure Configuration
If you ever want to use real credentials:

Create a config.py:

APIKey = "your-real-api-key"
biUsername = "your-username"
BIServer = "your-server.ps.beyondtrustcloud.com"

✅ Contributing

Feel free to fork, improve, or open PRs. This is designed for clean, modular, secure scripting — and great as a starting point for BeyondTrust API work.

📝 License
MIT License — free to use, modify, and share.


---

## ✅ Step 3: Create `config_template.py`

This helps others understand the config structure **without exposing real secrets**.

### 👉 Create `config_template.py`:

```python
# config_template.py

APIKey = "YOUR_API_KEY"
biUsername = "YOUR_USERNAME"
BIServer = "your-server.ps.beyondtrustcloud.com"
