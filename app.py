

# step 1-
from dotenv import load_dotenv

#step 2-
load_dotenv()

# step 3-
import os
key=os.getenv('gemini_api_key')



# run in terminal - pip install -U google-genai
from google import genai
from flask import Flask, render_template,request

app = Flask(__name__)
client = genai.Client(api_key=key)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')

    elif request.method=='POST':
        name=request.form['name']
        age=int(request.form['age'])
        height=float(request.form['height'])
        weight=float(request.form['weight'])
        bmi=float(request.form['bmi'])
        target=request.form['target']
        time=int(request.form['time'])
        meal=request.form['meal']
        plan_type=request.form['plan_type']

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=f"hello my name is {name}, i am {age} year old. My current height is {height} cm and "
                  f"weight is {weight}Kg. My BMI is {bmi}. I want to {target} i am doing workout for {time}min"
                  f"create a diet plan for me according to the provided data i want only {meal}"
                  f"generate a {plan_type} for me. make sure all the result in html format apply css to it and"
                  f"give the output to me."
        )

        return render_template('result.html',result=interaction.output_text)

# app.run(debug=True)