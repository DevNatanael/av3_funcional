import re

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

    # Inicializar a resposta
    result = ""

    # Dividir a função em termos
    terms = re.split(r'(?=[+-])', func)

    for term in terms:
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

# Exemplos de uso
expressao1 = "f(x)=x**2dx"
print(integral(expressao1))  # Esperado: 0.5*x**4 + C

