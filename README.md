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
Link: `server_link/api/get_balance_sheet/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_balance_sheet/RELIANCE.NS`<br>

- Cash Flow<br>
Link: `server_link/api/get_cash_flow/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_get_flow/RELIANCE.NS`<br>

- Historical Data<br>
Link: `server_link/api/get_historical_data/<ticker_symbol>/?interval=<interval>&period=<interval>`<br>
Example: `http://127.0.0.1:8000/api/get_historical_data/RELIANCE.NS/?interval=1d&period=1mo`<br>
Please Note: Only following combinations work:<br>
<table>
    <thead>
        <tr>
            <th>Period</th>
            <th>Interval</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1d</td>
            <td>1m, 5m, 15m, 30m, 1d</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>5m, 15m, 30m, 1d, 1mo</td>
        </tr>
    </tbody>
</table><br>

- Sector and Industry Information<br>
Link: `server_link/api/get_sector_and_industry/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_sector_and_industry/RELIANCE.NS`<br>

- Calendar information<br>
Link: `link/api/get_calendar/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_calendar/RELIANCE.NS`<br>
