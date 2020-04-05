from main import *

pool = Pool(processes=4,initializer=initializeRandomPool)
nEvt = 10000
nPe = 25
t = time.time()
for i in range(nEvt):
    timein = np.ones(np.random.poisson(nPe))*40
    pool.apply_async(SiPM,args=(timein,[]),callback=Callback)
    #output.append(SiPM(timein,[]))
pool.close()
pool.join()
T = time.time()
print(nEvt/(T-t))

output = np.array(output)

integral = output[:,0]
peak = output[:,1]
tstart = output[:,2]

if args.graphics:
    somestats(integral,peak,tstart)

# filename = "Test.txt"
# np.savetxt(filename,(integral,peak,tstart),delimiter='\t')
