# Paso 1: Leer cada parte del archivo
# Devuelve la cadena con la posicion y no se confunde por que va de letra en letra
def word_reader(file, current):
    temp = ""
    while current < len(file):
        if(file[current] == " " or file[current] == "\n") and (len(temp) > 0):
            break
        elif file[current] == " " or file[current] == "\n":
            current += 1
        else:
            temp += file[current]
            current += 1

    return temp, current

# Toma cada una de las letras y forma las palabras
# Con el for se puede ver cuando haga match entonces va a 
# su funcion respectiva
def readerino(file):
    a = 1
    current = 0
    chars = []
    tokens = []
    keywords = []
    prods = []
    temp = ""
    while True:
        temp, current = word_reader(file, current)
        if temp == "COMPILER":
            title, current = compiler(file, current)
        if temp == "CHARACTERS":
            chars, current = charas(file, current)
        if temp == "KEYWORDS":
            keywords, current = keys(file, current)
        if temp == "TOKENS":
            tokens, current = toks(file, current)
        if temp == "END":
            endof = endofline(file, current, title)
            if endof:
                break
            else:
                print("no hay final de archivo")
                exit()

    return title, chars, tokens, keywords, prods


# Devuelve el titulo y la posicion
def compiler(file, current):
    current += 1
    title, current = word_reader(file, current)
    return title, current


# Cuando encuentre characters va a seguir, cuando encuentre Keywords
# Regresa una y ahi se termina el ciclo
# Pero sino no encuentra, continua y se hace split de lo que este del lado 
# izquierdo y derecho del igual, se devuelve la lista de IDs y valores
def charas(file, current):

    current += 1
    charass = {}
    line = ""

    while True:
        temp, current = word_reader(file, current)
        if temp == "KEYWORDS":
            current -= 8
            break
        line += temp
        if line[-1] == "." and line[-2] != ".":
            if "=" in line:
                alles = line.split("=")
                ids = alles[0]
                vals = alles[1]
                charass[ids] = vals
                line = ""
            else:
                print("'=' no encontrado")
    return charass, current

# Cuando encuentre characters va a seguir, cuando encuentre Keywords
# Regresa una y ahi se termina el ciclo
# Pero sino no encuentra, continua y se hace split de lo que este del lado 
# izquierdo y derecho del igual, se devuelve la lista de IDs y valores
def keys(file, current):
    current += 1
    temp = ""
    keyes = {}
    ids = ""
    vals = ""
    line = ""
    while True:
        temp, current = word_reader(file, current)
        if temp == "TOKENS":
            current -= 6
            break
        line += temp
        if line[-1] == ".":
            if "=" in line:
                alles = line.split("=")
                ids = alles[0]
                vals = alles[1]
                keyes[ids] = vals
                line = ""
            else:
                print("'=' no encontrado")

    return keyes, current


# Cuando encuentre characters va a seguir, cuando encuentre Keywords
# Regresa una y ahi se termina el ciclo
# Pero sino no encuentra, continua y se hace split de lo que este del lado 
# izquierdo y derecho del igual, se devuelve la lista de IDs y valores
def toks(file, current):
    current += 1
    temp = ""
    tokis = {}
    ids = ""
    vals = ""
    line = ""
    while True:
        temp, current = word_reader(file, current)
        if temp == "END":
            current -= 3
            break
        line += temp
        if line[-1] == ".":
            if "=" in line:
                alles = line.split("=")
                print("este es alles", alles)
                ids = alles[0]
                vals = alles[1]
                print(alles[1])
                tokis[ids] = vals
                line = ""
            else:
                print("'=' no encontrado")

    return tokis, current


# Chequea que sea la misma palabra con la que empieza
def endofline(file,current, title):
    current += 1
    enderino, current = word_reader(file,current)
    if enderino == title:
        return True
    return False