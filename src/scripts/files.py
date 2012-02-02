# -*- coding: utf-8 -*-
def registerLinesByWordFound(word):
    file    = open('files/texto.txt', 'r', encoding = 'utf-8')
    fileLog = open('files/log.txt',   'a', encoding = 'utf-8')
    lines   = file.readlines()
    
    for line in lines:
        if word in line:
            print('Encontrado "' + word + '" na linha: ' + str(lines.index(line) + 1), file = fileLog)
    
    print("<<<Análise chegou ao fim do arquivo!>>>\n", file = fileLog)
    file.close()

if __name__ == '__main__':
    registerLinesByWordFound('Lorem Ipsum')