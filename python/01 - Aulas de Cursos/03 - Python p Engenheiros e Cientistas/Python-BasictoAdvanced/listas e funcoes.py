# Conjunto de dados de diferentes tipos, começar c colchetes [ ]
# Valores indexados a partir do 0 

lista_a = [7, 1, 3, 5, 'oie']

# Para chamar umunico elemento da lista, vamos bucas pelo index
print(lista_a[0])
print(len(lista_a))

# String x Lista
lista_2 = ['C','o','p','o']
string_2 = 'Copo'

print(lista_2[:1])
print(string_2[:2])

def minha_funcao(Nome):
    print(f'Meu nome é {Nome}')

meu_nome = "raul"
minha_funcao(meu_nome)

def multiplica_numero_por_100(a):
    resultado = a*100
    return resultado

n1 = 4

print(multiplica_numero_por_100(n1))