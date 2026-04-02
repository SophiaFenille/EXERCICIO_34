import os

valor:int = 0
dir: str = '/tmp/exercicios'
arq: str = 'ex34.txt'

def mult(vlr,tab):
    res= vlr*tab
    return res

def grava(c, rslt):
    global dir, arq
    file = ''
    tipo = ''
    enc = 'utf-8'
    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):
        caminho = os.path.join(dir,arq)

        if os.path.exists(caminho) and c > 0:
            tipo = 'a'
        else:
            tipo = 'w'
        
        with open(caminho, tipo, encoding=enc) as f:
            f.write(linha)
def main():
    global valor

    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chmod(dir,0o744)
    contador = 0
    result = 0
    valor = int(input("Digite um valor entre 1 e 10:"))
   
    while contador < 10:
        result = mult(valor, contador)
        grava(contador,result)
        contador += 1
if __name__ == "__main__":
    main()

