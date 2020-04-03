#include "datasetCPP/weights/TMVAClassification_TMlpANN.h"
#include <cmath>

double TMVAClassification_TMlpANN::Value(int index,double in0,double in1,double in2) {
   input0 = (in0 - 0.889087)/0.139402;
   input1 = (in1 - 3182.38)/9.43608;
   input2 = (in2 - 2.57786)/1.78959;
   switch(index) {
     case 0:
         return neuron0x55c42966f130();
     default:
         return 0.;
   }
}

double TMVAClassification_TMlpANN::Value(int index, double* input) {
   input0 = (input[0] - 0.889087)/0.139402;
   input1 = (input[1] - 3182.38)/9.43608;
   input2 = (input[2] - 2.57786)/1.78959;
   switch(index) {
     case 0:
         return neuron0x55c42966f130();
     default:
         return 0.;
   }
}

double TMVAClassification_TMlpANN::neuron0x55c4283f29c0() {
   return input0;
}

double TMVAClassification_TMlpANN::neuron0x55c428920140() {
   return input1;
}

double TMVAClassification_TMlpANN::neuron0x55c42809e7f0() {
   return input2;
}

double TMVAClassification_TMlpANN::input0x55c4260e1390() {
   double input = -0.237927;
   input += synapse0x55c42960b6a0();
   input += synapse0x55c42960b6e0();
   input += synapse0x55c42964cd10();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4260e1390() {
   double input = input0x55c4260e1390();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c42867f020() {
   double input = 4.75241;
   input += synapse0x55c42960d500();
   input += synapse0x55c42960d540();
   input += synapse0x55c42960d580();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c42867f020() {
   double input = input0x55c42867f020();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c42709ae40() {
   double input = -1.28658;
   input += synapse0x55c42960d770();
   input += synapse0x55c42960d7b0();
   input += synapse0x55c42960d7f0();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c42709ae40() {
   double input = input0x55c42709ae40();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c426e7e320() {
   double input = -0.188593;
   input += synapse0x55c42960cec0();
   input += synapse0x55c42960cf00();
   input += synapse0x55c42960cf40();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c426e7e320() {
   double input = input0x55c426e7e320();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c42960cf80() {
   double input = -1.31403;
   input += synapse0x55c4296450b0();
   input += synapse0x55c4296450f0();
   input += synapse0x55c429645130();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c42960cf80() {
   double input = input0x55c42960cf80();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c429645170() {
   double input = -2.29128;
   input += synapse0x55c4296454b0();
   input += synapse0x55c4296454f0();
   input += synapse0x55c429645530();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c429645170() {
   double input = input0x55c429645170();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4295377e0() {
   double input = -2.45329;
   input += synapse0x55c429537a90();
   input += synapse0x55c429537ad0();
   input += synapse0x55c429537b10();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4295377e0() {
   double input = input0x55c4295377e0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c429537b50() {
   double input = -3.66015;
   input += synapse0x55c429537e90();
   input += synapse0x55c429537ed0();
   input += synapse0x55c429537f10();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c429537b50() {
   double input = input0x55c429537b50();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a0ac0() {
   double input = -0.00372647;
   input += synapse0x55c4296a0e00();
   input += synapse0x55c4296a0e40();
   input += synapse0x55c4296a0e80();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a0ac0() {
   double input = input0x55c4296a0ac0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a0ec0() {
   double input = 0.172043;
   input += synapse0x55c4296a1200();
   input += synapse0x55c4296a1240();
   input += synapse0x55c4296a1280();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a0ec0() {
   double input = input0x55c4296a0ec0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a12c0() {
   double input = -1.08113;
   input += synapse0x55c4296a1600();
   input += synapse0x55c4296a1640();
   input += synapse0x55c4296a1680();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a12c0() {
   double input = input0x55c4296a12c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a16c0() {
   double input = 6.41424;
   input += synapse0x55c4296a1a00();
   input += synapse0x55c4296a1a40();
   input += synapse0x55c4296a1a80();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a16c0() {
   double input = input0x55c4296a16c0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a1ac0() {
   double input = 0.941695;
   input += synapse0x55c4296a1e00();
   input += synapse0x55c4296a1e40();
   input += synapse0x55c4296a1e80();
   input += synapse0x55c4296a1ec0();
   input += synapse0x55c4296a1f00();
   input += synapse0x55c4296a1f40();
   input += synapse0x55c4296a1f80();
   input += synapse0x55c4296a1fc0();
   input += synapse0x55c4296a2000();
   input += synapse0x55c4296a2040();
   input += synapse0x55c4296a2080();
   input += synapse0x55c4296a20c0();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a1ac0() {
   double input = input0x55c4296a1ac0();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a2100() {
   double input = -1.73341;
   input += synapse0x55c4296a2440();
   input += synapse0x55c4296a2480();
   input += synapse0x55c4296a24c0();
   input += synapse0x55c4296a2500();
   input += synapse0x55c4296a2540();
   input += synapse0x55c4296a2580();
   input += synapse0x55c4296a25c0();
   input += synapse0x55c4296a2600();
   input += synapse0x55c4296a2640();
   input += synapse0x55c4296a2680();
   input += synapse0x55c4296a26c0();
   input += synapse0x55c4296a2700();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a2100() {
   double input = input0x55c4296a2100();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c4296a2740() {
   double input = 2.23453;
   input += synapse0x55c4296a29f0();
   input += synapse0x55c4296a2a30();
   input += synapse0x55c4296a2a70();
   input += synapse0x55c4296a2ab0();
   input += synapse0x55c4296a2af0();
   input += synapse0x55c4296a2b30();
   input += synapse0x55c4296a2b70();
   input += synapse0x55c4296a2bb0();
   input += synapse0x55c4296a2bf0();
   input += synapse0x55c4296a2c30();
   input += synapse0x55c4296a2c70();
   input += synapse0x55c4296a2cb0();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c4296a2740() {
   double input = input0x55c4296a2740();
   return ((input < -709. ? 0. : (1/(1+exp(-input)))) * 1)+0;
}

double TMVAClassification_TMlpANN::input0x55c42966f130() {
   double input = -0.531496;
   input += synapse0x55c42966f470();
   input += synapse0x55c42966f4b0();
   input += synapse0x55c42966f4f0();
   return input;
}

double TMVAClassification_TMlpANN::neuron0x55c42966f130() {
   double input = input0x55c42966f130();
   return (input * 1)+0;
}

double TMVAClassification_TMlpANN::synapse0x55c42960b6a0() {
   return (neuron0x55c4283f29c0()*-5.76466);
}

double TMVAClassification_TMlpANN::synapse0x55c42960b6e0() {
   return (neuron0x55c428920140()*-4.66894);
}

double TMVAClassification_TMlpANN::synapse0x55c42964cd10() {
   return (neuron0x55c42809e7f0()*4.89108);
}

double TMVAClassification_TMlpANN::synapse0x55c42960d500() {
   return (neuron0x55c4283f29c0()*-1.26919);
}

double TMVAClassification_TMlpANN::synapse0x55c42960d540() {
   return (neuron0x55c428920140()*-3.61572);
}

double TMVAClassification_TMlpANN::synapse0x55c42960d580() {
   return (neuron0x55c42809e7f0()*4.17276);
}

double TMVAClassification_TMlpANN::synapse0x55c42960d770() {
   return (neuron0x55c4283f29c0()*-4.46692);
}

double TMVAClassification_TMlpANN::synapse0x55c42960d7b0() {
   return (neuron0x55c428920140()*-3.58085);
}

double TMVAClassification_TMlpANN::synapse0x55c42960d7f0() {
   return (neuron0x55c42809e7f0()*4.05986);
}

double TMVAClassification_TMlpANN::synapse0x55c42960cec0() {
   return (neuron0x55c4283f29c0()*1.62581);
}

double TMVAClassification_TMlpANN::synapse0x55c42960cf00() {
   return (neuron0x55c428920140()*1.20388);
}

double TMVAClassification_TMlpANN::synapse0x55c42960cf40() {
   return (neuron0x55c42809e7f0()*-1.88755);
}

double TMVAClassification_TMlpANN::synapse0x55c4296450b0() {
   return (neuron0x55c4283f29c0()*-3.8795);
}

double TMVAClassification_TMlpANN::synapse0x55c4296450f0() {
   return (neuron0x55c428920140()*-3.39516);
}

double TMVAClassification_TMlpANN::synapse0x55c429645130() {
   return (neuron0x55c42809e7f0()*3.33379);
}

double TMVAClassification_TMlpANN::synapse0x55c4296454b0() {
   return (neuron0x55c4283f29c0()*-0.696104);
}

double TMVAClassification_TMlpANN::synapse0x55c4296454f0() {
   return (neuron0x55c428920140()*7.79162);
}

double TMVAClassification_TMlpANN::synapse0x55c429645530() {
   return (neuron0x55c42809e7f0()*-0.740856);
}

double TMVAClassification_TMlpANN::synapse0x55c429537a90() {
   return (neuron0x55c4283f29c0()*2.93316);
}

double TMVAClassification_TMlpANN::synapse0x55c429537ad0() {
   return (neuron0x55c428920140()*3.79774);
}

double TMVAClassification_TMlpANN::synapse0x55c429537b10() {
   return (neuron0x55c42809e7f0()*-4.27836);
}

double TMVAClassification_TMlpANN::synapse0x55c429537e90() {
   return (neuron0x55c4283f29c0()*0.752454);
}

double TMVAClassification_TMlpANN::synapse0x55c429537ed0() {
   return (neuron0x55c428920140()*3.59721);
}

double TMVAClassification_TMlpANN::synapse0x55c429537f10() {
   return (neuron0x55c42809e7f0()*-8.25464);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a0e00() {
   return (neuron0x55c4283f29c0()*2.23272);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a0e40() {
   return (neuron0x55c428920140()*2.18872);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a0e80() {
   return (neuron0x55c42809e7f0()*-2.06189);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1200() {
   return (neuron0x55c4283f29c0()*4.54017);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1240() {
   return (neuron0x55c428920140()*4.43861);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1280() {
   return (neuron0x55c42809e7f0()*-4.18632);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1600() {
   return (neuron0x55c4283f29c0()*4.92843);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1640() {
   return (neuron0x55c428920140()*4.31956);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1680() {
   return (neuron0x55c42809e7f0()*-4.96681);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1a00() {
   return (neuron0x55c4283f29c0()*1.60071);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1a40() {
   return (neuron0x55c428920140()*-4.65056);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1a80() {
   return (neuron0x55c42809e7f0()*9.99288);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1e00() {
   return (neuron0x55c4260e1390()*-1.47354);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1e40() {
   return (neuron0x55c42867f020()*4.02312);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1e80() {
   return (neuron0x55c42709ae40()*-1.98603);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1ec0() {
   return (neuron0x55c426e7e320()*0.521752);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1f00() {
   return (neuron0x55c42960cf80()*-2.85416);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1f40() {
   return (neuron0x55c429645170()*2.44664);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1f80() {
   return (neuron0x55c4295377e0()*-2.26507);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a1fc0() {
   return (neuron0x55c429537b50()*-2.6938);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2000() {
   return (neuron0x55c4296a0ac0()*-0.414815);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2040() {
   return (neuron0x55c4296a0ec0()*2.71757);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2080() {
   return (neuron0x55c4296a12c0()*0.438412);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a20c0() {
   return (neuron0x55c4296a16c0()*6.42281);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2440() {
   return (neuron0x55c4260e1390()*1.71277);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2480() {
   return (neuron0x55c42867f020()*-6.49112);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a24c0() {
   return (neuron0x55c42709ae40()*3.20477);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2500() {
   return (neuron0x55c426e7e320()*-1.4776);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2540() {
   return (neuron0x55c42960cf80()*4.22092);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2580() {
   return (neuron0x55c429645170()*-5.22862);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a25c0() {
   return (neuron0x55c4295377e0()*4.31194);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2600() {
   return (neuron0x55c429537b50()*7.40509);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2640() {
   return (neuron0x55c4296a0ac0()*-0.26992);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2680() {
   return (neuron0x55c4296a0ec0()*-1.90887);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a26c0() {
   return (neuron0x55c4296a12c0()*1.76431);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2700() {
   return (neuron0x55c4296a16c0()*-11.5402);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a29f0() {
   return (neuron0x55c4260e1390()*-0.322193);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2a30() {
   return (neuron0x55c42867f020()*2.69714);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2a70() {
   return (neuron0x55c42709ae40()*-1.24998);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2ab0() {
   return (neuron0x55c426e7e320()*1.15838);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2af0() {
   return (neuron0x55c42960cf80()*-1.5994);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2b30() {
   return (neuron0x55c429645170()*3.87224);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2b70() {
   return (neuron0x55c4295377e0()*-1.41501);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2bb0() {
   return (neuron0x55c429537b50()*-3.10258);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2bf0() {
   return (neuron0x55c4296a0ac0()*0.137388);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2c30() {
   return (neuron0x55c4296a0ec0()*1.50184);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2c70() {
   return (neuron0x55c4296a12c0()*-0.331856);
}

double TMVAClassification_TMlpANN::synapse0x55c4296a2cb0() {
   return (neuron0x55c4296a16c0()*5.21882);
}

double TMVAClassification_TMlpANN::synapse0x55c42966f470() {
   return (neuron0x55c4296a1ac0()*1.87248);
}

double TMVAClassification_TMlpANN::synapse0x55c42966f4b0() {
   return (neuron0x55c4296a2100()*1.30303);
}

double TMVAClassification_TMlpANN::synapse0x55c42966f4f0() {
   return (neuron0x55c4296a2740()*-1.32966);
}

