from flask import Flask

app = Flask(__name__)


@app.route('/square/<int:number>')
def square(number):
    result = number*number
    return str(result)
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)