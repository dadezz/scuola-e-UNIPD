import numpy as np
import matplotlib.pyplot
dat = np.genfromtxt("fileprof")
datbss = np.genfromtxt("filebss")
idoss = dat[:,0]
idbss = datbss[:,0]
magbss =datbss[:,1]
mag = dat[:,1]
errbss = datbss[:,2]
magmedia = np.sum(mag)/mag.size
magmediabss = np.sum(magbss)/magbss.size
flux = 10**(magmedia*2,5)
fluxbss = 10**(magmediabss*2,5)
rapportoflux =  flux/fluxbss
print("rapporto dei flussi: ", rapportoflux)
