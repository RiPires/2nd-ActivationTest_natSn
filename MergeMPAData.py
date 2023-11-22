#RiP
import MPA2Lists
from MPA2Lists import *
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import os

##############################################################################################
def MergeYield_MPA(Dir):
    """
    Merges yields from different detectors' data .mpa files, in a specific directory, into a single list
    INPUTS:
    directory containing data files and desired detector
    OUTPUTS:
    Merged yield list
    """
    ConvYield = [0 for i in range(8192)] # 8192 for Ge det
    for file in os.listdir(Dir):
        Path = str(Dir+"\\"+file)
        Yield, Channel = Read_Ge(Path)
        ConvYield = [ConvYield[i] + Yield[i] for i in range(len(ConvYield))]
    return ConvYield, Channel
##############################################################################################


###   Ge Background merge and plot   ###
""" Ge_bg_Dir = "Medidas\Ge_Background"
Yield, Channel = MergeYield_MPA(Ge_bg_Dir)

fig, ax = plt.subplots()
ax.plot(Channel, Yield,'+-', color ='xkcd:blue', label=('Ge background'))
legend = ax.legend(loc="upper right",ncol=2, shadow=True,fancybox=True,framealpha = 0.0,fontsize=20)
legend.get_frame().set_facecolor('#DAEBF2')
tick_params(axis='both', which='major', labelsize=22)
xlabel('Channel',fontsize=22)
ylabel('Yield', fontsize=22)
#grid()
show() """
###########################################


###   Decay nerge and plot   ###
decay_dir = 'Medidas\Decaimento24'
Yield, Channel = MergeYield_MPA(decay_dir)
fig, ax = plt.subplots()
ax.plot(Channel, Yield,'+-', color ='xkcd:blue', label=('Decay'))
legend = ax.legend(loc="upper right",ncol=2, shadow=True,fancybox=True,framealpha = 0.0,fontsize=20)
legend.get_frame().set_facecolor('#DAEBF2')
tick_params(axis='both', which='major', labelsize=22)
xlabel('Channel',fontsize=22)
ylabel('Yield', fontsize=22)
show()