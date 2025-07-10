from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/product1')
def product1():
    return render_template("product1.html")

@app.route('/product2')
def product2():
    return render_template("product2.html")

@app.route('/product3')
def product2():
    return render_template("product3.html")

@app.route('/product4')
def product2():
    return render_template("product4.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
