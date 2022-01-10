from flask import (
     Flask ,
     render_template ,
     request ,
     redirect ,
     g
)

app = Flask(__name__)

@app.route('/')     
def index():
     return render_template('index.html')

@app.route('/money/' , methods=["POST" , "GET"])
def money():
     money = str(request.form['money'])
     all = 7
     person = money / all
     unit1 = person * 3
     unit2 = person * 4

     return "Unit 1 Must Pay :" , unit1
     return "Unit 2 Must Pay :" , unit2


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
