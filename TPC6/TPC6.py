#Modelo (nome;desc;anoCriacao;periodo;compositor;duracao;_id)

import csv

def lerObras(filename):
    file = open(filename, encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=";")

    lista = []
    for obra in csv_file:
        lista.append(tuple(obra))
    return lista


def tamanhoObras(obras):
    return len(obras)


def imprimeObras(obras):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for name, desc, ano, _, comp,*_ in obras:
        print(f"| {name[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15}")



def ordem(tuplo):
    return tuplo[0]


def titAno(obras):
    lista = []
    for name, _, ano, *_ in obras:
        lista.append((name,ano))

    lista.sort(key=ordem)
    return lista


def titAno2(obras):
    lista = []
    for name, _, ano, *_ in obras:
        lista.append((name,ano))

    lista.sort(key= lambda tuplo: tuplo[1])
    return lista


def titporAno(obras):
    dici={}
    for nome, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)

        else: 
            dici[ano] = [nome]

    return dici


def distribPeriodo(obras):
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici    


def distribAno(obras):
    dici = {}
    for _, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano] = dici[ano] + 1
        else:
            dici[ano] = 1
    return dici


def distribComp(obras):
    dici = {}
    for _, _, _, _, comp, *_ in obras:
        if comp in dici.keys():
            dici[comp] = dici[comp] + 1
        else:
            dici[comp] = 1
    return dici


def graph(distrib):
    fig1 = plt.figure(figsize = (30, 15))
    plt.bar(distrib.keys(), distrib.values(), color= "red", width= 0.7)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.title("Gráfico da distribuição")
    plt.ylabel("Quantidade")
    plt.show()
    return

def prob(obras):
    res= []
    listaComp= []
    for obra in obras:
        nome, _, _, _, comp, *_ = obra
        if comp not in listaComp:
            listaComp.append(comp)
    for compositor in listaComp:
        listaObras= []
        for obra in obras:
            nome, _, _, _, comp, *_ = obra
            if  comp == compositor:
                listaObras.append(nome)
        res.append((compositor, listaObras))
    return res

def lerProb(lista):
    for tuplo in lista:
        autor, obras = tuplo
        i = 1
        branco = ""
        print(f"\n{autor:<30}|{obras[0]:<20}")
        while i != len(obras):
            print(f"{branco:<30}|{obras[i]:<20}")
            i += 1
    return