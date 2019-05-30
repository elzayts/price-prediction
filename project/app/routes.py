from app import app
from flask import render_template, request, redirect, url_for
#from DB_get import get_rows
from app.form import MyForm
from app.my import *


@app.route("/index1", methods=['GET', 'POST'])
def main():
    form = MyForm()

    if request.method == 'POST' and form.validate_on_submit():
       area=int(form.distr.data)
       return redirect(url_for('info', ar=area, res=xgb_r.predict([float(form.square_min.data), float(form.square_max.data), 0.0,  float(form.rooms.data),  float(form.house_type.data),  float(form.state.data),  float(form.distr.data)])[0]))

    else:
        return render_template("index1.html", form=form)


@app.route("/info", methods=['GET'])
def info():
    return render_template("info.html", ar1=request.args.get("ar"), p=request.args.get("res"))


@app.route("/statistics", methods=['GET'])
def stat():
    return render_template("statistics.html")






