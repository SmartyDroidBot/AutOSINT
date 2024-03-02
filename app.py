from flask import Flask, render_template, url_for, request
import re
from method.geoloc import geoip
app = Flask(__name__)

@app.route('/')
def index():
    if request.method=="POST":
        query=request.form['query']
        type=verify_input(query)
        if type==1:
            geoip(query)
            

    else:
        return render_template('index.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)


#verifiying input
def verify_input(input_str):
    # Regular expressions for phone number, IP address, and email ID
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Check if input matches phone number pattern
    if re.match(phone_pattern, input_str):
        return 1

    # Check if input matches IP address pattern
    elif re.match(ip_pattern, input_str):
        return 2

    # Check if input matches email ID pattern
    elif re.match(email_pattern, input_str):
        return 3

    # If input doesn't match any pattern, return None
    else:
        return -1