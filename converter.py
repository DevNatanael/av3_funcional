def converter_equacao_para_codigo():
    # Recebe a equação do usuário
    equacao = input("Digite a equação com símbolos matemáticos: ")
    
    # Substitui os símbolos matemáticos por operadores Python
    equacao_python = equacao.replace('^', '**').replace('log', 'math.log').replace('sin', 'math.sin').replace('cos', 'math.cos')
    
    # Substitui 'e' por 'math.e' para constantes matemáticas
    equacao_python = equacao_python.replace('e', 'math.e')
    
    # Substitui 'pi' por 'math.pi' para constantes matemáticas
    equacao_python = equacao_python.replace('pi', 'math.pi')
    
    # Substitui 'sqrt' por 'math.sqrt' para raízes quadradas
    equacao_python = equacao_python.replace('sqrt', 'math.sqrt')
    
    # Substitui 'ln' por 'math.log' para logaritmos naturais
    equacao_python = equacao_python.replace('ln', 'math.log')
    
    # Substitui 'exp' por 'math.exp' para exponenciação
    equacao_python = equacao_python.replace('exp', 'math.exp')
    
    # Substitui 'tan' por 'math.tan' para tangentes
    equacao_python = equacao_python.replace('tan', 'math.tan')
    
    # Substitui 'cot' por '1/math.tan' para cotangentes
    equacao_python = equacao_python.replace('cot', '1/math.tan')
    
    # Substitui 'sec' por '1/math.cos' para secantes
    equacao_python = equacao_python.replace('sec', '1/math.cos')
    
    # Substitui 'csc' por '1/math.sin' para cosecantes
    equacao_python = equacao_python.replace('csc', '1/math.sin')
    
    # Substitui 'arcsin' por 'math.asin' para arco seno
    equacao_python = equacao_python.replace('arcsin', 'math.asin')
    
    # Substitui 'arccos' por 'math.acos' para arco cosseno
    equacao_python = equacao_python.replace('arccos', 'math.acos')
    
    # Substitui 'arctan' por 'math.atan' para arco tangente
    equacao_python = equacao_python.replace('arctan', 'math.atan')
    
    # Substitui 'arccot' por 'math.atan' para arco cotangente
    equacao_python = equacao_python.replace('arccot', 'math.atan')
    
    # Substitui 'arcsec' por 'math.acos' para arco secante
    equacao_python = equacao_python.replace('arcsec', 'math.acos')
    
    # Substitui 'arccsc' por 'math.asin' para arco cosecante
    equacao_python = equacao_python.replace('arccsc', 'math.asin')
    
    # Substitui 'abs' por 'abs' para valores absolutos
    equacao_python = equacao_python.replace('abs', 'abs')
    
    # Substitui 'mod' por '%' para módulo
    equacao_python = equacao_python.replace('mod', '%')
    
    # Substitui 'floor' por 'math.floor' para arredondamento para baixo
    equacao_python = equacao_python.replace('floor', 'math.floor')
    
    # Substitui 'ceil' por 'math.ceil' para arredondamento para cima
    equacao_python = equacao_python.replace('ceil', 'math.ceil')
    
    # Substitui 'round' por 'round' para arredondamento
    equacao_python = equacao_python.replace('round', 'round')
    
    # Substitui 'int' por 'int' para conversão para inteiros
    equacao_python = equacao_python.replace('int', 'int')
    
    # Substitui 'frac' por '/' para frações
    equacao_python = equacao_python.replace('frac', '/')
    
    # Substitui 'div' por '/' para divisão
    equacao_python = equacao_python.replace('div', '/')
    
    # Substitui 'mul' por '*' para multiplicação
    equacao_python = equacao_python.replace('mul', '*')
    
    # Substitui 'add' por '+' para adição
    equacao_python = equacao_python.replace('add', '+')
    
    # Substitui 'sub' por '-' para subtração
    equacao_python = equacao_python.replace('sub', '-')
    
    # Substitui 'pow' por '**' para potência
    equacao_python = equacao_python.replace('pow', '**')
    
    # Substitui 'sqrt' por 'math.sqrt' para raízes quadradas
    equacao_python = equacao_python.replace('sqrt', 'math.sqrt')
    
    # Substitui 'ln' por 'math.log' para logaritmos naturais
    equacao_python = equacao_python.replace('ln', 'math.log')
    
    # Substitui 'exp' por 'math.exp' para exponenciação
    equacao_python = equacao_python.replace('exp', 'math.exp')
    
    # Substitui 'tan' por 'math.tan' para tangentes
    equacao_python = equacao_python.replace('tan', 'math.tan')
    
    # Substitui 'cot' por '1/math.tan' para cotangentes
    equacao_python = equacao_python.replace('cot', '1/math.tan')
    
    # Substitui 'sec' por '1/math.cos' para secantes
    equacao_python = equacao_python.replace('sec', '1/math.cos')
    
    # Substitui 'csc' por '1/math.sin' para cosecantes
    equacao_python = equacao_python.replace('csc', '1/math.sin')
    
    # Substitui 'arcsin' por 'math.asin' para arco seno
    equacao_python = equacao_python.replace('arcsin', 'math.asin')
    
    # Substitui 'arccos' por 'math.acos' para arco cosseno
    equacao_python = equacao_python.replace('arccos', 'math.acos')
    
    # Substitui 'arctan' por 'math.atan' para arco tangente
    equacao_python = equacao_python.replace('arctan', 'math.atan')
    
    # Substitui 'arccot' por 'math.atan' para arco cotangente
    equacao_python = equacao_python.replace('arccot', 'math.atan')
    
    # Substitui 'arcsec' por 'math.acos' para arco secante
    equacao_python = equacao_python.replace('arcsec', 'math.acos')
    
    # Substitui 'arccsc' por 'math.asin' para arco cosecante
    equacao_python = equacao_python.replace('arccsc', 'math.asin')
    
    # Substitui 'abs' por 'abs' para valores absolutos
    equacao_python = equacao_python.replace('abs', 'abs')
    
    # Substitui 'mod' por '%' para módulo
    equacao_python = equacao_python.replace('mod', '%')
    
    # Substitui 'floor' por 'math.floor' para arredondamento para baixo
    equacao_python = equacao_python.replace('floor', 'math.floor')
    
    # Substitui 'ceil' por 'math.ceil' para arredondamento para cima
    equacao_python = equacao_python.replace('ceil', 'math.ceil')
    
    # Substitui 'round' por 'round' para arredondamento
    equacao_python = equacao_python.replace('round', 'round')
    
    # Substitui 'int' por 'int' para conversão para inteiros
    equacao_python = equacao_python.replace('int', 'int')
    
    # Substitui 'frac' por '/' para frações
    equacao_python = equacao_python.replace('frac', '/')
    
    # Substitui 'div' por '/' para divisão
    equacao_python = equacao_python.replace('div', '/')
    
    # Substitui 'mul' por '*' para multiplicação
    equacao_python = equacao_python.replace('mul', '*')
    
    # Substitui 'add' por '+' para adição
    equacao_python = equacao_python.replace('add', '+')
    
    # Substitui 'sub' por '-' para subtração
    equacao_python = equacao_python.replace('sub', '-')
    
    # Substitui 'pow' por '**' para potência
    equacao_python = equacao_python.replace('pow', '**')
    
    # Substitui 'sqrt' por 'math.sqrt' para raízes quadradas
    equacao_python = equacao_python.replace('sqrt', 'math.sqrt')
    
    # Substitui 'ln' por 'math.log' para logaritmos naturais
    equacao_python = equacao_python.replace('ln', 'math.log')
    
    # Substitui 'exp' por 'math.exp' para exponenciação
    equacao_python = equacao_python.replace('exp', 'math.exp')
    
    # Substitui 'tan' por 'math.tan' para tangentes
    equacao_python = equacao_python.replace('tan', 'math.tan')
    
    # Substitui 'cot' por '1/math.tan' para cotangentes
    equacao_python = equacao_python.replace('cot', '1/math.tan')
    
    # Substitui 'sec' por '1/math.cos' para secantes
    equacao_python = equacao_python.replace('sec', '1/math.cos')