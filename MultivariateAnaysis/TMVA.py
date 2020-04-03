from ROOT import TMVA, TFile, TTree, TCut, TString
import ROOT

ROOT.ROOT.EnableImplicitMT(4)
TMVA.Tools.Instance()

inputFile = TFile.Open("inputdata.root")
outputFile = TFile.Open("TMVAOutputPY.root", "RECREATE")

factory = TMVA.Factory("TMVAClassification", outputFile, "Color:DrawProgressBar:AnalysisType=Classification" )
loader = TMVA.DataLoader("datasetPY")

loader.AddVariable("cs")
loader.AddVariable("tstart")
loader.AddVariable("r95")

# tbackground = inputFile.Get("Electrons")
# tsignal = inputFile.Get("Pions")

tbackground = inputFile.Get("Pions")
tsignal = inputFile.Get("Electrons")

loader.AddSignalTree(tsignal)
loader.AddBackgroundTree(tbackground)
loader.PrepareTrainingAndTestTree(TCut("r95>=0"),
        "nTrain_Signal=2000:nTrain_Background=2000:SplitMode=Random:NormMode=NumEvents:V")

# General layout
layoutString = TString("Layout=TANH|128,TANH|128,TANH|128,LINEAR");

# Training strategies
training0 = TString("LearningRate=1e-1,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=2,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.5+0.5+0.5, Multithreading=True")
training1 = TString("LearningRate=1e-3,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=2,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.0+0.0+0.0, Multithreading=True")
trainingStrategyString = TString("TrainingStrategy=")
trainingStrategyString += training0 + TString("|") + training1

# General Options
dnnOptions = TString("!H:!V:ErrorStrategy=CROSSENTROPY:VarTransform=N:"
        "WeightInitialization=XAVIERUNIFORM")
dnnOptions.Append(":")
dnnOptions.Append(layoutString)
dnnOptions.Append(":")
dnnOptions.Append(trainingStrategyString)

# Standard implementation, no dependencies.
stdOptions =  dnnOptions + ":Architecture=GPU"
factory.BookMethod(loader, TMVA.Types.kDNN, "DNN", stdOptions)

kLikOptions = TString("TransformOutput:PDFInterpol=Spline3:NSmoothSig[0]=10:NSmoothBkg[0]=10:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=75")
factory.BookMethod(loader, TMVA.Types.kLikelihood, "kLikelihood", kLikOptions)

kBdOptions= TString("NTrees=2500:MinNodeSize=5%:MaxDepth=9:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")
factory.BookMethod(loader, TMVA.Types.kBDT, "kBoostedDecision", kBdOptions)

factory.BookMethod(loader,TMVA.Types.kMLP,"MLPBFGS","H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:!UseRegulator" )

factory.BookMethod(loader, TMVA.Types.kSVM, "SVM", "Gamma=0.25:Tol=0.001:VarTransform=Norm");

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

outputFile.Close()
TMVA.TMVAGui('TMVAOutputPY.root')
input()
