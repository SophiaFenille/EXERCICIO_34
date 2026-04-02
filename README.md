Baseado no Ex. 34, fazer:
a. Criar no Linux a pasta /tmp/exercicios
i. Assegurar que ela tem permissão 744 (Fazer em Python)
b. Declarar como globais, as variáveis:
i. valor: int = 0
ii. dir: str = ‘’
iii. arq: str = ‘’
iv. arq: str = ‘’
c. Um procedimento main() que use valor como global e inicie uma variável contador
e uma variável result, locais, peça ao usuário um valor entre 1 e 10 e chame 10 vezes
a função mult(vlr, tab), passando o valor e o contador como parâmetros. O retorno
da função deve ser retornado para a variável result. Por fim, ainda dentro da
estrutura de repetição, deve-se chamar o procedimento grava(c, rslt), passando o
contador e o result como parâmetros;
d. A função mult deve receber o valor passado pelo usuário e o contador, deve
declarar uma variável local res, que recebe a multiplicação de vlr e tab e é a variável
de retorno da função;
e. O procedimento grava recebe como parâmetros o contador da estrutura de
repetição e o resultado da multiplicação. Utilizando dir e arq como globais, que
devem ter dir = ‘/tmp/exercicios’ e arq = ‘ex34.txt’, deve declarar file, tipo, enc e linha
como str vazios. A variável linha deve receber o cast da variável rslt (str(rslt))
concatenado com uma quebra de linha (‘\n’). Criar, baseado no material de aula,
deve-se verificar se o diretório existe e é diretório e, em sendo verdadeiro, verificar
se o arquivo existe (Para definir se o tipo da operação será w (write) ou a (append)),
mas só pode mudar o tipo para ‘a’, se c for maior que 0. Gravar a linha no arquivo.
