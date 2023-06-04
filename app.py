from flask import Flask, render_template, request, redirect
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

@app.route('/', methods=['POST','GET'])
def index():
    return redirect("/login/")

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            idnumber = request.form.get('idnumber')
            if (not username) or (not idnumber):
                return render_template('error.html')

            try:

                cursor.execute("SELECT * FROM service_db WHERE username=%s AND idnumber=%s", (str(username), str(idnumber)))
                records = cursor.fetchone()[1]
            except TypeError:
                return render_template("er.html")
            return render_template('account.html', full_name=records)

        elif request.form.get("registration"):
            return redirect("/registration/")


    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        username = request.form.get('username')
        idnumber = request.form.get('idnumber')
        lastname = request.form.get('lastname')
        firstname = request.form.get('firstname')
        department = request.form.get('department')
        cohort1 = request.form.get('cohort1')
        course1 = request.form.get('course1')
        role1 = request.form.get('role1')
        course2 = request.form.get('course2')
        role2 = request.form.get('role2')
        course3 = request.form.get('course3')
        role3 = request.form.get('role3')
        course4 = request.form.get('course4')
        role4 = request.form.get('role4')
        course5 = request.form.get('course5')
        role5 = request.form.get('role5')
        course6 = request.form.get('course6')
        role6 = request.form.get('role6')
        course7 = request.form.get('course7')
        role7 = request.form.get('role7')
        course8 = request.form.get('course8')
        role8 = request.form.get('role8')



        if (not username) or (not idnumber) or (not lastname) or (not firstname) or (not department) or (not cohort1):
            return render_template("error.html")
        if idnumber:
            cursor.execute('SELECT * FROM service_db')
            rows = cursor.fetchall()
            for row in rows:
                if idnumber == row[2]:
                    return render_template("repeat.html")
            cursor.execute('INSERT INTO service_db (username, idnumber, lastname, firstname,  department, cohort1, course1, role1, course2, role2, course3, role3, course4, role4, course5, role5, course6, role6, course7, role7, course8, role8) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s);',
                       (str(username), str(idnumber), str(lastname), str(firstname), str(department), str(cohort1), str(course1), str(role1), str(course2), str(role2), str(course3), str(role3), str(course4), str(role4), str(course5), str(role5), str(course6), str(role6), str(course7), str(role7), str(course8), str(role8)))
            conn.commit()

        return redirect('/login/')
    return render_template('registration.html')
