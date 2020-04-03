from main import *

pool = Pool(processes=4,initializer=initializeRandomPool)
nEvt = 1000
nPe = 5
t = time.time()
for i in range(nEvt):
    timein = np.ones(np.random.poisson(nPe))*30
    pool.apply_async(SiPM,args=(timein,[]),callback=Callback)
    # SiPM(timein,[])
pool.close()
pool.join()
T = time.time()
print(nEvt/(T-t))

output = np.ascontiguousarray(output)

integral = output[:,0]
peak = output[:,1]
tstart = output[:,2]

if args.graphics:
    somestats(integral,peak,tstart)

# filename = "Test.txt"
# np.savetxt(filename,(integral,peak,tstart),delimiter='\t')
