def iniciar(n):
	"""
	Fazer a leitura da matriz
	"""
	print "Digite apenas 0's ou 1's para preencher a matriz"
	print "Digite apenas 1 numero por linha"
	entrada = []
	for i in range(3):
		linha = []
		for j in range(3):
			# print ()
			sim = 0
			while sim == False:
				# print sim
				try:
					print "Digite o valor a"+str(i+1) + str(j+1)+" da matriz " + str(n)
					valor = input()
					if(int(valor)==0 or int(valor) == 1):
						# print "Fim"
						sim = 1
						# print sim
					else:
						print "Numero nao permitido, digite apenas 0's ou 1's"	
				except Exception, e:
					print "Caracter nao permitido, digite apenas 0's ou 1's"
			linha.append(valor)
			# print linha
		entrada.append(linha)
	print imprimir(entrada)
	return entrada

def GF(m1,m2):
	"""
	Fazer o GF entre as duas matrizes
	"""
	matriz = []
	for i in range(len(m1)):
		l1 = m1[i]
		l2 = m2[i]
		linha = []
		for j in range(len(l1)):
			v1 = l1[j]
			v2 = l2[j]
			if v1==v2:
				linha.append(0)
			else:
				linha.append(1)
		matriz.append(linha)
	return matriz



def sub(n):
	"""
	Encontrar todos os subconjuntos
	"""
	i = 0
	subc = []
	while i<(1<<n):
		c = []
		s = False
		j = 0
		while j<n:
			if (i & (1<<j)) != False:
				c.append(j+1)
				s = True
			j += 1
		if s == True:
			subc.append(c)
		i += 1
	return subc

def encontrar(x,n,f):
	"""
	Encontrar os movimentos necessarias para passar da matriz de entrada da a matriz de saida
	"""
	re = []
	for i in n:
		z = x
		for j in range(len(i)):
			z = GF(z,i[j])
		if z == f:
			return i 
	return "Nenhum caso possivel"

def atribuir(v,n):
	"""
	Atribuir todos os movimentos a uma lista de movimentos
	"""
	r = [] # retorno
	for i in range(len(n)):
		n1 = []
		n2 = n[i]
		for j in range(len(n2)):
			# print j,n2
			n1.append(v[n2[j] - 1])
		r.append(n1)
	return r
def imprimir(m):
	"""
	Imprimir a matriz
	"""
	re = ''
	for i in m:
		for j in i:
			re += str(j) + ' '
		re += '\n'
	return re

x = iniciar("entrada")
y = iniciar("saida")
print "Digite 0 para usar os movimentos padrao ou 1 para digitar os movimentos"
fim = 0
mov = []
while fim == False:
	try:
		if(int(input())!=0):
			print "Digite a quantidade de movimentos que vao ser utilizados"
			tm = input()
			tm = int(tm)
			print tm
			for i in range(tm):
				movim = iniciar("movimento " + str(i + 1))
				imprimir(movim)
				mov.append(movim)
		else:
			print "Movimentos padrao\n"
			a1 = [[1,1,0],[1,0,0],[0,0,0]]
			print "Matriz movimento 1\n",imprimir(a1)
			a2 = [[1,1,0],[0,1,0],[0,0,0]]
			print "Matriz movimento 2\n",imprimir(a2)
			a3 = [[0,1,1],[0,0,1],[0,0,0]]
			print "Matriz movimento 3\n",imprimir(a3)
			a4 = [[1,0,0],[1,1,0],[1,0,0]]
			print "Matriz movimento 4\n",imprimir(a4)
			a5 = [[0,1,0],[1,1,1],[0,1,0]]
			print "Matriz movimento 5\n",imprimir(a5)
			a6 = [[0,0,1],[0,1,1],[0,0,1]]
			print "Matriz movimento 6\n",imprimir(a6)
			a7 = [[0,0,0],[1,0,0],[1,1,0]]
			print "Matriz movimento 7\n",imprimir(a7)
			a8 = [[0,0,0],[0,1,0],[1,1,1]]
			print "Matriz movimento 8\n",imprimir(a8)
			a9 = [[0,0,0],[0,0,1],[0,1,1]]
			print "Matriz movimento 9\n",imprimir(a9)
			mov.append(a1)
			mov.append(a2)
			mov.append(a3)
			mov.append(a4)
			mov.append(a5)
			mov.append(a6)
			mov.append(a7)
			mov.append(a8)
			mov.append(a9)
		fim = 1
	except Exception, e:
		print "Digite apenas numeros validos"

saida = encontrar(x,atribuir(mov,sub(len(mov))),y)
if saida != "Nenhum caso possivel":
	print "Matrizes para fazer a transicao da matriz de entrada para a matriz de saida\n"
	num = 0
	for sa in saida:
		print "Matiz " + str(num + 1)
		num += 1
		print imprimir(sa)
else:
	print saida