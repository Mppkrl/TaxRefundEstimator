from flask import Flask, render_template, request
from tax_calculator import Tax_calculator
app = Flask(__name__)

@app.route("/")

def home():
    return render_template("form.html")

@app.route('/result', methods=['POST'])

def result():
    try:
        gross_income = float(request.form['income'])
        tax_withheld = float(request.form['withheld'])

        calc = Tax_calculator(gross_income, tax_withheld)
        result_data = calc.summary()

        return render_template('result.html', result=result_data)

    except ValueError:
        error = "Please enter valid numbers only."
        return render_template('form.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)