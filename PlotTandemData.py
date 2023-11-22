#RiP
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import csv
from MPA2Lists import *

"""
Plots yield vs channel data from TANDEM's .mpa RBS file

INPUTS: "FileName.mca"
OUTPUTS: yield vs channel plot
"""

def PlotData(File, Label):

    Data_y, Data_x = Read_Ge(File) ## Detector Ge

    fig, ax = plt.subplots()
    ax.plot(Data_x,Data_y,'.', color ='xkcd:black', label=str(Label)+'Ge')
    legend = ax.legend(loc="upper right",ncol=2, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Channel',fontsize=22)
    ylabel('Counts', fontsize=22)
    show()

    return
##################################################


###   PLOTS   ###

## Triple alpha source energy calibration
#PlotData('Medidas/e2311_001.mpa', "Calib") ## Use this one

##   Dummy target PG02-14   ##
#PlotData('2023-10/e2310_002.mpa', "PG02-14 Dummy")

##   Activation run   ##
#PlotData('2023-10/e2310_003.mpa', "Step 1")

##   Decay runs   ##
PlotData('Medidas/Decaimento/PG02-19_024.mpa', 'Decay')
PlotData('Medidas/Decaimento/PG02-19_025.mpa', 'Decay')
PlotData('Medidas/Decaimento/PG02-19_026.mpa', 'Decay')

