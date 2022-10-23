def lerInf(file):
    f=open(str(file),"r")
    lista=[]

    for line in f:     
        paciente=line[:-1].split(",")
        lista.append(paciente)
    f.close
    return lista



def doencaSexo(lista):
    F = 0
    M = 0
    for i in lista:
        if i[-1] == "1":
            if i[1] == "F":
                F = F + 1

            if i[1] == "M":
                M = M + 1

    contagem = [("F", F),("M", M)]
    return contagem
                 

def doencaIdade(lista):
    distribuicao = []
    e = 30
    while e < 80:
        escalao = [e, e+4]
        numPessoas = 0
        for i in lista:
            if i[-1] == "1" and escalao[0] <= int(i[0]) <= escalao[1]:
                numPessoas = numPessoas + 1
        distribuicao.append((escalao,numPessoas))
        e = e + 5
    return distribuicao
        

def doencaColesterol(lista):
    distribuicao = []
    c = 0
    while c < 540:
        niveis = [c, c+10]
        numPessoas = 0
        for i in lista:
            if i[-1] == "1" and niveis[0] <= int(i[3]) < niveis[1]:
                numPessoas = numPessoas + 1
        distribuicao.append((niveis,numPessoas))
        c = c + 10
    return distribuicao



def tabela(dados,criterio):

    if criterio == doencaSexo:
        print("Sexo  |  Nº de Doentes")
        for i in doencaSexo(dados):
            print(i[0],"|",i[1])
    print("\n")
    
    
    if criterio == doencaIdade:
        print("Idade  |  Nº de Doentes")
        for i in doencaIdade(dados):
            print(i[0],"|",i[1])
    print("\n")

   
    if criterio == doencaColesterol:
        print("Colesterol  |  Nº de Doentes")
        for i in doencaColesterol(dados):
            print(i[0],"|",i[1])
    print("\n")

dados = lerInf("myheart.csv")

tabela(dados,doencaSexo)
tabela(dados,doencaIdade)
tabela(dados,doencaColesterol)
