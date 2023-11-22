##Rip
import os
import csv
from matplotlib.pylab import *
import matplotlib.pyplot as plt

##############################################################################################
def Read_Ge(File):
    Data_y = []
    aux = []
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    for i in range(1143, 9335):
        aux.append(data[i][0].split())
    for i in range(len(aux)):
        Data_y.append(float(aux[i][0]))
    return Data_y
##############################################################################################


##############################################################################################
def MergeYield_MPA(dir):
    """

    """
    mergeYield = [0 for i in range(8192)] # 8192 for Ge det
    for file in os.listdir(dir):
        path = str(dir+"\\"+file)
        Yield = Read_Ge(path)
        mergeYield = [mergeYield[i] + Yield[i] for i in range(len(mergeYield))]
    return mergeYield
##############################################################################################


##############################################################################################
def PlotData(x, y, Label):
    fig, ax = plt.subplots()
    ax.plot(x,y,'.', color ='xkcd:black', label=str(Label))
    legend = ax.legend(loc="best",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Channel',fontsize=22)
    ylabel('Yield', fontsize=22)
    show()
    return
##################################################


##################################################
def Normalize(y, norm):
    return [i/norm for i in y]
##################################################


##################################################
def Normalize2Max(y):
    norm_y = []
    for i in y:
        norm_y.append(i/max(y))
    return norm_y
##################################################


##################################################
def NormalizeBG(dir):
    bg_norm_yield = np.array([0 for i in range(8192)])
    for file in os.listdir(dir):
        path = str(dir+"\\"+file)
        #print(path)
        bg_time = 900. #s
        norm_yield = np.array(Normalize(Read_Ge(path),bg_time))
        bg_norm_yield = [bg_norm_yield[i] + norm_yield for i in range(len(bg_norm_yield))]
    print('Normalizing')
    print(type(bg_norm_yield))
    bg_norm_yield = Normalize2Max(bg_norm_yield)
    return bg_norm_yield
##################################################
