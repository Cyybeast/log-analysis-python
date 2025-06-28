# analyze_logs.py

# Open the log file
with open("login_logs.txt", "r") as file:
    lines = file.readlines()

# Create a dictionary to store failed login attempts by IP
failed_logins = {}

for line in lines:
    if "login failed" in line:
        ip = line.strip().split("IP")[-1].strip()
        if ip in failed_logins:
            failed_logins[ip] += 1
        else:
            failed_logins[ip] = 1

# Print the results
print("Failed login attempts by IP address:\n")
for ip, count in failed_logins.items():
    print(f"{ip} — {count} time(s)")