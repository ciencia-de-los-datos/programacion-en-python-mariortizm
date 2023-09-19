"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
        
    lines = data.split('\n')
    suma_total = 0

    for line in lines:
        if line.strip():
            parts = line.split('\t')
            num = int(parts[1])
            suma_total += num

    return suma_total


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])

    letter_counts = {}

    
    lines = data.strip().split('\n')
    for line in lines:
        parts = line.split('\t')
        letter = parts[0]

        
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    
    respuesta_02= sorted(letter_counts.items())

    return respuesta_02


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])

    letter_sums = {}

    lines = data.strip().split('\n')
    for line in lines:
        parts = line.split('\t')
        letter = parts[0]
        value = int(parts[1])


        if letter in letter_sums:
            letter_sums[letter] += value
        else:
            letter_sums[letter] = value


    respuesta_03 = sorted(letter_sums.items())       
    
    return respuesta_03



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    
    meses = {}
    lineas = data.strip().split('\n')

    for linea in lineas:
        campos = linea.split('\t')
        fecha = campos[2]
        mes = fecha.split('-')[1]
        if mes in meses:
            meses[mes] += 1
        else:
            meses[mes] = 1


    respuesta_04 = list(meses.items())

    respuesta_04.sort(key=lambda x: int(x[0]))

    return respuesta_04


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    

    max_values = {}
    min_values = {}

    rows = data.strip().split('\n')

    for row in rows:
        columns = row.split('\t')
        letra = columns[0]
        valor_columna_2 = int(columns[1])

        if letra in max_values:
            max_values[letra] = max(max_values[letra], valor_columna_2)
        else:
            max_values[letra] = valor_columna_2

        if letra in min_values:
            min_values[letra] = min(min_values[letra], valor_columna_2)
        else:
            min_values[letra] = valor_columna_2

    result = [(letra, max_values[letra], min_values[letra]) for letra in sorted(max_values)]

    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    clave_valores_min = {}
    clave_valores_max = {}
    import csv
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if row:
                _, _, _, _, columna5 = row
                entries = columna5.split(',')

                for entry in entries:
                    key, value = entry.split(':')
                    value = int(value)

                    if key in clave_valores_min:
                        if value < clave_valores_min[key]:
                            clave_valores_min[key] = value
                        if value > clave_valores_max[key]:
                            clave_valores_max[key] = value
                    else:
                        clave_valores_min[key] = value
                        clave_valores_max[key] = value

    resultado_06 = []
    for key in sorted(clave_valores_min.keys()):
        resultado_06.append((key, clave_valores_min[key], clave_valores_max[key]))

    return resultado_06



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])

    values_dict = {}

    rows = data.strip().split('\n')

    for row in rows:
        columns = row.split('\t')
        valor_columna_2 = int(columns[1])
        letra_columna_1 = columns[0]

        if valor_columna_2 in values_dict:
            values_dict[valor_columna_2].append(letra_columna_1)
        else:
            values_dict[valor_columna_2] = [letra_columna_1]

    respuesta_07 = [(valor, letras) for valor, letras in values_dict.items()]

    respuesta_07.sort()

    return respuesta_07



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv

    values_dict = {}

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        next(csv_reader)  

        for row in csv_reader:
            valor_columna_2 = int(row[1])
            letra_columna_1 = row[0]

            if valor_columna_2 in values_dict:
                values_dict[valor_columna_2].add(letra_columna_1)
            else:
                values_dict[valor_columna_2] = {letra_columna_1}

    respuesta_08 = [(key, sorted(list(value))) for key, value in sorted(values_dict.items())]

    return respuesta_08


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = """E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
    A	2	1999-10-28	a,f,c	ccc:2,ddd:0,aaa:3,hhh:9
    B	5	1998-05-02	f,e,a,c	ddd:2,ggg:5,ccc:6,jjj:12
    A	3	1999-08-28	a,b	hhh:9,iii:5,eee:7,bbb:1
    C	6	1999-12-01	f,g,d,a	iii:6,ddd:5,eee:4,jjj:12
    A	7	1998-07-28	c,d	bbb:2,hhh:0,ccc:4,fff:1,aaa:7
    A	9	1997-02-28	g,d,a	aaa:5,fff:8,ddd:2,iii:0,jjj:7,ccc:1
    B	1	1999-05-10	b,a	fff:3,hhh:1,ddd:2
    E	2	1997-04-12	d,e,a,f	eee:4,ccc:5,iii:9,fff:7,ggg:6,bbb:2
    B	3	1999-11-23	d,b,g,f	bbb:7,jjj:9,fff:5,iii:4,ggg:3,eee:3
    C	7	1998-01-17	d,c,f,b	hhh:6,eee:4,iii:0,fff:2,jjj:12
    C	5	1998-12-28	d,e,a,c	bbb:7,iii:6,ggg:9
    D	3	1999-10-15	g,e,f,b	bbb:9,aaa:3,ccc:6,fff:4,eee:2
    E	8	1998-11-01	c,f	aaa:8,ddd:5,jjj:12
    B	9	1999-08-12	d,b	ccc:7,jjj:6,fff:7,ddd:3,aaa:2
    D	8	1997-12-01	f,e	ccc:8,eee:6,bbb:9,ddd:3
    E	3	1997-07-28	e,b,f	bbb:6,iii:3,hhh:5,fff:4,ggg:9,ddd:2
    D	5	1998-08-12	g,a	hhh:4,jjj:5,ccc:9
    E	8	1999-08-24	e,c,f,a	ccc:1,iii:6,fff:9
    E	9	1998-01-23	e,a	bbb:9,aaa:3,fff:1
    E	7	1999-06-22	e,f	ddd:9,iii:2,aaa:4
    E	3	1999-04-24	c,b,g	ccc:5,fff:8,iii:7
    D	5	1999-06-25	c,f,a	eee:3,jjj:17,ddd:7
    A	9	1999-08-25	f,a,d	jjj:12,ggg:7,ccc:7,ddd:9,bbb:3
    E	4	1997-07-26	c,d	jjj:6,ccc:4,aaa:1,hhh:9,iii:7,ggg:8
    E	6	1997-09-24	e,d,c	fff:3,eee:6,iii:4,bbb:7,ddd:4,ccc:1
    A	8	1997-09-28	a,e,f	fff:0,ddd:5,ccc:4
    E	5	1999-06-22	c,a,g	ggg:6,hhh:3,ddd:9,ccc:10,jjj:7
    A	6	1999-07-29	f,e	hhh:6,jjj:13,eee:5,iii:7,ccc:3
    C	0	1999-08-22	f,c,a,g	eee:1,fff:4,aaa:2,ccc:7,ggg:10,ddd:6
    A	9	1998-04-26	b,f	ccc:6,aaa:9,eee:5,ddd:0,bbb:3
    D	3	1998-02-24	b,f	bbb:7,hhh:1,aaa:6,iii:4,fff:9,ddd:5
    E	5	1999-03-24	a,c	fff:3,ccc:1,ggg:3,eee:5
    B	4	1998-03-23	b,f,c	iii:7,ggg:3,ddd:0,jjj:8,hhh:5,ccc:1
    B	6	1999-04-21	f,a,e	hhh:6,ccc:3,jjj:9,bbb:8,ddd:7
    D	7	1999-02-29	a,f	aaa:1,fff:5,ddd:3
    B	8	1997-05-21	c,a	ddd:5,jjj:17,iii:7,ccc:10,bbb:4
    C	9	1997-07-22	c,a,e,f	eee:3,fff:2,hhh:6
    E	1	1999-09-28	e,d	fff:9,iii:2,eee:5
    E	5	1998-01-26	f,a,d	hhh:8,ggg:3,jjj:5"""

    clave_contador = {}

    lines = data.strip().split('\n')

    for line in lines:
        parts = line.strip().split('\t')
        column_5 = parts[4].split(',')

        for entry in column_5:
            key, _ = entry.split(':')
            key = key.strip()  
            key = key.strip('\ufeff') 
            if key in clave_contador:
                clave_contador[key] += 1
            else:
                clave_contador[key] = 1

    # Ordenar el diccionario
    clave_contador_ordenado = {k: v for k, v in sorted(clave_contador.items())}

    return clave_contador_ordenado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    respuesta_10 = []
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        
        for row in csvreader:
            letra_columna_1 = row[0]
            column_4 = row[3].split(',')
            column_5 = row[4].split(',')

            cantidad_columna_4 = len(column_4)
            cantidad_columna_5 = len(column_5)

            respuesta_10.append((letra_columna_1, cantidad_columna_4, cantidad_columna_5))

    return respuesta_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_letras = {}
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        
        for row in csvreader:
            columna_2 = int(row[1])
            letras_columna_4 = row[3].split(',')

            for letra in letras_columna_4:
                letra = letra.strip()  
                letra = letra.strip('\ufeff')  
                if letra in suma_letras:
                    suma_letras[letra] += columna_2
                else:
                    suma_letras[letra] = columna_2

    respuesta_11 = {k: v for k, v in sorted(suma_letras.items())}

    return respuesta_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_columna_5 = {}
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        
        for row in csvreader:
            letra_columna_1 = row[0]
            column_5 = row[4].split(',')

            for entry in column_5:
                _, valor = entry.split(':')
                valor = int(valor)
                
                if letra_columna_1 in suma_columna_5:
                    suma_columna_5[letra_columna_1] += valor
                else:
                    suma_columna_5[letra_columna_1] = valor

    # Ordenar el diccionario
    respuesta_12 = dict(sorted(suma_columna_5.items()))

    return respuesta_12
