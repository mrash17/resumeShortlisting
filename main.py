from flask import Flask  , redirect , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signin") 
def login():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/job-post")
def jobpost():
    return render_template('jobPost.html')

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