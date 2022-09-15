from flask import Flask,render_template
from flask import request

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='ops_digital_asset'
)

@app.route('/',methods=['GET','POST'])
def index():
    user={"name":"Ajay"}
    return render_template("index.html",user=user)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.values['email']=="admin@gmail.com" and request.values['pwd']=="admin":
        return render_template("dashboard.html")
    else:
        return "<h1>Invalid User!</h1>"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")
