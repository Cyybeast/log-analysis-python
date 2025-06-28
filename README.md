# Log Analysis Script (Python)

This project is a basic log analysis tool written in Python. It demonstrates how to read, parse, and analyze authentication logs to detect potential security incidents such as failed login attempts or suspicious activity.

## 🔍 What It Does

- Reads a sample `login_logs.txt` file
- Parses each line to extract:
  - Date
  - Time
  - Username
  - Login status (Success/Failure)
- Counts:
  - Total login attempts
  - Total successful and failed logins
  - Failed login attempts per user

## 🧠 Why This Matters

Log analysis is a **core skill** for cybersecurity analysts and SOC (Security Operations Center) professionals. This script shows how raw logs can be turned into meaningful insights — like identifying a brute-force attack or unauthorized login attempts.

## 🧪 Sample Output

Total login attempts: 10
Sucessful logins:6
Failed logins: 4

Failed login attempts by user: 
. User1: 2
. User2: 1
. admin: 1

## 🧾 Files

| File              | Description                                |
|-------------------|--------------------------------------------|
| `analyze_logs.py` | Python script that performs the analysis   |
| `login_logs.txt`  | Sample log file with simulated login data  |
| `README.md`       | This project documentation                 |

## 🚀 How to Run

1. Clone the repo or download the files  
2. Make sure Python is installed on your machine  
3. In the terminal, run:

```bash
python analyze_logs.py

Make sure login_logs.txt is in the same folder as the script.

📚 Next Steps
	•	Add support for other log formats (e.g. syslog)
	•	Output results to a CSV or JSON file
	•	Flag accounts with too many failed attempts
	•	Integrate into a basic SOC dashboard (future goal)


👨🏽‍💻 Author

Nelson “Cyybeast”
Aspiring Cybersecurity Analyst | Log Ninja in Training 🕶️
GitHub Profile

--------------------------------

📌 License

This project is open-source and free to use for learning and portfolio purposes.


6. **Save the file** (`Ctrl + S`)

✅ You now have a proper README!

---

## ✅ STEP 2: Upload it to GitHub

### Open Command Prompt:

```bash
cd Desktop\log-analysis-project