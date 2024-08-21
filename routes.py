from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Generative AI Application Areas')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='GenAI for Text')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='GenAI for Images')

if __name__ == '__main__':
    app.run(debug=True)
