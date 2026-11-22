# Smart Expense Tracker System

A web-based expense tracking application built with Python and Flask. The system helps users record, organize, and monitor their personal expenses through a simple dashboard.

## Features

- **User Authentication** – User registration, login, and logout.
- **Expense Management** – Record expenses with details such as amount, category, date, description, and payment method.
- **Dashboard** – View and monitor recorded expenses.
- **Database Management** – Store application data using SQLite.
- **Secure Password Handling** – Store passwords using password hashing.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration |
| Flask-Login | User authentication |
| Flask-WTF | Form handling and validation |
| WTForms | Form creation |
| SQLite | Database |
| HTML/CSS | Frontend structure and styling |
| Bootstrap | Responsive user interface |

## Project Structure

```text
Smart Expense Tracker System/
│
├── app.py
├── config.py
├── extensions.py
├── forms.py
├── models.py
├── requirements.txt
├── .gitignore
│
├── routes/
│   ├── auth.py
│   └── expenses.py
│
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    └── add_expense.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ADRIANDARYL/Smart-Expense-Tracker-System.git
```

### 2. Navigate into the project directory

```bash
cd Smart-Expense-Tracker-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Set a secure Flask secret key before running the application.

For Windows Command Prompt:

```cmd
set SECRET_KEY=your-secure-secret-key
```

### 7. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Database

The application uses SQLite for data storage. Database tables are managed through Flask-SQLAlchemy.

## Future Improvements

- Monthly and weekly expense reports.
- Budget tracking and management.
- Data visualization using charts.
- Expense filtering and search.
- Export expense reports.
- Improved financial insights.

## Author

**Daryl Chacha**

GitHub: [@ADRIANDARYL](https://github.com/ADRIANDARYL)

## License

This project is developed for educational and personal use.
