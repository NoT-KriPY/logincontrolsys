import time
import sqlite3
import hashlib

def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )
    """)
    
    users_to_add = {
        "admin": "supersecret123",
        "itsme": "mypassword456"
    }
    
    for username, password in users_to_add.items():
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
    
    conn.commit()
    conn.close()

def login():
    create_database()
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    stored_hash = None

    while True:
        username = input("\nEnter username: ").strip()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result:
            stored_hash = result[0]
            break
        else:
            print("[-] User not found. Try again.")

    failed_attempts = 0
    max_attempts = 5

    while failed_attempts < max_attempts:
        password = input("Enter password: ").strip()
        input_hash = hashlib.sha256(password.encode()).hexdigest()

        if input_hash == stored_hash:
            print("\n[+] Access Granted. Welcome!")
            conn.close()
            return
        else:
            failed_attempts += 1
            remaining = max_attempts - failed_attempts
            print(f"[-] Access Denied. Incorrect password. ({remaining} attempts left)")
    print(f"\n[!] BRUTEFORCE DETECTED!!! Too many failed attempts.")
    for i in range(5, 0, -1):
        print(f"Account Locking in: {i} seconds... ", end="\r", flush=True)
        time.sleep(1)
    
    print("\nAccount Locked. Exiting program.")
    conn.close()

login()