# Pharos Testnet Username Generator for Primus

This Python script helps you generate multiple batches of realistic X (formerly Twitter) usernames formatted for mass token sending on the **Pharos testnet (Primus)**. It outputs `.xlsx` files containing randomized usernames, pre-filled platform and amount values, and includes a descriptive header as required.

---

## ✨ Features
- Generates **10 Excel files** each with **200 unique usernames**
- Realistic username format, e.g., `@jeph_27`, `@zino88`, `@susan01`
- Follows the exact XLSX format required by the Pharos Primus testnet sender
- Fully customizable and beginner-friendly

---

## 📂 Output Format
Each generated file includes:
- A descriptive message row
- A column header row: `Receivers | Platform | Send Amount`
- 200 rows of formatted data (usernames, platform=X, amount=0.0001)
 ---<img width="786" height="225" alt="Screenshot From 2025-07-29 15-57-02" src="https://github.com/user-attachments/assets/4b0545ca-607a-4d54-adb4-bd6339be856d" />
  

---

## 🛠 Installation & Usage

### 1. Clone or Download
```bash
git clone https://github.com/your-username/pharos-username-generator.git
cd pharos-username-generator
```

### 2. Install Required Libraries
Make sure Python is installed, then run:

```bash
pip install pandas openpyxl numpy
```

Or use the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Run the Script
```bash
python generate_usernames.py
```
This will generate files like:
```
user_batch_1.xlsx
user_batch_2.xlsx
...
user_batch_10.xlsx
```

---

## ⚠️ Linux Users – Python Package Error Fix
If you're seeing this error:

```
error: externally-managed-environment
```
It’s due to new restrictions on global pip installs (PEP 668).

### ✅ Recommended Fix: Use a Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### ✅ Other Options:
- **Use pipx** (for CLI apps):
  ```bash
  sudo apt install pipx
  pipx install pandas openpyxl numpy
  ```
- **Allow pip to override (not recommended):**
  ```bash
  pip install --break-system-packages pandas openpyxl numpy
  ```
- **Or use apt (if available):**
  ```bash
  sudo apt install python3-pandas python3-numpy
  ```

🧠 **Tip:** Stick with virtual environments for safe package management.

---

## 📜 License
MIT License. Feel free to use, modify, and share.

## 🤝 Contributing
Pull requests are welcome! If you spot a bug or have suggestions, open an issue or submit a PR.

## 📣 Connect with the Author
Follow [@0jeph](https://x.com/0jeph) on X for more updates, testnet tools, and alpha.

---

## 🚨 Disclaimer
This script is provided for educational and testing purposes on the **Pharos/Primus testnet**. Do not use it for spamming or malicious automation. The author is not responsible for how you use the tool.

---

Happy testing and farming! 🚀


buy me a coffe 
BTC ```bc1pt2yjdhskgt2x5fkla3nhpp5zlne07wn07apz3gl4xwnjvv27lfgskd2g8v```
ERC20 ```0xcbfd9409e0b67a8a5f2fb2543ae792b08f5f76c0```
