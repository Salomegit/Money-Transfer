# REST Money Transfer API

This is a simple Django REST Framework (DRF) API for managing user money transfers. The API allows for the creation of accounts with a specified balance, retrieving account details by account ID, and transferring money between accounts.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- SQLite (default database)

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to create the necessary database tables**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API Endpoints

### 1. **Create an Account**
**URL**: `/accounts/`  
**Method**: `POST`  
**Description**: Creates a new account with the specified account number and initial balance.  

#### Request Body:
```json
{
  "account_no": "account1",
  "balance": 1000.0
}
```

#### Response:
```json
{
  "id": 1,
  "account_no": "account1",
  "balance": 1000.0
}
```

---

### 2. **Get Account Details**
**URL**: `/accounts/<int:account_id>/`  
**Method**: `GET`  
**Description**: Retrieves the details of an account based on the provided `account_id`.

#### Response:
```json
{
  "id": 1,
  "account_no": "account1",
  "balance": 1000.0
}
```

---

### 3. **Transfer Money Between Accounts**

