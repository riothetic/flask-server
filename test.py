#test program to play around with flask (http-server)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
#   return 'hello worlds'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
