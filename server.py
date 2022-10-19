from turtle import clear
from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key ='1234'

@app.route('/')
def index():
    if 'clicks' not in session:
        session['clicks'] = 0
    else:
        session['clicks'] += 1
    return render_template("index.html")
    
@app.route('/plus_2')
def plus_2():
    session['clicks'] += 1
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
