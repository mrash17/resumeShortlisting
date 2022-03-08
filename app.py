from flask import Flask,render_template, request,session, redirect, url_for, flash
import pymysql.cursors
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "abdhghsbghddvbnbds"

con = pymysql.Connect(host="127.0.0.1",user="root",passwd="",db="resumeshortlisting")
cur = con.cursor()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signin", methods=['GET','POST']) 
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        check_email = "SELECT * FROM recruiter WHERE company_email = '"+email+"'"
        cur.execute(check_email)
        get_one_email = cur.fetchone()
        if (not get_one_email):
            flash("You entered wrong email address")
            return redirect(url_for('login'))
        elif(get_one_email[3]!=password):
            flash("Wrong Password")
            return redirect(url_for('login'))
        else:
            session['loggedin'] = True 
            return redirect(url_for('dashboard'))
    return render_template('signin.html')

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=="POST":
        email = request.form["email"]
        check_email = "SELECT company_email FROM recruiter WHERE company_email = '"+email+"'"
        cur.execute(check_email)
        first_email = cur.fetchone()
        if(not first_email):
            company_name = request.form["cname"]
            password = request.form["password"]
            cpassword = request.form["cpassword"]
            sql = "INSERT INTO recruiter(company_email, company_name, password ) VALUES (%s,%s,%s)"
            val = (email, company_name, password)
            if(cpassword == password):
                cur.execute(sql,val)
                con.commit()
            else:
                flash("Password and confirm password should be same!")
                return redirect(url_for('signup'))
            sql2 = "SELECT id FROM recruiter WHERE company_email = '"+email+"'"
            cur.execute(sql2)
            myid = cur.fetchone()
            # print(myid[0])
            session['id'] = myid[0]
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
        else:
            flash("The email is already in use! Try using another")
            return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route("/dashboard")
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))   

@app.route("/job-post" , methods=["GET" , "POST"])
def jobpost():
     if 'loggedin' in session:
        if request.method == "POST":
            company_name = request.form["cname"]
            check_id = "select id from recruiter where company_name = '"+company_name+"'"
    return render_template('jobPost.html')

@app.route("/student-resume")
def studentresume():
    return render_template('student_resume.html')

@app.route("/resume1")
def template():
    return render_template("template1.html")

@app.route("/resume2")
def template2():
    return render_template("template2.html")

@app.route("/resume3")
def template3():
    return render_template("template3.html")

if __name__=='__main__':
    app.run(debug=True)