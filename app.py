from flask import Flask,render_template,redirect
from forms import LoginForm

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

@app.route('/',methods=['GET','POST'])
def login():
    return "<h1>running workflow</h1>"

 
if __name__ == "__main__":
    app.run(host="0.0.0.0")
