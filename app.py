from Solutions import *
from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/task6', methods=["POST", "GET"])
def task6():
    ctx = {}
    if request.method == "POST":
        q = float(request.form['Q'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        m = float(request.form['m'])
        ctx = {"task": Task6(q, x, y, m).split("\n"), "result": Calculate6(q, x, y, m).split("\n")}
    return render_template(template_name_or_list='form1.html', context=ctx)


@app.route('/task7', methods=["POST", "GET"])
def task7():
    ctx = {}
    if request.method == "POST":
        chp1 = float(request.form['chp1'])
        chp2 = float(request.form['chp2'])
        b1 = float(request.form['b1'])
        b2 = float(request.form['b2'])
        ctx = {"task": Task7(chp1, chp2, b1, b2).split("\n"), "result": Calculate7(chp1, chp2, b1, b2).split("\n")}
    return render_template(template_name_or_list='form2.html', context=ctx)


@app.route('/task8', methods=["POST", "GET"])
def task8():
    ctx = {}
    if request.method == "POST":
        m1 = float(request.form['m1'])
        m2 = float(request.form['m2'])
        m3 = float(request.form['m3'])
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        pn = float(request.form['pn'])
        ctx = {"task": Task8(m1, m2, m3, n1, n2, n3, pn).split("\n"),
               "result": Calculate8(m1, m2, m3, n1, n2, n3, pn).split("\n")}
    return render_template(template_name_or_list='form3.html', context=ctx)


@app.route('/', methods=["POST", "GET"])
def home():
    return render_template(template_name_or_list='index.html')



