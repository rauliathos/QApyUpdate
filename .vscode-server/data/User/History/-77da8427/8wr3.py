from flask import Flask

app = Flask(__name__)


@app.route('/home/<int:Number>')
def home(number):
    return number*number
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)