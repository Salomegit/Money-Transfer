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
  "account_no": 001,
  "balance": 1000.0
}
```

#### Response:
```json
{
  "id": 1,
  "account_no": 001,
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
  "account_no": 001,
  "balance": 1000.0
}
```

---

### 3. **Transfer Money Between Accounts**


**URL**: `/accounts/transactions/`  
**Method**: `POST`  
**Description**: Handles the transfer of funds between accounts.
#### Request Body:
```json
{
  "source_account": 1,            // ID of the source account 
  "destination_account": 2,       // ID of the destination account 
  "amount": 100.0                // Amount to be transferred 
}
```
#### Response:
```json
{
  "id": 1,
  "source_account": 1,
  "destination_account": 2,
  "amount": 1000.0,
  "created_at": "2025-01-08T12:00:00Z"
}
```

---