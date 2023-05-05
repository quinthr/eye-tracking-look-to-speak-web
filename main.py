from flask import Flask, render_template, request, session, redirect
import numpy as np
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lookToSpeakWeb'
app.config['SESSION_COOKIE_NAME'] ='lookToSpeakWeb'
app.secret_key = 'lookToSpeakWeb'
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(401)
def unauthorized_page(e):
    return redirect('/')

@app.errorhandler(500)
def internal_app_error(e):
    return redirect('/')


app.register_error_handler(404, page_not_found)
app.register_error_handler(401, unauthorized_page)
app.register_error_handler(500, internal_app_error)

words = [
        "Hello",
        "Thank you",
        "Great",
        "Okay",
        "What's your name?",
        "How are you?",
        "Can you repeat that?",
        "What's going on?",
        "Yes",
        "No",
        "Maybe",
        "Please",
        "I need some help please",
        "TV please",
        "Music please",
        "Water please"
        ]

@app.route('/')
def index():
    session.clear()
    range1 = int(len(words)/4)
    range2 = int(len(words)/2)
    range3 = int(range2+range1)
    return render_template('index.html', error=None, words=words, range1=range1,range2=range2, range3=range3)

@app.route('/step1/<column>')
def step1(column):
    if column is None:
        return redirect('/')
    arr = np.array(words)
    half = int(len(words) / 2)
    if int(column) == 1:
        newWords = arr[0:half]
    elif int(column) == 2:
        newWords = arr[half:]
    else:
        return redirect('/')
    session['words'] = newWords
    range1 = int(len(newWords) / 4)
    range2 = int(len(newWords) / 2)
    range3 = int(range2 + range1)
    return render_template('step1.html', error=None, words=newWords, range1=range1,range2=range2, range3=range3)

@app.route('/step2/<column>')
def step2(column):
    if column is None:
        return redirect('/')
    if session.get('words') is None:
        return redirect('/')
    oldWords = session['words']
    if len(oldWords) != 8:
        return redirect('/')
    print(len(oldWords))
    arr = np.array(oldWords)
    half = int(len(oldWords) / 2)
    if int(column) == 1:
        newWords = arr[0:half]
    elif int(column) == 2:
        newWords = arr[half:]
    else:
        return redirect('/')
    session['words'] = newWords
    range1 = int(len(newWords) / 4)
    range2 = int(len(newWords) / 2)
    range3 = int(range2 + range1)
    return render_template('step2.html', error=None, words=newWords, range1=range1,range2=range2, range3=range3)

@app.route('/step3/<column>')
def step3(column):
    print(session.get('words'))
    if session.get('words') is None:
        return redirect('/')
    oldWords = session['words']
    if len(oldWords) != 4:
        return redirect('/')
    arr = np.array(oldWords)
    half = int(len(oldWords) / 2)
    if int(column) == 1:
        newWords = arr[0:half]
    elif int(column) == 2:
        newWords = arr[half:]
    else:
        return redirect('/')
    session['words'] = newWords
    range = int(len(newWords) / 2)
    return render_template('step3.html', error=None, words=newWords, range=range)

@app.route('/step4')
def step4():
    if session.get('words') is None:
        return redirect('/')
    oldWords = session['words']
    word = request.args.get('word')
    if len(oldWords) != 2:
        return redirect('/')
    if word not in oldWords:
        return redirect('/')
    if word is None:
        return redirect('/')
    session.clear()
    return render_template('step4.html', error=None, word=word)

if __name__=='__main__':
    app.run(host='localhost', port=8080, debug=True)