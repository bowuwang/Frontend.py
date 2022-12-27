from flask import Flask,render_template

app = Flask(__name__)
#路由

import  datetime, time
tm = datetime.datetime.now()




@app.route('/')#要去访问的路径/
def login():#这边实现登陆的逻辑
        

    return render_template('login.html')

@app.route('/admin')
def admin():
    tmh=tm.hour
    timestr=time.strftime('%Y-%m-%d %H:%M:%S')
   
    return render_template('admin.html',th=tmh,tm=timestr)

@app.route('/bme') 
def bme(): 
        

    return render_template('bme.html')

@app.route('/setting')#要去访问的路径/
def setting():#这边实现登陆的逻辑
        

    return render_template('setting.html')



if __name__ =='__main__':
    app.run()

