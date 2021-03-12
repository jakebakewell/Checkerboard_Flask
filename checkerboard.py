from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows = 8, columns = 8, color0 = "black", color1 = "red")

@app.route('/<y>')
def specify_num_rows(y):
    return render_template('index.html', rows = int(y), columns = 8, color0 = "black", color1 = "red")

@app.route('/<y>/<x>')
def specify_num_rows_columns(y, x):
    return render_template('index.html', rows =  int(y), columns = int(x), color0 = "black", color1 = "red")

@app.route('/<y>/<x>/<color0>')
def specify_checkerboard_color(y, x, color0):
    return render_template('index.html', rows =  int(y), columns = int(x), color0 = color0, color1 = "red")

@app.route('/<y>/<x>/<color0>/<color1>')
def specify_checkerboard_traits(y, x, color0, color1):
    return render_template('index.html', rows =  int(y), columns = int(x), color0 = color0, color1 = color1)

if __name__ == '__main__':
    app.run(debug=True)