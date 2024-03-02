from flask import Flask, render_template, url_for, request

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

if __name__ == "__main__":
    app.run(debug=True)