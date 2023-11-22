#RiP
import os
import matplotlib.pyplot as plt
from matplotlib.pylab import *
from MPA2Lists import *
from Normalize import *

# set total accumulation for each peak and time as zero
accu_g = 0.
accu_t = 0.
# set empty lists to store accumulation points and time
Accu_g = []
Accu_t = []
# set regions of interest for each peak
gamma_roi_d = int(299)
gamma_roi_u = int(306)
# for each spectrum (15 min read), determine integral on Ka, Kb and gamma peaks
dir = "Medidas\Decaimento"
for file in os.listdir(dir):
    counts, channel = Read_Ge(str(dir+"\\"+file))
    # add each integral to the total
    for ch in range(gamma_roi_d, gamma_roi_u):
        accu_g += counts[ch]
    accu_t += 15
    # save integral as the nth point
    Accu_g.append(accu_g)
    Accu_t.append(accu_t)

###   Accumulation PLOT   ###
fig, ax = plt.subplots()
ax.plot(Accu_t, Normalize(Accu_g),'*', color ='xkcd:blue', label=('gamma'))
legend = ax.legend(loc="upper left",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
legend.get_frame().set_facecolor('#DAEBF2')
tick_params(axis='both', which='major', labelsize=22)
xlabel('Time (minutes)',fontsize=22)
ylabel('Yield', fontsize=22)
show()
###########################################
 
