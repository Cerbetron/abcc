"""Simple Flask server to display agent usage reports."""
from __future__ import annotations

import os
from flask import Flask, send_from_directory, render_template
import pandas as pd

LOG_FILE = os.path.join('logs', 'agent_usage_log.csv')

app = Flask(__name__, static_url_path='')

@app.route('/')
def report() -> str:
    # Render static HTML template. Data is loaded client side via JavaScript.
    return render_template('report.html')

@app.route('/log.csv')
def log_file():
    return send_from_directory('logs', 'agent_usage_log.csv')


def load_data():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    return pd.DataFrame()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
