import utils
import toAutomata
def create_file(final, dfas, title):
    output = open("./outputs/" + title + ".py", "w+", encoding="utf-8")
    output.write("import utils\n")
    output.write("import automateichon\n")
    output.write("import automataEsq\n")
    output.write("import nfaToDfa\n")
    output.write("import toAutomata\n")
    i = 0
    output.write("def matching(automata, texto):\n")
    output.write("    opts = list(texto)\n")
    output.write("    est = [0]\n")
    output.write("    est = utils.cerraduraEpsilon(automata, est)\n")
    output.write("    q = 0\n")
    output.write("    while True:\n")
    output.write("        temporales = []\n")
    output.write("        for es in est:\n")
    output.write("            for trans in automata.states[es].transitions:\n")
    output.write("                if trans.simbolo == opts[q] and trans.destino not in temporales:\n")
    output.write("                    temporales.append(trans.destino)\n")
    output.write("        q += 1\n")
    output.write("        temporales = utils.cerraduraEpsilon(automata, temporales)\n")
    output.write("        if not temporales and opts == utils.EPSILON:\n")
    output.write("            break\n")
    output.write("        est = temporales.copy()\n")
    output.write("        if q > len(opts)-1:\n")
    output.write("            break\n")
    output.write("    for x in est:\n")
    output.write("        if automata.states[x].accept:\n")
    output.write("            return True\n")
    output.write("    return False\n")
    output.write("def longest_string(file, automata, current = 0):\n")
    output.write("    temp = ''\n")
    output.write("    valid = []\n")
    output.write("    while current < len(file):\n")
    output.write("        temp += file[current]\n")
    output.write("        if matching(automata, temp):\n")
    output.write("            valid.append(temp)\n")
    output.write("        current += 1\n")
    output.write("    if valid:\n")
    output.write("        return max(valid, key = len)\n")
    output.write("    return False\n")


    output.write("def main():\n")
    output.write("    automatas = []\n")

    writeAutomata(final, i, output)
    i += 1

    for dfa in dfas:
        writeAutomata(dfas[dfa], i, output, dfa)
        i += 1

    output.write("    print('nombre de archivo:')\n")
    output.write("    test = input()\n")
    output.write("    filerino = open('/Users/cristinabautista/Desktop/Diseño Lenguajes/Proyecto2_DdL/Proyecto2/tests/' + test)\n")
    output.write("    words = filerino.read()\n")
    output.write("    filerino.close()\n")
    output.write("    i = 0\n")
    output.write("    last = 0\n")
    output.write("    while i < len(words):\n")
    output.write("        valid = longest_string(words, automata0, i)\n")
    output.write("        if valid:\n")
    output.write("            if last != 0 and (i - last > 0):\n")
    output.write("                while last < i:\n")
    output.write("                    last += 1\n")
    output.write("            last += len(valid)\n")
    output.write("            aut = 1\n")
    output.write("            while aut<len(automatas):\n")
    output.write("                if (matching(automatas[aut], valid)):\n")
    output.write("                    print(valid, 'is', automatas[aut].id)\n")
    output.write("                    break\n")
    output.write('                aut += 1\n')
    output.write("            i += len(valid)\n")
    output.write("        else:\n")
    output.write("            i+=1\n")
    output.write('if __name__ == "__main__":\n'+'   main()')




def writeAutomata(automata, i, file, title="el grande"):
    file.write("    automata"+str(i)+' = automataEsq.Machine("'+ title +'")\n')
    for n in automata.states:
        file.write("    tempNode = automataEsq.State(" + str(n.id) + ")\n")
        if n.accept:
            file.write("    tempNode.accept = True\n")
        for t in n.transitions:
            if t.simbolo == utils.EPSILON:
                z = utils.EPSILON
            else:
                z = t.simbolo
            file.write("    trans = automataEsq.Transition('" + z + "' , " + str(t.destino) + ")\n")
            file.write("    tempNode.transitions.append(trans)\n")
        file.write("    automata"+str(i)+".states.append(tempNode)\n")
    file.write("    automatas.append(automata" + str(i) + ")\n")
    file.write("\n")

if __name__ == "__main__":
    archivito = "inputs/ArchivoPrueba1v2.0.atg"
    file = open(archivito)
    content = file.read()
    errores = False
    lista_errores = []
    if "EXCEPT KEYWORDS" in content:
        if content.count("KEYWORDS") == 1:
            lista_errores.append("Error: No existe la seccion de KEYWORDS en el documento")
            # errores = True
    if "KEYWORDS" not in content:
        lista_errores.append("Error: No existe la seccion de KEYWORDS en el documento")
        # errores = True
    if "CHARACTERS" not in content:
        lista_errores.append("Error: No existe la seccion de CHARACTERS en el documento")
        # errores = True
    if "TOKENS" not in content:
        lista_errores.append("Error: No existe la seccion de TOKENS en el documento")
        # errores = True
    with open(archivito) as file2:
        importantes = ['KEYWORDS\n', 'CHARACTERS\n', 'TOKENS\n']
        content2 = file2.readlines()
        contador = 0
        for i in content2:
            contador += 1 
            if i[len(i)-2] != '.' and i != '\n' and contador != 1 and contador != len(content2) and i not in importantes and i[len(i)-2] != '=':
                lista_errores.append([i, "No hay punto en la linea: ", contador])
            if i.count('"') % 2 !=0:
                lista_errores.append("No hay misma cantidad de comillas")
            if i.count("{") != i.count("}"):
                lista_errores.append("Las llaves no corresponden")
            if len(i) <= 3 and i != '\n':
                lista_errores.append("Error en la linea: ", contador)

    if len(lista_errores) > 0:
        for i in lista_errores:
            print(i)
        exit()


    title, chars, tokens, keywords, prods = toAutomata.lecture.readerino(content)
    file.close()
    prueba = toAutomata.charToAutomata(chars)
    keywordsitas = toAutomata.keyworder(keywords)
    tokenilos = toAutomata.tokensToAutomata(tokens, prueba)
    final, dfas = toAutomata.theBigOne(keywordsitas, tokenilos)
    create_file(final, dfas, "scanner")

            
    
    # with open(archivo) as file:
