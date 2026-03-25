# 🔐 Secure IoT Access System

A Python-based secure access control system simulating IoT authentication with security features and event logging.

---

## 🚀 Features

* 🔑 Password-based authentication
* 🚫 Limited login attempts (3 max)
* 📜 Logging of all events (success & failure)
* ⏱️ Timestamped logs
* 🔒 System lock after multiple failed attempts

---

## 🛠️ Tech Stack

* Python
* File Handling
* Basic Cybersecurity Concepts

---

## 📂 Project Structure

```
Secure-IoT-access-system/
│
├── auth.py        # Handles authentication  
├── logger.py      # Handles logging system  
├── main.py        # Main system controller  
├── logs/          # Stores log files  
└── README.md  
```

---

## ▶️ How to Run

1. Open terminal

2. Run:

```
python main.py
```

3. Enter password:

```
secure123
```

---

## 📸 Sample Behavior

* Tracks failed login attempts
* Grants access on correct password
* Locks system after multiple failures
* Logs all activity in `logs/log.txt`

---

## 🎯 Future Improvements

* Arduino / ESP32 integration
* Biometric authentication
* Web-based dashboard
* Remote IoT device control

---

## 💡 Author

Built by an Electronics & Communication Engineering student focusing on Embedded Systems + Cybersecurity 🚀
