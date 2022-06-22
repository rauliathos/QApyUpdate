from flask import Flask, request

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)