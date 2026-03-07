# Personal Expense Tracker (CLI)

## Project Description
This is a simple command-line Python application that helps users track their daily expenses.

Users can:
- Add new expenses
- View all expenses
- View total spending
- View spending by category
- Save expenses to a file

The data is stored locally in a JSON file.

---

## Project Structure

expense-tracker/
├─ src/
│ ├─ main.py
│ ├─ tracker.py
│ └─ storage.py
├─ data/
│ └─ expenses.json
├─ README.md
└─ .gitignore

---

## Setup Instructions

1. Create a virtual environment
python -m venv .venv

```
2. Activate the virtual environment

Mac/Linux:
source .venv/bin/activate

```

Windows:
```

`.venv\Scripts\activate`

```

3. Install required packages
```

`pip install tabulate`

```

---

## Run the application

Run the following command from the project folder:
```

`python src/main.py`

```

---

## Features

- Add expenses
- View expense list
- Total spending calculation
- Category summary
- Data stored using JSON
```