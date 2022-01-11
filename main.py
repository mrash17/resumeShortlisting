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

if __name__=='__main__':
    app.run(debug=True)