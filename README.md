# 📈 Stock Price Alerting System

A **Django-based** application that lets users create **threshold** and **duration-based** alerts for predefined stocks.  
It fetches stock prices from the **[Twelve Data API](https://twelvedata.com/)** (free tier), checks alert conditions **every 5 minutes**, and sends **email notifications** when alerts are triggered.  

---

## 🚀 Features

- **User Registration & JWT Authentication** (secure endpoints).
- **Alert Management**  
  - Create, view, update, delete alerts.
  - Toggle alert activation.
  - View triggered alerts.
- **Predefined Stock List**:  
  ```
  AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM, V, WMT
  ```
- **Automated Price Monitoring** (via Django-crontab, runs every 5 minutes).
- **Email Notifications** (using Gmail SMTP & app passwords).

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (SimpleJWT)
- **Task Scheduling**: Django-crontab
- **Email Service**: Gmail SMTP
- **Stock Data API**: Twelve Data API (Free Tier)
- **Database**: PostgreSQL

---

## 📦 Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mahmoudAshraf283/farapi.git
cd farapi
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables  
Create a `.env` file in the root directory or export variables manually:
```env
API_KEY=your_twelvedata_key
EMAIL=your_gmail
PASSWORD=your_gmail_app_password  # Use Gmail App Password (not your actual password)
SECRET_KEY=your_django_secret
```

> 💡 **Tip:** To generate a Gmail App Password, enable 2FA in your Google account.

---

## ⚙️ Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ⏱️ Scheduling Tasks (Price Check Every 5 Minutes)
```bash
python manage.py crontab add      # Add the job
python manage.py crontab show     # Verify job is added
```
To remove the cron job:
```bash
python manage.py crontab remove
```

---

## ▶️ Run the Development Server
```bash
python manage.py runserver
```
Access the app at: **http://127.0.0.1:8000/**

---

## 📡 API Endpoints

### **Auth**
| Method | Endpoint                 | Description             |
|--------|--------------------------|-------------------------|
| POST   | `/api/users/register/`   | Register a new user     |
| POST   | `/api/users/login/`      | Get JWT tokens          |
| POST   | `/api/users/refresh/`    | Refresh JWT token       |

### **Alerts**
| Method | Endpoint                                         | Description                 |
|--------|--------------------------------------------------|-----------------------------|
| GET    | `/api/alerts/alerts/`                            | List all alerts (auth)      |
| POST   | `/api/alerts/alerts/`                            | Create a new alert (auth)   |
| GET    | `/api/alerts/alerts/<id>/`                       | Get alert details           |
| PUT    | `/api/alerts/alerts/<id>/`                       | Update alert details        |
| DELETE | `/api/alerts/alerts/<id>/`                       | Delete alert                |
| POST   | `/api/alerts/alerts/<id>/toggle_active/`         | Toggle alert activation     |
| GET    | `/api/alerts/alerts/triggered/`                  | List triggered alerts       |

---

## 📌 Notes
- This project uses **Twelve Data API free tier**, which has request limits.
- You **must** use a Gmail App Password for email notifications.
- Cron jobs run every **5 minutes** by default — configurable in `settings.py`.


