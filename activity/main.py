from flask import Flask, request, render_template

app = Flask(__name__)

# pages
@app.route('/')
def introduction():
    return render_template('introduction.html')

@app.route('/activity1')
def activity1():
    return render_template('activity1.html')

@app.route('/activity2')
def activity2():
    return render_template('activity2.html')

@app.route('/resources1')
def resources1():
    return render_template('resources1.html')

@app.route('/resources2')
def resources2():
    return render_template('resources2.html')

@app.route('/final')
def final():
    return render_template('final.html')


if __name__ == '__main__':
    app.run(port=5050, debug=True)