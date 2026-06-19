# menu de opções
print("Calculadora equação geral da reta.")
opcoes = input("Informe os dados disponíveis na ordem x, y e m: ").split()
if len(opcoes) < 3:
    print("Entrada inválida. Use três valores: x y m")
    exit(1)

x = float(opcoes[0])
y = float(opcoes[1])
m = float(opcoes[2])
#formulas
def pontos(m,x,y):
    #y - 1y = m (1x-x)
    b = (m*x)-y
    return b
b = pontos(m,x,y)

print(f"A equação geral da reta é: {m}x - y + {b} = 0")
