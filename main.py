import urllib.request
import re
import string

def retorna_possiveis_emails(url):

    ####################################
    u2 = urllib.request.urlopen(url) # Pega o HTML
    chars_permit = list(string.ascii_letters + string.digits + "@" + ".") # array com caracteres permitidos no email


    grande_linha = "" # armazena o HTML
    for lines in u2.readlines():
        grande_linha = grande_linha + str(lines) # concatena a grande linha de HTMLs

    index_arrobas = [] # index dos arrobas
    for i in range(len(grande_linha)):
        if str(grande_linha[i]) == "@":
            index_arrobas.append(i) # guarda a posiçao dos arrobas para serem analisados posteriormente

    saidas = []
    for index in index_arrobas: # Analise de cada arroba
        txt_atual = ""

        espaco = False # aqui basicamente confere os chars a direita e esquerda do index do arroba até encontrar um elemento nao permitido
        i = 0
        while espaco == False:
            letra = grande_linha[index - i] in chars_permit # confere se o char a esquerda esta contido no array de letras permitidas
            if( letra ):
                txt_atual = str(grande_linha[index - i]) + txt_atual # caso seja um char permitido é armazenado numa string "buffer"
            else:
                espaco = True
            i = i + 1
        

        espaco = False
        i = 1
        while espaco == False: # Aqui ocorre o mesmo procediemnto mas a direita do arroba
            letra = grande_linha[index + i] in chars_permit
            if( letra):
               txt_atual = txt_atual + str(grande_linha[index + i])
            else:
                espaco = True
            i = i + 1
        
        if(txt_atual[0] != "@" and txt_atual[len(txt_atual) - 1] != "@"): # confere se nao foi retonado apenas um @
            saidas.append(txt_atual)
    return saidas

def confirma_email(url):
    possiveis = retorna_possiveis_emails(url)
    confirmados = []
    for email in possiveis:
        valido = True

        final = email[len(email)-3] + email[len(email)-2] + email[len(email)-1] # validaçao em casos de imagens com nome "arquivo@servidor.jpg"
        if(final == "jpg" or final == "png"):
            valido = False
        
        ponto = False
        for i in range(len(email) -1 ): # confere se tem pelo menos um ponto no email
            if email[i] == ".":
                ponto = True
        
        if valido and ponto:
            confirmados.append(email)
    
    return confirmados


### links ###
# https://www.magazineluiza.com.br/
# https://www.bc.sc.gov.br/conteudo.cfm?caminho=oportunidades
# https://premacar.com.br/
###       ###


emails = confirma_email('https://www.magazineluiza.com.br/')

print(emails)
    