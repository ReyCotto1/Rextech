from flask import Flask, render_template, request


app = Flask(__name__)
env = "prod"


@app.route('/')
def about_me():
    return render_template('about.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/experiences')
def work():
    return render_template('experiences.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text


if env == "dev":
    app.run()
