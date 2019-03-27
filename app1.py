from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

filters = []


@app.route("/main", methods=['GET', 'POST'])
def main():
    return render_template("index1.html")

#@app.route("/info", methods=['GET'])
#def show():
 #   filt=tuple(filters)
  #  filters.clear()
   # return render_template("info.html", f=filt)


@app.route("/ans", methods=['POST', 'GET'])
def get_filt():

    str=request.form['street']
    room= request.form['rooms']
    #distr=request.form['district']
    #t_area = request.form['total_area']
    #l_area = request.form['living_area']
    #residence= request.form['residence_type']

    filters.append(str)
    filters.append(room)
    #filters.append(distr)
    #filters.append(t_area)
    #filters.append(l_area)
    #filters.append(residence)

    return redirect(url_for('main'))





