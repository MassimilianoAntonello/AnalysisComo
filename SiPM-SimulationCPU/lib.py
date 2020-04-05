#In this file I define all  the functions I will use in the main file of simulation
from variables import *

#################################################################################################################
################>>>   EDITING THIS FILE MAY SERIOUSLY COMPROMISE SIMULATION BEHAVIOUR   <<<######################
#################################################################################################################

###GENERATION OF DCR TIMES AND INDICES###
def addDCR():											#Generate dcr times
	if fastDCR:
		ndcr = poisson(dcr*siglen*1e-9)					#Number of dcr events folows a poissonian distribution											## TODO: Delay esponenziale?
		dcrTime = np.random.random(ndcr)*siglen
	else:
		dcrTime = [0]
		while dcrTime[-1]<siglen:
			delayDCR = random.expovariate(dcr)*1e9
			dcrTime.append(dcrTime[-1]+delayDCR)
		dcrTime = np.array(dcrTime[1:-1])
	return(dcrTime)

###FUNCTION TO UPDATE THE SIPM MATRIX ARRAY###
def evtsGen(time):
	evtTimes = []
	sigHtemp = []
	if time.size > 0:
		idx = randint(0,ncell,time.size,dtype=np.int32)							#Generate random indexes for each cell to be fired
		time = (sort(time)/sampling)											#Convert times in sampling times units and sort them
		if fastXT:
			nxt = poisson(xt*time.size)											#Generate number of cross talk events
			if nxt > 0:
				addcells=(-1,1,-cellside,cellside,-1-cellside,-1+cellside,1-cellside,1+cellside)	#Values to add to change cell for XT (8 adjacent cells)
				xtidx = randint(0,time.size,nxt,dtype=np.int32)					#Indexes of cells triggering xt events
				xtcells = idx[xtidx]											#Cell ids triggering xt events
				xttimes = time[xtidx]											#Times of xt events
				xtcells += choice(addcells,nxt)									#Select neighbouring cells
				idx = hstack((idx,xtcells))										#Add XT cells to the list
				time = hstack((time,xttimes))									#Add XT times to the list
		elif not fastXT:
			nxt = poisson(xt,time.size)											#Generate number of poisson events per each cell
			if np.sum(nxt)>0:
				xtcells = []
				xttimes = []
				for i in range(time.size):
					if nxt[i]>0:
						addcells=(-1,1,-cellside,cellside,-1-cellside,-1+cellside,1-cellside,1+cellside)
						xtcells.extend(idx[i]+choice(addcells,nxt[i]))
						xttimes.extend([time[i]]*nxt[i])
				idx = hstack((idx,xtcells))
				time = hstack((time,xttimes))

		if idx.size == len(set(idx)):											#If all cells index are different output all times without other iterations
			evtTimes = time
			sigH = time*0+1														#All signals have height 1
		else:
			uCells,uCellsIdx,uCellsCounts = np.unique(idx,return_index=True,return_counts=True)
			sTimes = time[uCellsIdx[uCellsCounts==1]]							#Times of cells fired once
			evtTimes.append(sTimes)												#Add times of cells fired once
			sigHtemp.append(sTimes*0+1)											#Cells fired once have an height of 1

			mCellIdx = idx[uCellsIdx[uCellsCounts>1]]							#Idx of cell fired multple times
			for i in range(mCellIdx.size):
				mCellI = mCellIdx[i]											#Loop on cells fired multiple times
				mCellT = sort(time[idx==mCellI])								#Times of events in the same cell
				delays = mCellT-mCellT[0]										#Delays of events consecutive to the first one (first delay returns 0)
				h = 1-exp(-delays/tfall)										#Calculate height of pulses (RC discharge circuit)
				h[0] = 1														#First pulse height is one
				evtTimes.append(mCellT)
				sigHtemp.append(h)
			evtTimes = hstack(evtTimes)											#Stack al times and heights of signals
			sigH = hstack(sigHtemp)
	else:
		evtTimes = np.empty(0)													#If signal has 0 pe and 0 dcr pass an empty array
		sigH = np.empty(0)
	return(np.array(evtTimes,dtype='int32'),np.array(sigH,dtype='float32'))

###GENERATION OF SIGNALS###
@numba.njit('(float32[:])(int32[:],float32,float32,float32,float32)',fastmath=True,nogil=True)
def signalShapeCPU(x,tfall,trise,ccgv,h):
	z = h*ccgv*(exp(-x/tfall)-exp(-x/trise))
	return(z)
#Signals are made with the two exponentials approximation and each peack height is smeared by a gaussian distribution (Cell to cell gain variation), each signals is also mutiplied by its height considering cell recovery time (h=1 if i's the firs event or less if the cell is fired multiple times)
@numba.njit('(float32[:])(int32,float32)',fastmath=True,nogil=True)
def PulseCPU(t,h):
	vect = (np.arange(sigpts,dtype=np.int32)-t)												#Generate matrix containing times of each fired cell (x of exponential function)
	vect[vect<0] = 0
	gainvar = np.float32(random.gauss(1,ccgv))																#Generate random ccgv for each fired cell
	s = signalShapeCPU(vect,tfall,trise,gainvar,h)										#Call kernel to generate singal
	nap = poisson(ap)																			#Generate number of afterpulses
	if nap>0:
		for i in range(nap):																		#If there are afterpulses generate theyr signals like the pe ones
			apdel = random.expovariate(1/tauapfast)+random.expovariate(1/tauapslow)						#APs have a time delay exponential distribution
			tap = np.int32(apdel/sampling+t)																#Each afterpulse has a delay from its "main" signal that follows a exp distribution
			hap = 1-exp(-apdel/tfall)
			vect = (np.arange(sigpts,dtype=np.int32)-tap)
			vect[vect<0] = 0
			s += signalShapeCPU(vect,tfall,trise,gainvar,hap)								#Add each afterpulse signal to main signal
	return(s)

###COUNTING PHOTONS AND ADDING NOISE TO SIGNALS###
@numba.njit('(float64[:])(int32[:],float32[:])',fastmath=True,nogil=True)
def signalGen(times,sigH):																		#Function that passes signals times and height to main function for generating signals
	baseline = random.gauss(0,basespread)														#Add a baseline to the signal (gaussian distribution)
	signal = np.random.normal(baseline,SNR,sigpts)
	for i in range(times.size):
		signal += PulseCPU(times[i],sigH[i])																	#Generate signals
	return(signal)

###SOME STATISCTICS AT END OF SCRIPT###
def somestats(integral,peak,tstart):
	plt.ioff()
	plt.subplot(2,2,1)
	plt.hist(integral,bins=750,histtype='step')
	plt.title('Integral')
	plt.subplot(2,2,2)
	plt.hist(peak,bins=750,histtype='step')
	plt.title('Peak')
	plt.subplot(2,2,3)
	bins = np.arange(tstart.min(),tstart.max())
	plt.hist(tstart,bins,histtype='step')
	plt.title('Starting time')
	plt.xlabel('Time [ns]')
	plt.subplot(2,2,4)
	plt.hist2d(integral,peak,bins=300)
	plt.title('Peak vs Integral')
	plt.show()

def sigPlot(signal,dev,sigTimes,dcrTime):
	current_core = psutil.Process().cpu_num()
	screenx = 1920; screeny = 1080;
	xsize = screenx/nJobs; ysize = xsize;
	xpos = current_core*xsize
	ypos = 0
	fig = plt.figure('Signals')
	manager = plt.get_current_fig_manager().window.setGeometry(xpos,ypos,xsize,ysize)
	ax = plt.gca()
	ax.hlines(-0.5,0,intstart*sampling,'r')
	ax.vlines(intstart*sampling,-0.5,-1,'r')
	ax.vlines((intstart-preg)*sampling,-0.5,-1,'r')
	ax.hlines(-1,intstart*sampling,(intstart+intgate)*sampling,'r')
	ax.vlines((intstart+intgate)*sampling,-1,-0.5,'r')
	ax.hlines(-0.5,(intstart+intgate)*sampling,siglen,'r')
	ax.grid(linestyle=':')

	titlestring = f"Signal generated on core {current_core:d} processed by {dev:s}.\n"
	titlestring += f"{sigTimes.size-dcrTime.size:d} Photons and {dcrTime.size:d} DCR events:\n"
	ax.set_title(titlestring)
	ax.set_xlabel('Time [ns]')
	ax.plot(np.arange(sigpts)*sampling,signal,'-b',linewidth=0.5)

	plt.draw()
	# plt.show()
	plt.pause(0.5)
	ax.lines[-1].remove()
	return

def initializeRandomPool():
	current_core = psutil.Process().cpu_num()
	time.sleep(random.random()/2)
	rngseed=struct.unpack('I',os.urandom(4))[0]+current_core
	random.seed(rngseed)
	np.random.seed(rngseed)
	core=multiprocessing.current_process().name
	print("Running simulation on %s with seed %d\r"%(core,rngseed))
	return()

###WRITING OUTPUT FILES###
def writefiles(integral,peak,tstart,filename,append):																#Function to save data in binary files format
	print('\nWriting on files...')																					## TODO: Save ROOT file
	S=time.time()
	fname='Output/'+filename
	if append:
		f = open(fname,'a')
		for i,j,k in zip(integral,peak,tstart):
			f.write("%f,%f,%f\n"%(i,j,k))
	else:
		f = open(fname,'w')
		for i,j,k in zip(integral,peak,tstart):
			f.write("%f,%f,%f\n"%(i,j,k))
	f.close()
	E=time.time()
	T=(E-S)*1000
	if args.verbosity:
		print('File '+filename+'.txt written in %.2fms...' %T)
	return()

output = []
def Callback(results):
	output.append((results))
