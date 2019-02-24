from flask import Flask, render_template, redirect, url_for,request
import psutil
import datetime
import water
import os
import cgi
import subprocess
import pandas as pd
app = Flask(__name__)

Moist_Hist = pd.DataFrame(columns=['DateTime','Status'])

def template(title = "AutoWatering System", text = "",Moist_Hist = pd.DataFrame()):
    now = datetime.datetime.now()
    timeString = now
    templateDate = {
        'title' : title,
        'time' : timeString,
        'text' : text,
        'Moist_Hist': Moist_Hist,
        'tables': [Moist_Hist.to_html(classes='data')],
        'titles': Moist_Hist.columns.values
        }
    return templateDate

@app.route("/")
def hello(Moist_Hist = pd.DataFrame()):
    templateData = template(Moist_Hist=Moist_Hist)
    return render_template('main.html', **templateData)

@app.route("/last_watered")
def check_last_watered(Moist_Hist = pd.DataFrame()):
    templateData = template(text = water.get_last_watered(), Moist_Hist=Moist_Hist)
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action(Moist_Hist = pd.DataFrame()):
    status = water.get_status()
    message = ""
    if (status == 0):
        message = "Water me please!"
    else:
        message = "I'm a happy plant"

    templateData = template(text = message, Moist_Hist=Moist_Hist)
    return render_template('main.html', **templateData)

@app.route("/water/<toggle>")
def action2(toggle,Moist_Hist = pd.DataFrame()):
    delay = int(toggle)
    water.pump_on(7,delay*60)
    templateData = template(text = "Watered Once", Moist_Hist=Moist_Hist)
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_water(toggle,Moist_Hist = pd.DataFrame()):
    running = False
    if toggle == "ON":
        templateData = template(text = "Auto Watering On", Moist_Hist=Moist_Hist)
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templateData = template(text = "Already running", Moist_Hist=Moist_Hist)
                    running = True
            except:
                pass
        if not running:
            auto_proc = subprocess.Popen(["python3","auto_water.py"])
    else:
        templateData = template(text = "Auto Watering Off", Moist_Hist=Moist_Hist)
        os.system("pkill -f water.py")

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
