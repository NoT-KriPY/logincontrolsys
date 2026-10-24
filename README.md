<div align="center">

# 🔐 Login Control System

### A Python-Based Authentication System

A command-line login system using SQLite, password-hash verification, and basic failed-login attempt handling.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![Security](https://img.shields.io/badge/Focus-Authentication-6C5CE7)
![Project](https://img.shields.io/badge/Type-Cybersecurity%20Project-16A085)

*Authenticate users. Store credentials in a database. Explore login security.*

</div>

---

## 📌 Overview

**Login Control System** is a Python-based command-line application that demonstrates a basic user authentication workflow with SQLite database integration.

The program creates a local database, stores usernames and password hashes, and verifies login credentials when a user attempts to sign in.

It also limits password attempts during a login session. After five incorrect password attempts, the application displays a countdown and exits.

This project is designed to help beginners understand authentication logic, database queries, password hashing, and basic defenses against repeated login failures.

> **Security notice:** This project is educational. Its current password-storage method and hard-coded demonstration credentials are not suitable for production authentication systems.

## ✨ Features

| Feature | Description |
|---|---|
| 👤 User Identification | Checks whether the entered username exists in the database. |
| 🗄️ SQLite Database | Stores usernames and password hashes in a local database. |
| 🔑 Password-Hash Verification | Compares a SHA-256 hash of the entered password with the stored hash. |
| 🚦 Attempt Limit | Allows up to five incorrect password attempts during a login session. |
| ⏳ Countdown Mechanism | Displays a five-second countdown after the password attempt limit is reached. |
| 🛡️ Parameterized SQL | Uses a parameterized database query when looking up a username. |
| 🖥️ Command-Line Interface | Provides a straightforward terminal-based login experience. |

## 🧰 Tech Stack

- **Python 3** — application logic
- **SQLite** — local database storage
- **`sqlite3`** — Python's built-in SQLite interface
- **`hashlib`** — SHA-256 hashing
- **`time`** — countdown and delay functionality

No third-party Python packages are required for the current implementation.

## ⚙️ Requirements

Before running the project, ensure you have:

- Python 3 installed
- A terminal or command prompt
- Permission to create and write files in the project directory

SQLite support is included with Python's standard `sqlite3` module in typical Python installations.

## 🚀 Installation and Setup

### 1. Verify Python

Open a terminal or Windows Command Prompt and run:

```bash
python --version
```

If your system uses `python3`, use that command instead.

### 2. Download or clone the repository

After uploading the project to GitHub, clone it:

```bash
git clone <your-repository-url>
cd login-control-system
```

Replace `<your-repository-url>` with the URL of your repository.

### 3. Run the application

If your Python script is named `main.py`, run:

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file if it is different.

## ▶️ How It Works

### Step 1 — Database initialization

When the program starts, it creates a local SQLite database named:

```text
users.db
```

The program creates a `users` table if one does not already exist.

The table stores:

| Column | Purpose |
|---|---|
| `username` | Stores the username and acts as the primary key. |
| `password_hash` | Stores the hashed password value. |

The application also inserts its demonstration accounts if their usernames do not already exist.

### Step 2 — Username verification

The user enters a username.

The program queries the database to determine whether that username exists. If no matching user is found, it asks the user to try another username.

The query uses a parameterized SQL statement rather than combining user input directly into the SQL string.

### Step 3 — Password verification

After finding a valid username, the program asks for a password.

It hashes the entered password using SHA-256 and compares the result with the stored password hash.

If the values match, the application displays an access-granted message and exits the login function.

### Step 4 — Failed-login attempt handling

The program permits a maximum of five incorrect password attempts for the current login session.

After each incorrect password, it displays the number of attempts remaining.

Once the limit is reached, it displays a five-second countdown and exits.

## 🔄 Authentication Workflow

```text
       ┌────────────────────┐
       │   Start Program    │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ Create/Load SQLite │
       │      Database      │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │   Enter Username   │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ Username Exists?   │
       └──────┬───────┬─────┘
              │       │
            No│       │Yes
              ▼       ▼
       ┌──────────┐  ┌────────────────┐
       │ Try Again│  │ Enter Password │
       └────┬─────┘  └────────┬───────┘
            │                 │
            └───► Username    ▼
                  Check   ┌────────────────┐
                          │ Verify Hash    │
                          └───────┬────────┘
                                  │
                                  ▼
                          ┌────────────────┐
                          │ Password Match?│
                          └───────┬────────┘
                              │       │
                            Yes       No
                              │       │
                              ▼       ▼
                       ┌─────────┐ ┌──────────────┐
                       │ Access  │ │ Attempts     │
                       │ Granted │ │ Remaining?   │
                       └─────────┘ └──────┬───────┘
                                          │
                                    ┌─────┴─────┐
                                    │           │
                                 Yes│           │No
                                    ▼           ▼
                              Enter Again   Countdown
                                           and Exit
```

## 🔐 Understanding Password Hashing

This project uses SHA-256 through Python's `hashlib` module.

Hashing transforms a password into a fixed-length digest. The program stores the digest instead of storing the demonstration passwords directly in the database.

However, **SHA-256 is a general-purpose hash function, not a password-storage algorithm**.

Password hashing for real applications should use a purpose-built password hashing algorithm such as:

- **Argon2id**
- **scrypt**
- **bcrypt**

These algorithms are designed to make large-scale password guessing more expensive. Passwords should also be stored using appropriate salts and secure configuration.

The current implementation uses unsalted SHA-256, which is fast to calculate and therefore unsuitable for securely storing real user passwords.

## 🛡️ Security Considerations

### 1. Hard-coded demonstration credentials

The current source code contains demonstration usernames and passwords.

Hard-coded credentials should never be used as real account credentials or committed to a public repository as if they were secure defaults.

Before publishing, replace the demonstration-account mechanism with a safer account creation process and remove any credentials that should not be public.

### 2. Password storage

The current implementation stores unsalted SHA-256 hashes. Although it does not store the password as plain text in the database, this approach does not provide adequate password-storage protection for production use.

Use Argon2id, scrypt, or bcrypt with a suitable password-hashing library for a more secure implementation.

### 3. Attempt limits are temporary

The five-attempt limit exists only while the current program is running.

The countdown and program exit do **not** create a persistent account lock. Restarting the application resets the attempt counter.

A more robust system would track failed attempts and apply rate limits or lockout policies across sessions, with safeguards against denial-of-service abuse.

### 4. Username enumeration

The application explicitly reports when a username does not exist. This can reveal which usernames are registered.

Production authentication systems commonly use more generic login error messages to reduce this information disclosure.

### 5. Password input

The current implementation uses `input()` and strips leading or trailing whitespace from entered passwords.

For a more secure and predictable login experience, use `getpass.getpass()` to avoid echoing passwords in the terminal and define consistent password-handling rules.

## ⚠️ Limitations

- Uses unsalted SHA-256 rather than a dedicated password-hashing algorithm.
- Contains hard-coded demonstration credentials.
- Failed attempts are not persisted between program runs.
- The countdown does not implement a real account lock.
- Unknown usernames are reported explicitly.
- No account registration, password reset, or password change workflow is included.
- No multi-factor authentication is implemented.
- The application has not been audited or designed for production use.

## 🗺️ Future Improvements

Potential improvements for future versions include:

- Replace SHA-256 with Argon2id, scrypt, or bcrypt.
- Add secure user registration and password-change functionality.
- Hide password input using `getpass`.
- Implement persistent, carefully designed failed-login tracking.
- Add rate limiting and stronger abuse protection.
- Use generic error messages for unsuccessful logins.
- Add automated tests for valid credentials, invalid passwords, and unknown users.
- Improve database schema constraints and error handling.
- Separate authentication logic, database operations, and user-interface code.

## 📚 Learning Outcomes

This project provides hands-on practice with:

- Python authentication logic
- SQLite database creation and queries
- Password hashing and verification
- Parameterized SQL queries
- Failed-login attempt handling
- Basic access-control concepts
- Security weaknesses in simple authentication systems

## 📄 License

No license has been specified yet. If you intend to share this repository publicly, consider adding a `LICENSE` file that defines how others may use, modify, and distribute your code.

---

<div align="center">

**Built as a hands-on Python and cybersecurity learning project.**

*Learn authentication. Understand security. Keep improving.*

</div>
