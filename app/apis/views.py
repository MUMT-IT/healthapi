import csv
from io import StringIO

import pandas as pd
import requests
from flask import jsonify, Response, request

from . import apis
from app import engine


def generate(df):
    data = StringIO()
    w = csv.writer(data)

    # write header
    w.writerows(df.to_csv())
    return data.getvalue()

@apis.route('/testing')
def test():
    return jsonify({ 'message': 'I am good'})


@apis.route('/tests')
def get_tests():
    resp = requests.get('http://localhost:8080/apis/tests')
    df = pd.DataFrame(resp.json())
    return Response(df.to_csv(doublequote=True))


@apis.route('/tests-by-month')
def get_tests_by_month():
    resp = requests.get('http://localhost:8080/apis/tests-by-month')
    df = pd.DataFrame(resp.json())
    return Response(df.to_csv(doublequote=True, index=False))


@apis.route('/customers-by-month')
def get_customers_by_month():
    resp = requests.get('http://localhost:8080/apis/customers-by-month')
    df = pd.DataFrame(resp.json())
    return Response(df.to_csv(doublequote=True, index=False))
