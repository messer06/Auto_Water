from flask import render_template
import psutil
import datetime
from app.waterer import water
from app.waterer.models import MoistHist, WaterHist
import os
import subprocess
from flask import current_app as app


def template(title="AutoWatering System", text=""):
    now = datetime.datetime.now()
    timestring = now
    templatedata = {
        'title': title,
        'time': timestring,
        'text': text
    }
    return templatedata


@app.route("/")
def hello():
    templatedata = template()
    return render_template('main.html', **templatedata)


@app.route("/last_watered")
def check_last_watered():
    templatedata = template(
        text=(WaterHist.query.order_by(WaterHist.eventtime.desc()).with_entities(WaterHist.eventtime).first())[
            0].strftime("%d-%b-%y %H:%M:%S"))
    return render_template('main.html', **templatedata)


@app.route("/sensor")
def action():
    status = water.get_status()
    moist_event = MoistHist(eventtime=datetime.datetime.now(), status=status)
    app.db.session.add(moist_event)
    app.db.session.commit()
    message = ""
    if status == 0:
        message = "Water me please!"
    else:
        message = "I'm a happy plant"

    templatedata = template(text=message)
    return render_template('main.html', **templatedata)


@app.route("/water/<toggle>")
def action2(toggle):
    delay = int(toggle)
    water.pump_on(7, delay * 60)
    water_event = WaterHist(eventtime=datetime.datetime.now(), duration=delay * 60)
    app.db.session.add(water_event)
    app.db.session.commit()
    templatedata = template(text="Watered Once")
    return render_template('main.html', **templatedata)


@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        templatedata = template(text="Auto Watering On")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templatedata = template(text="Already running")
                    running = True
            except:
                pass
        if not running:
            subprocess.Popen(["python3", "auto_water.py"])
    else:
        templatedata = template(text="Auto Watering Off")
        os.system("pkill -f water.py")

    return render_template('main.html', **templatedata)
