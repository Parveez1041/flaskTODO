from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/aboutus')
def About_us():
    return 'This is about us page!'

@app.route('/contactus')
def Contact_Us():
    return 'This is contact us page'

if __name__== "__main__":
    app.run(debug = True)

