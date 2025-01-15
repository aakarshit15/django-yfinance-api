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
Only following combinations work:<br>

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
            <td>1m</td>
        </tr>
        <tr>
            <td>1d</td>
            <td>5m</td>
        </tr>
        <tr>
            <td>1d</td>
            <td>15m</td>
        </tr>
        <tr>
            <td>1d</td>
            <td>30m</td>
        </tr>
        <tr>
            <td>1d</td>
            <td>1d</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>5m</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>15m</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>30m</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>1d</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>1mo</td>
        </tr>
    </tbody>
</table>

| Period  | Interval |
| ------- | -------- |
| 1d      | 1m       |
| 1d      | 5m       |
| 1d      | 15m      |
| 1d      | 30m      |
| 1d      | 1d       |
| 1mo     | 5m       |
| 1mo     | 15m      |
| 1mo     | 30m      |
| 1mo     | 1d       |
| 1mo     | 1mo      |
Example: `http://127.0.0.1:8000/api/get_historical_data/RELIANCE.NS/?interval=1d&period=1mo`<br>

- Sector and Industry Information<br>
Link: `server_link/api/get_sector_and_industry/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_sector_and_industry/RELIANCE.NS`<br>

- Calendar information<br>
Link: `link/api/get_calendar/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_calendar/RELIANCE.NS`<br>
