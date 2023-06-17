import sys, os

INTERP = os.path.join(os.environ['HOME'], '', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import math

application = Flask(__name__)

@application.route('/simple')
def output_simple():
    out_text = 'hello world now'
    return render_template('output.html', arithmetic=out_text)

@application.route('/chain')
def opt_chain():
    return "Hello World"

@application.route('/numbers')
def hello():
    ticker = 'NQ=F'
    data = yf.download(tickers=ticker, period='6mo')
    return data.to_html(header='true', table_id='table')