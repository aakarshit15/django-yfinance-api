# Quickyearning_Backend_Django
<br>

### Packages Required
Run these in command prompt of project directory:<br>
`pip install django`<br>
`pip install djangorestframework`<br>
`pip install django-cors-headers`<br>
`pip install yfinance`<br>
<br>

### How to start Server
To start the django server, run this command in terminal of the django_backend directory:<br>
`python manage.py runserver`<br>
<br>

### Documentation to fetch api

- Balance Sheet<br>
Link: `link/api/get_balance_sheet/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_balance_sheet/RELIANCE.NS`<br>

- Cash Flow<br>
Link: `link/api/get_cash_flow/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_get_flow/RELIANCE.NS`<br>

- Historical Data<br>
Link: `link/api/get_historical_data/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_historical_data/RELIANCE.NS`<br>

- Sector and Industry Information<br>
Link: `link/api/get_sector_and_industry/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_sector_and_industry/RELIANCE.NS`<br>

- Calendar information<br>
Link: `link/api/get_calendar/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_calendar/RELIANCE.NS`<br>
