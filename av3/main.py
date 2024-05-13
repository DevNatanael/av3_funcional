from flask import Flask, render_template, request

app = Flask(__name__)

# Função para calcular a integral indefinida numericamente usando o método do trapézio
def integral(f, a, b, n=1000):
    h = (b - a) / n
    integral_value = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral_value += f(a + i * h)
    integral_value *= h
    return integral_value

@app.route('/', methods=['GET', 'POST'])
def calcular_integral():
    if request.method == 'POST':
        # Recebendo a expressão da função do formulário
        expressao = request.form['expressao']
        # Definindo a função original com base na expressão inserida
        f = lambda x: eval(expressao)
        # Recebendo os limites de integração do formulário
        limite_inferior = float(request.form['limite_inferior'])
        limite_superior = float(request.form['limite_superior'])
        # Calculando a integral indefinida numericamente
        resultado = integral(f, limite_inferior, limite_superior)
        resultado_formatado = "{:.2f}".format(resultado)
        return render_template('formulario.html', resultado=resultado_formatado)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
