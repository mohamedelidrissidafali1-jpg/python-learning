# Simple logging system
from datetime import datetime
import os

LOG_FILE = "app.log"

def log_message(level, message):
    """Log a message with timestamp and level"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        with open(LOG_FILE, "a") as file:
            file.write(log_entry)
        
        print(f"✓ Logged: {log_entry.strip()}")
    except Exception as e:
        print(f"Error logging: {e}")

def log_info(message):
    """Log info message"""
    log_message("INFO", message)

def log_warning(message):
    """Log warning message"""
    log_message("WARNING", message)

def log_error(message):
    """Log error message"""
    log_message("ERROR", message)

def view_logs():
    """Display all logs"""
    if not os.path.exists(LOG_FILE):
        print("No logs yet!")

        return
    
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()
            print("\n--- Logs ---")
            for log in logs:
                print(log.strip())
    except Exception as e:
        print(f"Error reading logs: {e}")

def view_errors_only():
    """Display only error logs"""
    if not os.path.exists(LOG_FILE):
        print("No logs yet!")
        return
    
    try:
        with open(LOG_FILE, "r") as file:
            print("\n--- Error Logs ---")
            for log in file:
                if "[ERROR]" in log:
                    print(log.strip())
    except Exception as e:
        print(f"Error reading logs: {e}")

def clear_logs():
    """Clear all logs"""
    try:
        with open(LOG_FILE, "w") as file:
            pass
        print("✓ Logs cleared!")
    except Exception as e:
        print(f"Error clearing logs: {e}")

def view_today_logs():
    """Display logs from today only"""
    if not os.path.exists(LOG_FILE):
        print("No logs yet!")
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(LOG_FILE, "r") as file:
            print(f"\n--- Logs for {today} ---")
            for log in file:
                if today in log:
                    print(log.strip())
    except Exception as e:
        print(f"Error reading logs: {e}")

def count_logs():
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(LOG_FILE, "r") as file:
        for line in file:
            for level in counts:
                if level in line: 
                    counts[level] += 1

    print(counts)

def export_errors():

    with open(LOG_FILE, "r") as file, open("errors.log", "w") as out:

        for line in file: 
            if "ERROR" in line: 
                out.write(line)

def log_debug(message):
    log_message("DEBUG", message)

def log_critical(message):
    log_message("CRITICAL", message)


# Test the logger
print("=== Simple Logger ===\n")

log_info("Application started")
log_info("User logged in")
log_warning("Disk space low")
log_error("Failed to connect to database")
log_info("Application closed")


print("\nAll logs:")
view_logs()

print("\nErrors only:")
view_errors_only()

print("\nToday's logs:")
view_today_logs()

print("\nLog counts:")
count_logs()

print("\nExporting errors to errors.log...")
export_errors()









