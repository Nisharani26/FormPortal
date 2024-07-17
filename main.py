from flask import Flask,render_template,request,session,redirect 
import sqlite3


database_connection = sqlite3.connect('database.db',check_same_thread=False)
#cursor is used to execute statements
database_cursor=database_connection.cursor()

app=Flask(__name__)
app.secret_key="nisharani"


@app.route('/home')
def home():
    return render_template('index.html')
   
    

@app.route('/login')
def login():
    return render_template('login.html')
   
@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signupsubmission',methods=["POST"])
def signupsubmission():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    confirmpassword=request.form["confirmpassword"]
    print(name  , username ,password ,confirmpassword)
    session["name"]=name
    session["username"]=username
    session["password"]=password
    session["confirmpassword"]=confirmpassword

    database_cursor.execute("insert into user(name,username,password,confirmpassword) values(name,username,password,confirmpassword)")
    database_connection.commit()
    database_connection.close()
    return redirect('/')

@app.route('/loginsubmission',methods=["POST","Get"])
def loginsubmission():
    username=request.form["username"]
    password=request.form["password"]
    session["username"]=username
    session["password"]=password
    if request.method=="POST":
         if session["username"] =="nisha123":
             return redirect('/')
         else:
             return "Invalid Username and password"
    else:
        return render_template('login.html')
    

@app.route('/createform')
def createform():
    return render_template('createform.html')

@app.route('/fillform')
def fillform():
    return render_template('fillform.html')

@app.route('/manageform')
def manageform():
    return render_template('manageform.html')

@app.route('/postedform')
def postedform():
    return render_template('postedform.html')

@app.route('/submittedform')
def submittedform():
    return render_template('submittedform.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')



if (__name__=="__main__"):
    app.run(debug=True)

    