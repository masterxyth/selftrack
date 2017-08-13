
import time
from dbq import DBQ


from flask import Flask, render_template, request
app = Flask(__name__)

DB = DBQ()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET'])
def submit():
    type = request.args.get('exercise')
    timenote = time.strftime('%Y-%m-%d %H:%M:%S')
    reps = request.args.get('reps')
    sets = request.args.get('sets')
    unit = request.args.get('unit')
    weight = request.args.get('weight')
    DB.create_exercise(type,timenote ,int(reps),int(sets),int(weight),unit)
    return render_template('done.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
