import json
from flask import Flask,request,render_template,send_from_directory
import random
from mail import send_email
import os


def init():
    with open('words.json') as f:
        data = json.load(f)
    global used_words
    used_words=[]
    return data

def play(word,d):
    #assuming d is present and loaded
    #a is short for alphabet
    try:
        word=word.lower().strip()
        if ((d[word[0]]) and (word in d[word[0]])) and (word not in used_words):
            if len(used_words)>0 and used_words[-1][-1]!=word[0]:
                return {"stat":"UR"}
            used_words.append(word)
            ri=random.randint(0,len(d[word[-1]])-1)
            wd=d[word[-1]].pop(ri)
            used_words.append(wd)
            return {"stat":"OK","word":wd}
        else:
            return {"stat":"NOT OK"}
    except:
        return {"stat":"NOT OK"}
app=Flask(__name__,template_folder='Templates')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    global d
    d=init()
    return render_template('index.html')

@app.route("/play",methods=["POST"])
def wb():
    data=request.get_json()
    re=play(data['word'],d)
    if re['stat']=='OK':
        return re,200
    elif re['stat']=='UR':
        return re,203
    else:
        return re,220

@app.route("/report",methods=["POST"])
def rep():
    data=request.get_json()
    wd=data['word']
    if len(wd)<3 or wd in d[wd[0]]:
        return {"Message":"NOT OK"},265
    else:
        send_email(data['word'])
        return {"Message":"Success"},200
    
if __name__ == '__main__':
    global d
    d=init()
    app.run()

