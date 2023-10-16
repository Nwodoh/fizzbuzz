from flask import Flask, render_template
app = Flask(__name__)

@app.route('/fizzbuzz')
def hello_world():
    return render_template('/fizzbuzz.html')

print(not 0 and not 0)