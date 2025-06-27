# 💰 Mutex & Money: Concurrent Banking System with Thread Synchronization

### 🚀 Built using Python | Threading | Mutex (Lock)

---

> 🎥 *Simulates multiple concurrent deposits, withdrawals, and transfers with real-time balance updates & synchronization using mutex.*

---

## 📖 Overview

**Mutex & Money** is a Python project that simulates real-world banking operations — deposit, withdrawal, and transfer — executed by multiple users (threads) simultaneously. The goal is to ensure **data integrity** using proper **thread synchronization (mutex locks)**.

---

## 🛠️ Features

- 🧵 Multithreaded banking transactions
- 🔒 Mutex-based synchronization (no race conditions!)
- 🔁 Transfer, deposit, and withdraw simulation
- ✅ Final balance consistency
- 📊 Terminal log showing transaction flow
- 🖼️ Optional: Extendable with GUI using Tkinter

---

## 📂 Project Structure

```
mutex-and-money/
├── bank_account.py         # Bank logic (deposit, withdraw, transfer)
├── main.py                 # Transaction simulation & thread logic
├── requirements.txt        # Python dependencies (standard lib only)
├── README.md               # You’re reading it
├── .gitignore              # Ignores .pyc, __pycache__, etc.
└── screenshots/            # Add demo screenshot or gif
```

---

## 📦 Installation & Setup

### ✅ Prerequisites
- Python 3.8 or higher

### 📥 Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/mutex-and-money.git
cd mutex-and-money

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows

# 3. Install dependencies (if any)
pip install -r requirements.txt

# 4. Run the project
python main.py
```

---

## 📈 Sample Output (Terminal)

```
[ACC001] Depositing 200
[ACC002] Withdrawing 100
[ACC001] Transferring 300 to ACC002
[ACC002] New balance: 900
[ACC001] New balance: 500

Final Balances:
ACC001: ₹500
ACC002: ₹900
```

---

## 🔧 Extending the Project

- ✅ Add a **Tkinter GUI**
- 💾 Save transaction logs to a file
- 🔐 Role-based access (Admin/User)
- 📉 Transaction history

---

## 👨‍💻 Authors
- **Dhruv Joshi** — [dhruvjoshi26a@gmail.com](mailto:dhruvjoshi26a@gmail.com)
Course: **Operating Systems (TCS-601)**

---

## 📚 References

- [GeeksforGeeks – Python Multithreading](https://www.geeksforgeeks.org/multithreading-in-python)
- [Python threading docs](https://docs.python.org/3/library/threading.html)
- [Operating Systems - Silberschatz, Galvin, Gagne]
