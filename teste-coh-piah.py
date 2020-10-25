import re
texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."

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


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass
#verificar erro nessa função com o enunciado e o teste#

