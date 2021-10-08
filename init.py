from flask import Flask, render_template, request
import get_all




app = Flask(__name__)



@app.route("/result")
def show_database():
    result = get_all.see_all()
    return render_template('index.html', out=result)



@app.route("/id_record", methods=['POST'])
def id_record():
    id = request.form['send_id']
    if id != '':
        result = get_all.get_id(id)
        return render_template('index.html', out=result)
    else:
        return render_template('index.html', out="Please enter the record's ID")


@app.route("/n_record", methods=['POST'])
def n_record():
    n = request.form['send_n']
    if n != '':
        result = get_all.get_n(n)
        return render_template('index.html', out=result)
    else:
        return render_template('index.html', out="Please enter N")


@app.route("/delete_id", methods=['POST'])
def delete_id():
    id = request.form['send_del_id']
    if id != '':
        result = get_all.del_id(id)
        return render_template('index.html', out=result)
    else:
        return render_template('index.html', out="Please enter ID")


@app.route("/edit_record", methods=['POST'])
def edit_record():
    id = request.form['edit_id']
    name = request.form['edit_name']
    desc = request.form['edit_desc']
    number = request.form['edit_number']
    price = request.form['edit_price']
    rare = request.form['edit_rare']
    if id != '' and name != '' and desc != '' and number != '' and price != '' and rare != '':
        result = get_all.edit(id, name, desc, number, price, rare)
        return render_template('index.html', out=result)
    else:
        return render_template('index.html', out="Please enter data into all fields")



@app.route("/create_record", methods=['POST'])
def create_record():
    name = request.form['create_name']
    desc = request.form['create_desc']
    number = request.form['create_number']
    price = request.form['create_price']
    rare = request.form['create_rare']
    if name != '' and desc != '' and number != '' and price != '' and rare != '':
        result = get_all.create(name, desc, number, price, rare)
        return render_template('index.html', out=result)
    else:
        return render_template('index.html', out="Please enter data into all fields")



@app.route("/clear")
def clear():
    return render_template('index.html')


@app.route("/")
def about():
    return render_template('index.html')


