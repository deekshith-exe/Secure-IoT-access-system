# Main System

from auth import authenticate
from logger import log_event

def run_system():
    print("🔐 Secure IoT Access System\n")

    result = authenticate()

    if result:
        log_event("Successful login")
        print("System Access Granted 🚀")
    else:
        log_event("System locked after failed attempts")
        print("System Locked 🔒")

if __name__ == "__main__":
    run_system()