# version 1.1
# This version finally works for problem 1.
#%%
import numpy as np 
import matplotlib.pyplot as plt
import os

#%%
# Problem 1

path = 'C:\\Users\\menno\\Desktop\\Code\\Python\\ALOP\\data\\'
Ab = np.loadtxt(path+'Ab1f.dat.fix',delimiter=',')[:,0] # initialise the Ab array with its specific wavelengths
Ab = np.append(Ab,0) # this serves as a space for fileID
Bb = np.loadtxt(path+'Bb11.dat.fix',delimiter=',')[:,0] # initialise the Bb array with its specific wavelengths
Bb = np.append(Bb,0) # this serves as a space for fileID
spectra = np.genfromtxt(path+'spectra.list.csv',dtype=str,delimiter=',')

for filename in os.listdir(path):
  # fill Ab with all Flux values
  if filename.endswith("f.dat.fix"): 
    #Ab{}f files
    fname = path + filename
    arr = np.loadtxt(fname, delimiter=',',dtype=np.float32)
    arr = np.append(arr[:,1],int(filename[2:-9])) # adds fileID
    Ab = np.c_[Ab, arr] # adds Flux values to Ab array

 # fill Bb with all Flux values   
  elif filename.endswith('.dat.fix'):
    #Bb{} files
    fname = path + filename
    arr = np.loadtxt(fname, delimiter=',')
    arr = np.append(arr[:,1],int(filename[2:-8])) # adds fileID
    Bb = np.c_[Bb, arr] # adds Flux values to Bb array
  else:
    pass

#%%
picks = [2,4,7]

plt.figure()
plt.xlim(3000,9000)

plt.xlabel(r"Wavelength in $\AA$")
plt.ylabel(r"Flux in $erg/s/cm^2/\AA$")
plt.title("Spectral energy distributions")
for el in picks:
  fname = "Ab{}f.dat.fix".format(int(Ab[-1,el+1]))
  index = int(np.argwhere(spectra[:,0] == fname))
  plt.plot(Ab[:-1,0],Ab[:-1,el+1],label="Star {}, type {}".format(spectra[index,0][:5],spectra[index,1]))

plt.legend()
plt.grid()
plt.show()

#%%
