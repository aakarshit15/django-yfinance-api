from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .yf_fetch import *

@api_view(["GET"])
def index(request):
    return render(request, "index.html")

@api_view(["GET"])
def get_balance_sheet(request, ticker):
    try:
        final_json_file = get_balance_sheet_as_json(ticker)
        return Response(final_json_file)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["GET"])
def get_cash_flow(request, ticker):
    try:
        final_json_file = get_cash_flow_as_json(ticker)
        return Response(final_json_file)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["GET"])
def get_historical_data(request, ticker):
    try:
        data = yf.Ticker(ticker).history(period="max")
        historical_data_json = json.loads(convert_to_json(data))
        return Response(historical_data_json, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["GET"])
def get_sector_and_industry(request, ticker):
    try:
        data = yf.Ticker(ticker).info
        sector = data.get("sector", "N/A")
        industry = data.get("industry", "N/A")
        sector_and_industry_data = {"ticker": ticker, "sector": sector, "industry": industry}
        return Response(sector_and_industry_data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["GET"])
def get_calendar(request, ticker):
    final_json_file = get_calendar_as_json(ticker)
    return Response(final_json_file)
