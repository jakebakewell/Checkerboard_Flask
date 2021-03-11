from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows = 8, columns = 8, color0 = "black", color1 = "red")

@app.route('/<x>')
def specify_num_rows(x):
    return render_template('index.html', rows = int(x), columns = 8, color0 = "black", color1 = "red")

@app.route('/<x>/<y>')
def specify_num_rows_columns(x, y):
    return render_template('index.html', rows =  int(x), columns = int(y), color0 = "black", color1 = "red")

@app.route('/<x>/<y>/<color0>/<color1>')
def specify_checkerboard_traits(x, y, color0, color1):
    return render_template('index.html', rows =  int(x), columns = int(y), color0 = color0, color1 = color1)

if __name__ == '__main__':
    app.run(debug=True)