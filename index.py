from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine,
from DB_get import get_rows
app=Flask(__name__)

filt = {}
db = create_engine('postgresql+psycopg2://postgres:tiger@localhost/test')

@app.route("/index1", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        filt['room'] = request.form['rooms']
        filt['distr']=request.form['district']
        # filt[t_area] = request.form['total_area']
        # filt[l_area] = request.form['living_area']
        # filt[residence]= request.form['residence_type']
        r = get_rows(filt['room'])
        return redirect(url_for('show'))
    else:
      return render_template("index1.html")


@app.route("/info", methods=['GET'])
def show():
    return render_template("info.html")
