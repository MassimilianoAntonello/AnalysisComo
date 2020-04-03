import ROOT
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from terminaltables import SingleTable
from MyFunctions import legstyle, plotstyle
os.system('clear')
plotstyle('Aroot')
#############################################################
def tableCreator(effS,effB,submetodName):
	effS=np.array([i for i in effS][1::])
	effB=np.array([i for i in effB][1::])
	x=np.linspace(0,1,len(effS))

	for i,val in enumerate(effS):
		if val<=0.999:
			idx999=i
			cut999=val
			break
	for i,val in enumerate(effS):
		if val<=0.998:
			idx998=i
			cut998=val
			break
	for i,val in enumerate(effS):
		if val<=0.995:
			idx995=i
			cut995=val
			break
	for i,val in enumerate(effS):
		if val<=0.99:
			idx99=i
			cut99=val
			break
	for i,val in enumerate(effS):
		if val<=0.985:
			idx985=i
			cut985=val
			break
	for i,val in enumerate(effS):
		if val<=0.98:
			idx98=i
			cut98=val
			break
	for i,val in enumerate(effS):
		if val<=0.95:
			idx95=i
			cut95=val
			break

	effS999=effS[idx999]
	effS998=effS[idx998]
	effS995=effS[idx995]
	effS99=effS[idx99]
	effS985=effS[idx985]
	effS98=effS[idx98]
	effS95=effS[idx95]

	effB999=effB[idx999]
	effB998=effB[idx998]
	effB995=effB[idx995]
	effB99=effB[idx99]
	effB985=effB[idx985]
	effB98=effB[idx98]
	effB95=effB[idx95]

	cut999=x[idx999]
	cut998=x[idx998]
	cut995=x[idx995]
	cut99=x[idx99]
	cut985=x[idx985]
	cut98=x[idx98]
	cut95=x[idx95]

	effSB=effS/np.sqrt(effS+effB)

	bestcutIdx=np.nanargmax(effSB)
	besteffS=effS[bestcutIdx]
	besteffB=effB[bestcutIdx]
	bestcut=x[bestcutIdx]
	cuts=[cut999,cut998,cut995,cut99,cut985,cut98,cut95]

	purity = effS/(effS+effB)
	rej = effS/effB

	table=[['Signal Efficieny:','Purity','Rejection:','Cutting @:'],
	['{:.1f}'.format(effS999*100)+'%','{:.1f}'.format(100*effS999/(effS999+effB999))+'%','{:.1f}'.format(100/(effS999/effB999))+'%','{:.4f}'.format(cut999)],
	['{:.1f}'.format(effS998*100)+'%','{:.1f}'.format(100*effS998/(effS998+effB998))+'%','{:.1f}'.format(100/(effS998/effB998))+'%','{:.4f}'.format(cut998)],
	['{:.1f}'.format(effS995*100)+'%','{:.1f}'.format(100*effS995/(effS995+effB995))+'%','{:.1f}'.format(100/(effS995/effB995))+'%','{:.4f}'.format(cut995)],
	['{:.1f}'.format(effS99*100)+'%','{:.1f}'.format(100*effS99/(effS99+effB99))+'%','{:.1f}'.format(100/(effS99/effB99))+'%','{:.4f}'.format(cut99)],
	['{:.1f}'.format(effS985*100)+'%','{:.1f}'.format(100*effS985/(effS985+effB985))+'%','{:.1f}'.format(100/(effS985/effB985))+'%','{:.4f}'.format(cut985)],
	['{:.1f}'.format(effS98*100)+'%','{:.1f}'.format(100*effS98/(effS98+effB98))+'%','{:.1f}'.format(100/(effS98/effB98))+'%','{:.4f}'.format(cut98)],
	['{:.1f}'.format(effS95*100)+'%','{:.1f}'.format(100*effS95/(effS95+effB95))+'%','{:.1f}'.format(100/(effS95/effB95))+'%','{:.4f}'.format(cut95)],
	['{:.2f}'.format(besteffS*100)+'%','{:.2f}'.format(100*besteffS/(besteffS+besteffB))+'%','{:.2f}'.format(100/(besteffS/besteffB))+'%','{:.4f}'.format(bestcut)]]

	table=SingleTable(table,submetodName)
	print(table.table)
	print('Best cut value @: %.4f with signal efficiency of %.1f%% and background rejection of %.1f%%'%(bestcut,besteffS*100,100-besteffB*100))
	plt.figure()
	plt.title('Signal efficiency and purity')
	# for i in cuts:
	# 	plt.plot([i,i],[0,1],'--k',linewidth=0.5,)
	plt.hlines(0.99,0,x[-1],'k',label='99\%')
	plt.plot(x,effS,'-r',label='Efficiency',linewidth=1)
	plt.plot(x,purity,'-b',label='Purity',linewidth=1)
	#plt.plot(x,rej,'-y',label='Rejection',linewidth=1)
	plt.ylim(0.94,1.02)
	plt.xlabel('Cut')
	legstyle()
##################################################################################
inputFile = ROOT.TFile.Open(sys.argv[1])
if 'PY' in sys.argv[1]:
	dataset=inputFile.Get("datasetPY")
if 'CPP' in sys.argv[1]:
	dataset=inputFile.Get("datasetCPP")

ListOfKeys=dataset.GetListOfKeys()
for i in ListOfKeys:
	if 'Method' in i.GetName():
		print('Found: %s'%i.GetName())
methodName="TMlpANN"
submetodName="TMlpANN"
MLPMethod=dataset.Get("Method_"+methodName)
MLPBFGSMethod=MLPMethod.Get(submetodName)
effS=MLPBFGSMethod.Get("MVA_"+submetodName+"_effS")
effB=MLPBFGSMethod.Get("MVA_"+submetodName+"_effB")
tableCreator(effS,effB,submetodName)

#plt.show()

inputFile = ROOT.TFile.Open(sys.argv[1])
if 'PY' in sys.argv[1]:
	dataset=inputFile.Get("datasetPY")
if 'CPP' in sys.argv[1]:
	dataset=inputFile.Get("datasetCPP")

ListOfKeys=dataset.GetListOfKeys()
for i in ListOfKeys:
	if 'Method' in i.GetName():
		print('Found: %s'%i.GetName())
methodName="MLP"
submetodName="MLPBFGS"
MLPMethod=dataset.Get("Method_"+methodName)
MLPBFGSMethod=MLPMethod.Get(submetodName)
effS=MLPBFGSMethod.Get("MVA_"+submetodName+"_effS")
effB=MLPBFGSMethod.Get("MVA_"+submetodName+"_effB")
tableCreator(effS,effB,submetodName)

#plt.show()
