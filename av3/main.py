import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Função lambda de alta ordem que aplica uma transformação a cada termo
apply_transformation = lambda terms, transform: [transform(term) for term in terms]

# Função lambda recursiva para validar a expressão
validate_term = lambda term: (
    validate_term_polynomial(term) or
    validate_term_trig(term) or
    validate_term_constant(term) or
    validate_term_division(term)
)

validate_expression = lambda terms: all(validate_term(term) for term in terms)

# Funções auxiliares para validação de termos específicos
validate_term_polynomial = lambda term: re.match(r'^\d*\*?x\*\*\d+$', term) or re.match(r'^x\*\*\d+$', term)
validate_term_trig = lambda term: re.match(r'^(sin|cos|tan|cot|sec|csc)\(x\)$', term)
validate_term_constant = lambda term: re.match(r'^\d+$', term)
validate_term_division = lambda term: '/' in term and (re.match(r'^\d+/\d*\*?x\*\*\d+$', term) or re.match(r'^\d+/x$', term))

# Funções lambda com currying para processamento da expressão
curry_add = lambda x: (lambda y: x + y)
curry_multiply = lambda x: (lambda y: x * y)
curry_process_term = lambda func: (lambda term: func(term))

def integral(expression):
    # Remover espaços em branco
    expression = expression.replace(" ", "")

    # Separar a função e a variável de integração
    if "dx" in expression:
        func = expression.split("dx")[0]
    else:
        raise ValueError("A expressão deve conter 'dx' como variável de integração.")

    # Verificar se a função está no formato correto
    if not func.startswith("f(x)="):
        raise ValueError("A expressão deve começar com 'f(x)='.")

    func = func[5:]  # Remover 'f(x)='

    # Dividir a função em termos
    terms = re.split(r'(?=[+-])', func)

    # Validar a expressão usando a função lambda recursiva
    if not validate_expression(terms):
        raise ValueError("A expressão contém termos inválidos.")

    # Inicializar a resposta
    result = ""

    # Definir a transformação de exemplo: aqui não faremos nenhuma transformação real
    # mas podemos mostrar como seria usada
    transform = lambda term: term  # Transformação de identidade (não altera o termo)

    # Aplicar a transformação a cada termo usando a função lambda de alta ordem
    transformed_terms = apply_transformation(terms, transform)

    # Aplicar currying para processar os termos
    process = curry_process_term(transform)
    processed_terms = [process(term.strip()) for term in transformed_terms]

    for term in processed_terms:
        term = term.strip()

        # Verificar se o termo contém uma divisão (ex: 1/x**3)
        if '/' in term:
            num, denom = term.split('/')
            if denom.startswith("x**"):
                power = int(denom[3:])
                new_power = power - 1
                coeff = -float(num) / new_power
                result += f"{coeff:+}/x**{new_power}"
            elif denom == "x":
                result += f"+{num}*ln(x)"
            else:
                raise ValueError("Formato de termo não suportado.")
        # Verificar se o termo é uma potência de x (ex: x**3)
        elif term.startswith("x**"):
            power = int(term[3:])
            new_power = power + 1
            result += f"+1/{new_power}*x**{new_power}"
        # Verificar se o termo é um termo polinomial (ex: 3*x**2 ou x**2)
        elif re.match(r'^\d*\*?x\*\*\d+$', term):
            match = re.match(r'^(\d*)\*?x\*\*(\d+)$', term)
            if match.group(1) == '':
                coeff = 1
            else:
                coeff = int(match.group(1))
            power = int(match.group(2))
            new_power = power + 1
            coeff = float(coeff) / new_power
            result += f"{coeff:+}*x**{new_power}"
        # Verificar se o termo é uma função trigonométrica
        elif term.startswith("sin(x)"):
            result += "-cos(x)"
        elif term.startswith("cos(x)"):
            result += "sin(x)"
        elif term.startswith("tan(x)"):
            result += "-ln|cos(x)|"
        elif term.startswith("cot(x)"):
            result += "ln|sin(x)|"
        elif term.startswith("sec(x)"):
            result += "ln|sec(x)+tan(x)|"
        elif term.startswith("csc(x)"):
            result += "-ln|csc(x)+cot(x)|"
        # Verificar se o termo é uma constante
        elif re.match(r'^\d+$', term):
            result += f"+{term}*x"
        else:
            raise ValueError("Formato de termo não suportado.")

    # Adicionar a constante de integração
    result += " + C"

    # Corrigir possíveis sinais no início da expressão
    if result[0] == '+':
        result = result[1:]

    return result

@app.route('/', methods=['GET', 'POST'])
def calcular_integral():
    if request.method == 'POST':
        # Recebendo a expressão da função do formulário
        expressao = request.form['expressao']
        modelo = "f(x)="+expressao+"dx"
        try:
            resultado = integral(modelo)
        except ValueError as e:
            resultado = str(e)
        return render_template('formulario.html', resultado=resultado)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
