from flask import Flask, render_template, url_for
from weasyprint import HTML

app = Flask(__name__)



@app.route("/dd")
def function():
    HTML(string=render_template('about.html')).write_pdf("report.pdf")
    return ("itworked")


if __name__ == '__main__':
    app.run(debug=True)
