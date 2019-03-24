from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

filters=[]

@app.route("/main", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/ans", methods=['POST', 'GET'])
def get_filt():
    str=request.form['street']
    room= request.form['rooms']

    filters.append(str)
    filters.append(room)

    return redirect(url_for('main'))



