from flask import Flask,render_template


app=Flask(__name__)

@app.route("/")
def hello_world():
   return "hello in my programing world"

@app.route("/login")
def login_page():
   return render_template("login.html")



@app.route("/index")
def index_page():
   dict = {'phy': 50, 'che': 60, 'maths': 70 }
   return render_template("index.html",name="Umesh",di=dict)

@app.route("/scr")
def script_page():
   return render_template("first.html")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
