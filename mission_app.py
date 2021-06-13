from flask import Flask, render_template

from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('missionrequest.html')


@app.route('/login', methods=['post'])
def login():

   
    print("-----", request.form.get('id'))


    id = request.form.get('id')

    
   
    return render_template('missionresponse.html', idencore = '회원가입을 진심으로 축하드립니다!!')


if __name__=='__main__':
    app.run(debug=True)