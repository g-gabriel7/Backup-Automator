# Backup-Automator
A simple yet extensible Python script to automate local directory backups with logging and system information capture. Designed with cybersecurity best practices in mind – ensuring data integrity and traceability.

🚀 Features 
- Copies entire directory trees (`shutil.copytree`);
- Automatically creates destination folder if it doesn't exist;
- Logs success/failure with timestamp, hostname, IP, user, and error details;
- Simple command-line interface;
- SHA-256 Hashing: To ensure data integrity post-transfer;
- AES-256 Encryption: To protect data at rest in the backup destination;
- JSON Logging: For easier integration with SOC tools like Splunk or ELK.

❔ Why this matters for security
- Backups are critical for **incident response** and **disaster recovery**;
- Detailed logs provide **audit trail** – essential for forensic analysis;
- Extensible to include **encryption**, **integrity checks**, and **cloud storage**.

📜 Requirements
- Python 3.6+
- No external dependencies (uses only standard library)
