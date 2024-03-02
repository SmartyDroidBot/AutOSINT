from flask import Flask, render_template, url_for, request

from meths.meth import geoip
app = Flask(__name__)

@app.route('/')
def index():
    if request.method=="POST":
        query=request.form['query']

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