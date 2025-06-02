import json
from flask import Flask,request
def init():
    with open('words.json') as f:
        data = json.load(f)
    return data

def play(word,d):
    #assuming d is present and loaded
    #a is short for alphabet
    try:
        word=word.lower()
        if (d[word[0]]) and (word in d[word[0]]):
            wd=d[word[-1]].pop(0)
            return {"stat":"OK","word":wd}
        else:
            return {"stat":"NOT OK"}
    except:
        return {"stat":"NOT OK"}
app=Flask(__name__)

@app.route('/play',methods=["POST"])
def wb():
    data=request.get_json()
    re=play(data['word'],d)
    if re['stat']=='OK':
        return re,200
    else:
        return re,420
    

if __name__ == '__main__':
    global d
    d=init()
    app.run()

