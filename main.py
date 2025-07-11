from flask import Flask,render_template,request,session,redirect 
import sqlite3

app=Flask(__name__)
app.secret_key="nisharani"

@app.route('/')
def home():
    return render_template('index.html')
    # if "username" in session:
    #    return render_template('index.html')
    # else:
    #    return redirect('/login')

@app.route('/login')
def login():
    # return render_template('login.html')
    if "username" in session:
        return redirect('/')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("username")
    return redirect('/login')
   
@app.route('/signup')
def signup():
    # print("signup"+username)
    if "username" in session:
        return redirect('/')
    else:
        return render_template('signup.html')


@app.route('/signupsubmission',methods=["POST"])
def signupsubmission():
    database_connection = sqlite3.connect('database.db',check_same_thread=False)
    database_cursor=database_connection.cursor()
    name=request.form["name"]
    email=request.form["email"]
    username=request.form["username"]
    password=request.form["password"]
    confirmpassword=request.form["confirmpassword"]
    print(name  , username ,password ,confirmpassword)
    session["name"]=name
    session["email"]=email
    session["username"]=username
    session["password"]=password
    session["confirmpassword"]=confirmpassword
    database_cursor.execute("insert into user(name,email,username,password,confirmpassword) values(?,?,?,?,?)",(name,email,username,password,confirmpassword))
    database_connection.commit()
    database_connection.close()
    print(session["username"])
    return redirect('/signup')

@app.route('/loginsubmission',methods=["POST","GET"])
def loginsubmission():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        database_connection = sqlite3.connect('database.db',check_same_thread=False)
        database_cursor=database_connection.cursor()
        data = database_cursor.execute("SELECT password, username FROM USER WHERE username = ?",(username,)).fetchone()
        database_connection.commit()
        database_connection.close()
        print(data)
        print(password)
        # print(type(data[0])==type(password))
        if (data != None and password == data[0]):
            session["username"]=username
            print(session["username"])
            return redirect('/')
        else:
            return "Invalid Username and password"
    else:
        return redirect('/') 

@app.route('/dashboard/createform')
def createform():
    return render_template('createform.html')

@app.route('/dashboard/fillform')
def fillform():
    return render_template('fillform.html')

@app.route('/dashboard/manageform')
def manageform():
    return render_template('manageform.html')

@app.route('/dashboard/postedform')
def postedform():
    return render_template('postedform.html')

@app.route('/dashboard/submittedform')
def submittedform():
    return render_template('submittedform.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/dashboard')
def dashboard():
    return render_template('createform.html')

if (__name__=="__main__"):
    app.run(debug=True)

    