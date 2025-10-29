from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact-process', methods=['POST'])
def contact_process():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    return render_template('result.html', name=name, email=email, mobile=mobile)

if __name__ == '__main__':
    app.run(debug=True)
