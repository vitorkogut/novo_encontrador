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
            if( grande_linha[index - i] == " " or grande_linha[index - i] == "<" or grande_linha[index - i] == ">" or grande_linha[index - i] == "|" or grande_linha[index - i] == "\\" or grande_linha[index - i] == "/" or grande_linha[index - i] == "'" or grande_linha[index - i] == '"' or grande_linha[index - i] == '[' or grande_linha[index - i] == ']' or grande_linha[index - i] == ')' or grande_linha[index - i] == '(' or grande_linha[index - i] == '^'):
                espaco = True
            else:
                txt_atual = str(grande_linha[index - i]) + txt_atual
            i = i + 1
        
        espaco = False
        i = 1
        while espaco == False:
            if( grande_linha[index + i] == " " or grande_linha[index + i] == "<" or grande_linha[index + i] == ">" or grande_linha[index + i] == "|" or grande_linha[index + i] == "\\" or grande_linha[index + i] == "/" or grande_linha[index + i] == "'" or grande_linha[index + i] == '"' or grande_linha[index + i] == '[' or grande_linha[index + i] == ']' or grande_linha[index + i] == ')' or grande_linha[index + i] == '(' or grande_linha[index + i] == '^'):
                espaco = True
            else:
                txt_atual = txt_atual + str(grande_linha[index + i])
            i = i + 1
        
        if(txt_atual[0] != "@" and txt_atual[len(txt_atual) - 1] != "@"):
            saidas.append(txt_atual)
    return saidas

emails = retorna_possiveis_emails('https://www.codegrepper.com/code-examples/python/How+to+check+if+a+value+is+an+empty+string+in+python')

print(emails)
    









