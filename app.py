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

@app.route('/student_resume', methods=['GET','POST'])
def student_resume():
    if request.method=="POST":
        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]
        number=request.form["number"]
        address=request.form["address"]
        title = request.form["title"]
        soft_skill= request.form["soft-skill"]
        technical_skill= request.form["technical-skill"]
        position=request.form["position"]
        company_name=request.form["company-name"]
        period_fom=request.form["period-from"]
        period_to = request.form["period-to"]
        description = request.form["description"]
        project1_title=request.form["project1-title"]
        project1=request.form["project1"]
        project1_tech=request.form["project1-tech"]
        project2_title=request.form["project2-title"]
        project2=request.form["project2"]
        project2_tech=request.form["project2-tech"]
        education=request.form["education"]
        language=request.form["language"]
        sql = "INSERT INTO student_resume(name, dob, email ,number ,address ,title ,soft-skill ,technical-skill ,position ,company-name ,period-from ,period-to ,description ,project1-title ,project1 ,project1-tech ,project2-title ,project2 ,project2-tech ,education,language ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name, dob, email ,number ,address ,title ,soft_skill ,technical_skill ,position ,company_name ,period_fom ,period_to ,description ,project1_title ,project1 ,project1_tech ,project2_title ,project2 ,project2_tech ,education,language)
    return render_template('student_resume.html')

@app.route('/job_post', methods=['GET','POST'])
def job_post():
    if request.method=="POST":
        cname = request.form["cname"]
        columns = request.form.getlist('skill[]')
        skill_query=[]
        for x in columns:
            skill = request.form["skill[]"]
            skill_query.append(getattr(skill, x))
        
        experience = request.form["experience"]
        education=request.form["education"]
        city=request.form["city"]
        sql = "INSERT INTO student_resume(cname ,skill_query ,experience ,education ,city ) VALUES (%s,%s,%s,%s,%s)"
        val = (cname ,skill_query ,experience ,education ,city)
    return render_template('dashboard.html')

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
