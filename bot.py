from flask import Flask
from flask import render_template,request
import RPi.GPIO as GPIO
import time

app=Flask(__name__)
m9= 9
m10= 10
m8= 8
m7= 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m9,GPIO.OUT)
GPIO.setup(m10,GPIO.OUT)
GPIO.setup(m8,GPIO.OUT)
GPIO.setup(m7,GPIO.OUT)
GPIO.output(m9,0)
GPIO.output(m10,0)
GPIO.output(m8,0)
GPIO.output(m7,0)
print ('Done')
a=1
@app.route("/")
def index():
	return render_template('Surve.html')

@app.route('/up_side')
def up_side():
    data1= 'FORWARD'
    GPIO.output(m9,1)
    GPIO.output(m10,0)
    GPIO.output(m8,1)
    GPIO.output(m7,0)
    return 'true'

@app.route('/down_side')
def down_side():
    data1= 'REVERSE'
    GPIO.output(m9,0)
    GPIO.output(m10,1)
    GPIO.output(m8,0)
    GPIO.output(m7,1)
    return 'true'

@app.route('/left_side')
def left_side():
    data1= 'LEFT'
    GPIO.output(m9,0)
    GPIO.output(m10,0)
    GPIO.output(m8,1)
    GPIO.output(m7,0)
    return 'true'

@app.route('/right_side')
def right_side():
    data1= 'RIGHT'
    GPIO.output(m9,1)
    GPIO.output(m10,0)
    GPIO.output(m8,0)
    GPIO.output(m7,0)
    return 'true'

@app.route('/stop')
def stop():
    data1= 'STOP'
    GPIO.output(m9,0)
    GPIO.output(m10,0)
    GPIO.output(m8,0)
    GPIO.output(m7,0)
    return 'true'

if __name__ == '__main__':
    print ('Start')
    app.run(host='192.168.8.100',port=5010)
