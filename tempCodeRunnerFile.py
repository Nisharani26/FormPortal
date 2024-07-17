from flask import Flask,render_template,request,session,redirect 
import sqlite3


database_connection = sqlite3.connect('database.db',check_same_thread=False)
#cursor is used to execute statements
database_cursor=database_connection.cursor()

app=Flask(__name__)
app.secret_key="nisharani"

@app.route('/')
def home():
    if "username" in session:
        return render_template('index.html')
    else:
        return redirect('/login')

@app.route('/login')
def login():
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

@app.route('/loginsubmission',methods=["POST","GET"])
def loginsubmission():
    # username=request.form["username"]
    # password=request.form["password"]
    # # data=database_cursor.execute("Select password,username from user where username=?",(username)).fetchone()
    # data = database_cursor.execute("SELECT password, username FROM USER WHERE username = ?",(username,)).fetchone()
    # if request.method=="POST":
    #     if (data == None and password == data[0]):
    #         print(data[0])
    #         print(password)
    #         session["username"]=username
    #         print(session["username"])
    #         return redirect('/')
    #     else:
    #         print(data[0])
    #         print(password)
    #         return "Invalid Username and password"
    # else:
    #     return render_template('login.html')
    # if (data == None and password == data[0]):
    #     # print(data[0])
    #     # print(password)
    #     # session["username"]=username
    #     # print(session["username"])
    #     # return redirect('/')
    #     print(data[0])
    #     print(password)
    #     return "Invalid Username and password"
    # else:
    #     print(data[0])
    #     print(password)
    #     session["username"]=username
    #     print(session["username"])
    #     return redirect('/')
        
        if data:
    stored_password = data[0]  # Password retrieved from the database
    print(f"Stored Password: {stored_password}")
    print(f"Input Password: {password}")
    if password == stored_password:
        session['username'] = username  # Store username in session
        return redirect('/')
    else:
        return "Invalid password"
else:
    return "Invalid username"
        
    # print(data[0])
    # print(data[1])
    # if password == data[0]:
    #     print()
    #     return "ok"
    # else:
    #     return "invalid"

    # if request.method=="POST":
    #      if session["username"] == username:
    #          return redirect('/')
    #      else:
    #          return "Invalid Username and password"
    # else:
    #     return render_template('login.html')
    
    # if password == data[0]:
    #     session["username"]=username
    #     return redirect('/')
    # else:
    #     return "Invalid Username and password"    

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

    