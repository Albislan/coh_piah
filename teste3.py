import re
textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', ' Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def separa_palavras(frase):
    return frase.split()

def filtra_palavras(palavras):
    palavras_filtradas = []
    for x in palavras:
        item = x
        for y in [(',')]:
            item = item.replace(y, "")
            palavras_filtradas.append(item)
    return palavras_filtradas   

def conta_palavras(texto):
    sep_palavras = separa_palavras(texto)
    return len(sep_palavras)


def conta_sentencas(texto):
    sep_sentencas = separa_sentencas(texto)
    return len(sep_sentencas)


def conta_letras(texto):
    letras = []
    for letra in texto:
        total = 0
        if letra == " " or letra == "," or letra == "." or letra == "!" or letra == "?":
            del(letra)
        else:
            letras.extend(letra)
    return len(letras)
    
def conta_caracteres(texto):
    caracteres = []
    for caracter in texto:
        total = 0
        if caracter == ".":
            del(caracter)
        else:
            caracteres.extend(caracter)
    return len(caracteres)           

def conta_caracteres_frase(texto):
     caracteres = []
     for caracter in texto:
          total = 0
          if caracter == "." or caracter == ",":
               del(caracter)
          else:
               caracteres.extend(caracter)
     return len(caracteres)    

def conta_frases(texto):
     sentencas = separa_sentencas(texto)
     n = len(sentencas)
     splited = []
     len_l = len(sentencas)
     for i in range(n):
          start = int(i*len_l/n)        
          end = int((i+1)*len_l/n)
          splited.append(sentencas[start:end])

     soma_qtd_frases = [] 
     for i in splited:
          qtd_frases = len(separa_frases(str(i)))
          soma_qtd_frases.append(qtd_frases)
     return sum(soma_qtd_frases)      

def remove_virgula(palavra):
    caracter = ","
    for letra in range(0, len(caracter)):
        palavra = palavra.replace(caracter[letra],"")
    
    return palavra

def remove_ponto(palavra):
    caracter = ","
    for letra in range(0, len(caracter)):
        palavra = palavra.replace(caracter[letra],"")
    
    return palavra

def calcula_assinatura(texto):
    tam_med_palavras = conta_letras(texto) / conta_palavras(texto) #wal_texto#
    type_token = n_palavras_diferentes(filtra_palavras(separa_palavras(texto))) / conta_palavras(texto)
    hapax = n_palavras_unicas(filtra_palavras(separa_palavras(texto))) / conta_palavras(texto)
    tam_med_sent = conta_caracteres(texto) / len(separa_sentencas(texto))
    complex_sentenca = conta_frases(texto) / len(separa_sentencas(texto))
    tam_med_frase = conta_caracteres_frase(texto) / conta_frases(texto)
    return [tam_med_palavras, type_token, hapax, tam_med_sent, complex_sentenca, tam_med_frase]


lista = []
for texto in textos:
    assinatura = calcula_assinatura(str(texto))
    lista.append(assinatura)
    
for as_b in lista:

    print(as_b)     

fia = [4.5396825396825395, 0.7777777777777778, 0.6666666666666666, 89.0, 3.25, 26.846153846153847]
fib = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
i = 6
x = 0
res = []
while i > 0:
    res.append(abs(fia[x] - fib[x]))
    i = i-1
    x = x+1
print(res)    
sab = sum(res) / 6
print(sab)



    