#Function of simulation
from lib import *

def SiPM(times,other):
	###SIMULATION CORE###
	dcrTime=addDCR()													#Generate DCR events (times and positions on matrix)
	if dcrTime.size:
		times=hstack((times,dcrTime))									#Concatenate DCR events with photoelectrons events
		sigTimes,sigH=evtsGen(times)									#Update list of times considering SiPM matrix occupancy and recovery times
	else:
		sigTimes,sigH=evtsGen(times)

	signal=signalGen(sigTimes,sigH)													#Generate digital signals

	signalInGate=signal[intstart:intstart+intgate]
	baseline = 0
	#baseline=np.mean(signal[preg:intstart])*0									#Calculating baseline
	integral=sum(signalInGate-baseline)*sampling								#Calculating integrals
	peak=np.amax(signalInGate)-baseline											#Calculating peaks
	tstart=np.argmax(signalInGate>1.5)*sampling									#Calculating starting times of signals
	#tovert=sum(signalInGate>1.5)*sampling										#Calculating time over threshld
	#tpeak=np.argmax(signalInGate)*sampling										#Calculating peaking time
	if pltFlag:
		dev="CPU"
		sigPlot(signal,dev,sigTimes,dcrTime)
	return(integral,peak,tstart,other)
