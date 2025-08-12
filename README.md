Stock Price Alerting System
This is a Django-based stock price alerting system that allows users to set threshold and duration-based alerts for predefined stocks. It fetches stock prices from Twelve Data API (free tier), checks conditions periodically, and sends email notifications when alerts are triggered.
Features

User registration and JWT authentication.
Create, view, toggle, and list alerts.
View triggered alerts.
Periodic price fetching and alert checking every 5 minutes.
Email notifications using Gmail SMTP.
Predefined stocks: AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM, V, WMT.

Setup Locally

Clone the repo: git clone <repo-url>
Create virtual env: python -m venv venv
Activate: source venv/bin/activate
Install deps: pip install -r requirements.txt
Set env vars in .env or export:
API_KEY=your_twelvedata_key
EMAIL=your_gmail
PASSWORD=your_gmail_app_password (use app password for Gmail)
SECRET_KEY=your_secret


Run migrations: python manage.py makemigrations && python manage.py migrate
Add crontab jobs: python manage.py crontab add
Run server: python manage.py runserver
Show crontab: python manage.py crontab show
Remove crontab: python manage.py crontab remove (if needed)

API Endpoints

/api/users/register/ : POST to register user.
/api/users/login/ : POST to get JWT tokens.
/api/users/refresh/ : POST to refresh token.
/api/alerts/alerts/ : GET/POST to list/create alerts (auth required).
/api/alerts/alerts/<id>/ : GET/PUT/DELETE for specific alert.
/api/alerts/alerts/<id>/toggle_active/ : POST to toggle active.
/api/alerts/alerts/triggered/ : GET to list triggered alerts.


