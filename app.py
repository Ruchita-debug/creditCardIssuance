from flask import (Flask, render_template, request) # import package
import logging as logger
from api_call import inference_call

logger.basicConfig(level="DEBUG")
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
@app.route("/login.html", methods=['POST','GET'])
def welcome():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        email = str(request.form.get("email"))
        password = str(request.form.get("password"))
        if email == 'admin@creditpro.com' and password == 'admin':
            return render_template('index.html')
        else:
            return render_template('login.html')

@app.route("/index.html") 
def index():
    return render_template('index.html')

@app.route("/form.html", methods=['POST','GET'])
def predict():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        car = int(request.form.get("cars"))
        home = int(request.form.get("home"))
        cntChild = int(request.form.get("cntChild"))
        IncomeType = int(request.form.get("IncomeType"))
        educationType = int(request.form.get("educationType"))
        income = int(request.form.get("income"))
        familyStatus = int(request.form.get("familyStatus"))
        cntMem = int(request.form.get("cntMem"))
        housingType = int(request.form.get("housingType"))
        age = int(request.form.get("age"))
        gender = int(request.form.get("gender"))
        yearsEmployed = int(request.form.get("yearsEmployed"))

        # print("car " ,car,"\nhome ", home,"\ncntChild ", cntChild,"\nIncomeType ", IncomeType)
        # print("\neducationType ", educationType, "\nincome ", income, "\nfamilyStatus ", familyStatus)
        # print("\ncntMem ", cntMem, "\nhousingType ", housingType, "\nage ", age)
        # print("\ngender ", gender, "\nyearsEmployed ", type(yearsEmployed))

        data = [0, car, home, cntChild, IncomeType, educationType, income, familyStatus, cntMem, housingType, age, gender, yearsEmployed]
        msg = inference_call(data)
        print(msg)
        return render_template('form.html', msg=msg, income=(income/12), IncomeType=IncomeType)
    elif request.method == "GET":
        return render_template('form.html')

app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)