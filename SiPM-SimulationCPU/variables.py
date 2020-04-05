#In this file I define all the global variables that I will use in other fies.
print('Written by Edoardo Proserpio \n')

import numpy as np
import matplotlib.pyplot as plt
import time, random, os, sys, argparse, struct, multiprocessing, matplotlib, psutil, numba
from multiprocessing import Pool
from numpy import exp, hstack, unique, sort, sum, cumsum
from numpy.random import randint, poisson, choice, exponential

plt.style.use("fast")
# matplotlib.use("Qt5Agg")

#################################################################################################################
##################################>>>  VARIABLES DEFINITIONS  <<<################################################
#################################################################################################################

global siglen		# Length of signal in ns
global sampling		# Samlping time in ns
global sigpts		# Total number of points in signal
global ncell		# Total number of cells in SiPM matrix
global cellside		# Number of cells in the side of SiPM matrix
global dcr			# Dark Count Rate in Hz
global xt			# Optical Cross Talk probability in %
global tfall		# Falling time of SiPM signal in ns
global trise		# Rising time of SiPM signal in ns
global cellrecovery	# Cell recovery time in ns
global intstart		# Start of integration gate in ns
global intgate		# Integration gate lenght in ns
global preg			# Lenght of pre-gate in ns
global SNR			# Signal to noise ratio in dB
global basespread	# Baseline spread (sigma)
global ccgv			# Cell to cell gain variation (sigma)
global normpe		# Normalization of peack height (1 pe  = > peak  =  1)
global ap			# After pulsing probability in %
global tauapfast	# After pulses time distribution decay (fast) in ns
global tauapslow	# After pulses time distribution decay (slow) in ns
global fastDCR		# Enable fast generation of DCR (less precision)
global fastXT		# Enable fast generation of XT (less precision)

#################################################################################################################
##################################>>>   EDITABLE VARIABLES   <<<#################################################
#################################################################################################################

###VARIABLES INITIALIZATION##
#Simulation parameters
siglen = 500			#in ns
sampling = 0.1			#in ns

#SiPM parameters
size = 1				#in mm
cellsize = 25			#in um
dcr = 200e3				#in Hz
xt = 0.10				#in %
ap = 0.02				#in %
tfall = 20				#in ns
trise = 1				#in ns
tauapfast = 15			#in ns
tauapslow = 85			#in ns
intstart = 20			#in ns
intgate = 300			#in ns
preg = 20				#in ns
SNR = 30				#in dB
basespread = 0.00		#relative to single pe peack height (sigma)	Off at the moment
ccgv = 0.05				#relative to single pe peack height (sigma)

fastDCR = False
fastXT = False

#################################################################################################################
####################################>>> ARGUMENTSS PARSER   <<<##################################################
#################################################################################################################

parser = argparse.ArgumentParser("SiPM Simulation")
parser.add_argument("-g","--graphics",action = 'count',help = "Plots of generated events histograms")
parser.add_argument("-v","--verbosity",action = 'count',help = "Set verbosity of simulation")
parser.add_argument("-w","--write",nargs = '?',type = str,help = "File to write as output")
parser.add_argument("-G","--Graphics",action = 'count',help = "Plot each signal (Heavy!)")
parser.add_argument("-j","--jobs",type = int,help = "Number of jobs for multiprocessing")
parser.add_argument("-NDCR","--nodcr",action = 'count',help = 'Set DCR rate to 0')
parser.add_argument("-FDCR","--fastdcr",action = 'count',help = 'Faster generation of DCR')
parser.add_argument("-NXT","--noxt",action = 'count',help = 'Set XT rate to 0')
parser.add_argument("-FXT","--fastxt",action = 'count',help = 'Faster generation of XT')
parser.add_argument("-NAP","--noap",action = 'count',help = 'Set AP rate to 0')
args = parser.parse_args()

pltFlag = args.Graphics

if args.jobs is not None:					#If a number of jobs is choosen then it is used
	nJobs = args.jobs
else:
	nJobs = multiprocessing.cpu_count()		#If not specified all cores are used

if not args.verbosity:
	sys.stdout  =  open('/dev/null','w')		#Move all printed output to inexisting file

if args.nodcr:								#Set dcr rate to 0
	dcr = 0

if args.noxt:								#Set xt rate to 0
	xt = 0

if args.noap:
	ap = 0

if args.fastdcr:
	fastDCR  =  True

if args.fastxt:
	fastXT  =  True

print('Detected %d cores...\r'%(multiprocessing.cpu_count()))
print('Starting simulation on %d cores...\r'%(nJobs))

#################################################################################################################
#################################>>> NOT EDITABLE VARIABLES   <<<################################################
#################################################################################################################
#Conversion of time units from ns to units of sampling times. All the simulation works using samples as time unit.
sampling *= 1.
tfall = np.float32(tfall/sampling)
trise = np.float32(trise/sampling)
tauapfast = np.float32(tauapfast/sampling)
tauapslow = np.float32(tauapslow/sampling)
sigpts = int(siglen/sampling)
cellside = int(size/(cellsize*1e-3))
ncell = int(cellside**2)-1
intstart = int(intstart/sampling)
intgate = int(intgate/sampling)
preg = preg/sampling
preg = int(intstart-preg)
b = tfall/trise
normpe = 1	#(b**(1/(1-b))-b**(1/((1/b)-1)))**-1
SNR = np.sqrt(10**(-SNR/10))
