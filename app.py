from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('homepage.html')
@app.route('/About')
def About():
    return render_template('About.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')
app.run(debug=False,host='0.0.0.0')
