import os
from flask import Flask,render_template,url_for,redirect

#configuring app
app = Flask(__name__)

port = int(os.environ.get("PORT",5000))
#routing view function
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/code-snippets')
def codesnippets():
	return render_template('codesnippets.html')
	
#Running Server
if __name__ == "__main__":
        app.debug = False
        app.use_reloader=True
        app.run(host='0.0.0.0',port = port)