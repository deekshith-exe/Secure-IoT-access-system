from logger import log_event

MAX_ATTEMPTS = 3
PASSWORD = "secure123"

def authenticate():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        user_input = input("Enter password: ")

        if user_input == PASSWORD:
            log_event("User authenticated successfully")
            print("Access Granted ✅")
            return True
        else:
            attempts += 1
            log_event(f"Failed attempt {attempts}")
            print(f"Access Denied ❌ | Attempts left: {MAX_ATTEMPTS - attempts}")

    log_event("System locked due to multiple failed attempts")
    print("System Locked 🔒 Too many failed attempts")
    return False