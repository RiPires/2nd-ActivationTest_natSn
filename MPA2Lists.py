# Rip
import csv

def Read_TANDEM_Data(File, det):

    Data_x = []
    Data_y = []
    aux = []

    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)

    if det == "E": #MOV E
        for i in range(143, 1166):
            aux.append(data[i][0].split())
    elif det == "Ge": #Ge
        for i in range(1168, 9360):
            aux.append(data[i][0].split())
    elif det == "D": #MOV D
        for i in range(9361, 10384):
            aux.append(data[i][0].split())

    for i in range(len(aux)):
        Data_x.append(float(i)) ## axes in channel
        Data_y.append(float(aux[i][0]))

    return Data_x, Data_y
#########################################################
#########################################################


def Read_Ge(File):

    Data_x = []
    Data_y = []
    aux = []

    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)

    for i in range(1143, 9335):
        aux.append(data[i][0].split())

    for i in range(len(aux)):
        Data_x.append(float(i)) ## axes in channel
        Data_y.append(float(aux[i][0]))

    return Data_y, Data_x