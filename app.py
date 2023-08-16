from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def converter():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        c = CurrencyRates()
        converted_amount = c.convert(from_currency, to_currency, amount)

        return render_template('result.html', amount=amount, from_currency=from_currency,
                               to_currency=to_currency, converted_amount=converted_amount)

    return render_template('converter.html')


if __name__ == '__main__':
    app.run(debug=True)
