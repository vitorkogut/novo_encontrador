import urllib.request
import re


def retorna_possiveis_emails(url):

    ####################################
    u2 = urllib.request.urlopen(url)

    linhas = []
    grande_linha = ""
    for lines in u2.readlines():
        linhas.append(lines)
        grande_linha = grande_linha + str(lines)

    index_arrobas = []
    for i in range(len(grande_linha)):
        if str(grande_linha[i]) == "@":
            #print( str(grande_linha[i]) + " INDEX: " + str(i))
            index_arrobas.append(i)

    saidas = []
    for index in index_arrobas:
        txt_atual = ""

        espaco = False
        i = 0
        while espaco == False:
            #print(grande_linha[index - i])
            if( grande_linha[index - i] == " " or grande_linha[index - i] == "<" or grande_linha[index - i] == ">" or grande_linha[index - i] == "|" or grande_linha[index - i] == "\\" or grande_linha[index - i] == "/" or grande_linha[index - i] == "'" or grande_linha[index - i] == '"' or grande_linha[index - i] == '[' or grande_linha[index - i] == ']' or grande_linha[index - i] == ')' or grande_linha[index - i] == '(' or grande_linha[index - i] == '^' or grande_linha[index - i] == '}' or grande_linha[index - i] == '{' or grande_linha[index - i] == '-' or grande_linha[index - i] == ',' or grande_linha[index - i] == '}' or grande_linha[index - i] == '{' or grande_linha[index - i] == '-' or grande_linha[index - i] == '?' or grande_linha[index - i] == ':' or grande_linha[index - i] == '&' or grande_linha[index - i] == ';'):
                espaco = True
            else:
                txt_atual = str(grande_linha[index - i]) + txt_atual
            i = i + 1
        
        espaco = False
        i = 1
        while espaco == False:
            if( grande_linha[index + i] == " " or grande_linha[index + i] == "<" or grande_linha[index + i] == ">" or grande_linha[index + i] == "|" or grande_linha[index + i] == "\\" or grande_linha[index + i] == "/" or grande_linha[index + i] == "'" or grande_linha[index + i] == '"' or grande_linha[index + i] == '[' or grande_linha[index + i] == ']' or grande_linha[index + i] == ')' or grande_linha[index + i] == '(' or grande_linha[index + i] == '^' or grande_linha[index + i] == '}' or grande_linha[index + i] == '{' or grande_linha[index + i] == '-' or grande_linha[index + i] == ',' or grande_linha[index + i] == '}' or grande_linha[index + i] == '{' or grande_linha[index + i] == '-' or grande_linha[index + i] == '?' or grande_linha[index + i] == ':' or grande_linha[index + i] == '&' or grande_linha[index + i] == ';'):
                espaco = True
            else:
                txt_atual = txt_atual + str(grande_linha[index + i])
            i = i + 1
        
        if(txt_atual[0] != "@" and txt_atual[len(txt_atual) - 1] != "@"):
            saidas.append(txt_atual)
    return saidas

def confirma_email(url):
    possiveis = retorna_possiveis_emails(url)
    confirmados = []
    for email in possiveis:
        valido = True

        final = email[len(email)-3] + email[len(email)-2] + email[len(email)-1]
        if(final == "jpg" or final == "png"):
            valido = False
        
        ponto = False
        for i in range(len(email) -1 ):
            if email[i] == ".":
                ponto = True
        
        if valido and ponto:
            confirmados.append(email)
    
    return confirmados



# https://www.magazineluiza.com.br/
# https://www.bc.sc.gov.br/conteudo.cfm?caminho=oportunidades
# https://premacar.com.br/

emails = confirma_email('https://premacar.com.br/')

print(emails)
    









