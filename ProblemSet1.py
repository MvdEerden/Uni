# version 1.0

import numpy as np 
import matplotlib.pyplot as plt
import os

#%%
# Problem 1

path = 'C:\\Users\\menno\\Desktop\\Code\\Python\\ALOP\\data\\'
Ab = np.loadtxt(path+'Ab1f.dat.fix',delimiter=',')[:,0] # initialise the Ab array with its specific wavelengths
Ab = np.append(Ab,'filename')
Bb = np.loadtxt(path+'Bb11.dat.fix',delimiter=',')[:,0] # initialise the Bb array with its specific wavelengths
Bb = np.append(Bb,'filename')
spectra = np.genfromtxt(path+'spectra.list.csv',dtype=str,delimiter=',')

for filename in os.listdir(path):
  # fill Ab with all Flux values
  if filename.endswith("f.dat.fix"): 
    #Ab{}f files
    fname = path + filename
    arr = np.loadtxt(fname, delimiter=',')
    arr = np.append(arr[:,1],filename)

    Ab = np.c_[Ab, arr] # adds Flux values to Ab array

 # fill Bb with all Flux values   
  elif filename.endswith('.dat.fix'):
    #Bb{} files
    fname = path + filename
    arr = np.loadtxt(fname, delimiter=',')
    arr = np.append(arr[:,1],filename)
    Bb = np.c_[Bb, arr] # adds Flux values to Bb array
  else:
    pass

#%%
picks = np.random.randint(0,len(Ab[0]),2)

plt.figure()
plt.xlim(3000,9000)

plt.xlabel(r"Wavelength in $\AA$")
plt.ylabel(r"Flux in $erg/s/cm^2/\AA$")
plt.title("Spectral energy distributions")
for el in picks:
  plt.plot(Ab[:-1,0],Ab[:-1,el+1])

#plt.legend()
plt.grid()
# plt.yticks(np.linspace(0,3e-7,100))
plt.show()

#%%
