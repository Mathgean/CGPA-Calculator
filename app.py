from flask import Flask, render_template, request

def clac(marks, credit):
    result = []
    for i in range(len(credit)):
        result.append(credit[i] * marks[i])
    for i in range(len(result)):
        if result[i] == 0:
            credit[i] = 0
    sum_total = 0
    for i in result:
        sum_total += i
    sum_credit = 0
    for i in credit:
        sum_credit += i
    try:
        gpa = sum_total / sum_credit
    except ZeroDivisionError:
        gpa = 0
    return gpa


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/sem1', methods=['GET', 'POST'])
def sem1():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        mini = int(request.form['mini'])
        marks = [ip, ai, mc, cd, ds, ipl, mad, mini]
        credit = [4, 4, 3, 3, 3, 4, 2, 2]
        gpa = clac(marks, credit)
        return render_template('sem1.html', data=gpa)
    return render_template('sem1.html')


@app.route('/sem2', methods=['GET', 'POST'])
def sem2():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        mini = int(request.form['mini'])
        marks = [ip, ai, mc, cd, ds, ipl, mad, mini]
        credit = [4, 4, 3, 3, 3, 3, 2, 2]
        gpa = clac(marks, credit)
        return render_template('sem2.html', data=gpa)
    return render_template('sem2.html')


@app.route('/sem3', methods=['GET', 'POST'])
def sem3():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        mini = int(request.form['mini'])
        nm = int(request.form['nm'])
        marks = [ip, ai, mc, cd, ds, ipl, mad, mini, nm]
        credit = [4, 4, 3, 3, 3, 2, 2, 2, 1]
        gpa = clac(marks, credit)
        return render_template('sem3.html', data=gpa)
    return render_template('sem3.html')


@app.route('/sem4', methods=['GET', 'POST'])
def sem4():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        mini = int(request.form['mini'])
        nm = int(request.form['nm'])
        marks = [ip, ai, mc, cd, ds, ipl, mad, mini, nm]
        credit = [4, 3, 3, 3, 3, 3, 2, 2, 1]
        gpa = clac(marks, credit)
        return render_template('sem4.html', data=gpa)
    return render_template('sem4.html')


@app.route('/sem5', methods=['GET', 'POST'])
def sem5():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        mini = int(request.form['mini'])
        net = int(request.form['net'])
        marks = [ip, ai, mc, cd, ds, ipl, mad, mini, net]
        credit = [4, 3, 3, 3, 3, 3, 2, 2, 2]
        gpa = clac(marks, credit)
        return render_template('sem5.html', data=gpa)
    return render_template('sem5.html')


@app.route('/sem6', methods=['GET', 'POST'])
def sem6():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        mini = int(request.form['mini'])
        pc = int(request.form['pc'])
        marks = [ip, ai, mc, cd, ds, ipl, mad, mini, pc]
        credit = [3, 3, 3, 4, 3, 2, 2, 1, 1]
        gpa = clac(marks, credit)
        return render_template('sem6.html', data=gpa)
    return render_template('sem6.html')


@app.route('/sem7', methods=['GET', 'POST'])
def sem7():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        mc = int(request.form['mc'])
        cd = int(request.form['cd'])
        ds = int(request.form['ds'])
        ipl = int(request.form['ipl'])
        mad = int(request.form['mad'])
        marks = [ip, ai, mc, cd, ds, ipl, mad]
        credit = [3, 3, 3, 3, 3, 2, 2]
        gpa = clac(marks, credit)
        return render_template('sem7.html', data=gpa)
    return render_template('sem7.html')


@app.route('/sem8', methods=['GET', 'POST'])
def sem8():
    if request.method == 'POST':
        ip = int(request.form['ip'])
        ai = int(request.form['ai'])
        marks = [ip, ai, nm]
        credit = [3, 10]
        gpa = clac(marks, credit)
        return render_template('sem8.html', data=gpa)
    return render_template('sem8.html')


@app.route('/cgpa', methods=['GET', 'POST'])
def cgpa():
    if request.method == 'POST':
        try:
            result = []
            num = int(request.form['op'])
            for i in range(1, num + 1):
                se = 'sem' + str(i)
                result.append(float(request.form[se]))
            suma = 0.0
            for i in result:
                suma = suma + i
            a = suma / num
        except ZeroDivisionError:
            a = 0
        return render_template('cgpa.html', data=a)
    return render_template('cgpa.html')


if __name__ == "__main__":
    app.run(debug=True)
