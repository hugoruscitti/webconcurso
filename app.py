import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
