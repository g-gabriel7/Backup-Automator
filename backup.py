import os
import shutil
import logging
import getpass
import socket
from datetime import datetime

def get_client_info():
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    return hostname, ip_local


def setting_log(c_destination):
    log_file = os.path.join(c_destination, "backup_history.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(message)s',
        encoding='utf-8'
    )
    return log_file


def backup_perform(origin, destination):
    if not os.path.exists(origin):
        print(f"Error: The source folder '{origin}' was not found.")
        return

    os.makedirs(destination, exist_ok=True)
    
    log_file = setting_log(destination)
    user = getpass.getuser()
    hostname, ip_local = get_client_info()
    date_time = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    
    print("Starting backup... Please wait.")

    try:
        shutil.copytree(origin, destination, dirs_exist_ok=True)
        
        message = f"[{date_time}] SUCESS | Host: {hostname} ({ip_local}) | USER: {user} | DESTINATION: {destination} | ORIGIN: {origin}"
        logging.info(message)
        print("\nBackup completed successfully!")
        print(f"Log saved in: {log_file}")

    except Exception as e:
        error_message = f"[{date_time}] ERROR | Host: {hostname} ({ip_local}) | USER: {user} | DESTINATION: {destination} | FAILURE: {str(e)}"
        logging.error(error_message)
        print("\nAn error occurred during the backup. Please check the log file.")


if __name__ == "__main__":
    print("-" * 40)
    print("      AUTOMATED BACKUP SCRIPT      ")
    print("-" * 40)
    

    origin_folder = input("Enter the full path to the SOURCE folder:\n> ").strip()
    destination_folder = input("Enter the full path to the DESTINATION folder:\n> ").strip()
    

    print("-" * 40)
    backup_perform(origin_folder, destination_folder)