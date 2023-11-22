## Rip

from matplotlib.pylab import *
import matplotlib.pyplot as plt
from fAnalysis import *
import numpy as np


###   Background removal   ###

## Set-up bg dir
bg_dir = "Medidas\Ge_Background"
## Merge bg files
bg_yield = MergeYield_MPA(bg_dir)
## Set-up ge channel list
ge_ch = [i for i in range(8192)]
## Plot merged bg
#PlotData(ge_ch, bg_yield, "Background")

## Normalize bg runs to measure time
## 16h32 -> 10h31
# 24h-16h30m + 10h30m = 
# 18h = 3600 * 18 = 64800 s
bg_time = 900. #s = 15 min/run
bg_norm_yield = NormalizeBG(bg_dir)
PlotData(ge_ch, bg_norm_yield, "Norm. BG sum")

decay_dir = "Medidas\Decaimento"
decay_yield = MergeYield_MPA(decay_dir)

decay_time = 237600. #s
norm_decay = np.array(Normalize(decay_yield, decay_time))
#PlotData(ge_ch, norm_decay, "Decay")

removed_bg = norm_decay - norm_bg
#PlotData(ge_ch, removed_bg, 'Removed Bg')
###############################################################

###   Plot norm decay - norm bg
decay_files = os.listdir(decay_dir)
decays = np.array([Normalize(Read_Ge(decay_dir+"\\"+file),1800.) for file in decay_files])

fig, ax = plt.subplots()
ax.plot(ge_ch,decays[1],'.', color ='xkcd:black', label='2')
ax.plot(ge_ch,decays[2],'+', color ='xkcd:red', label='1')
legend = ax.legend(loc="upper right",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
legend.get_frame().set_facecolor('#DAEBF2')
tick_params(axis='both', which='major', labelsize=22)
xlabel('Channel',fontsize=22)
ylabel('Counts', fontsize=22)
show()


