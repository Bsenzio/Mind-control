# BRAIN MODULE TESTER V 0.7
# UNIVERSITY OF THE RYUKYUS 2014
#   FACULTY OF ENGINEERING - IT DIVISION
#   YAMADA-KEN
#   AUTHOR: BRUNO SENZIO-SAVINO BARZELLATO
#   DATE: 25/08/2014

#Comments:
# Still missing performance-wise programming and custom peak generation and comparison

#Import libraries

import numpy as np
import matplotlib.pyplot as plt
import serial
import time
import winsound

#Predefined Pattern declaration
selected_pattern_1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
selected_expected=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
selected_peaks=0
selected_ramps=0
selected_ztimes=[0,0,0,0,0,0]
selected_threshold=80
expected_threshold=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
graph_threshold=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

R=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Predefined thresholds
top=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100];

#Pattern A

pattern_a=[10,10,10,10,10,10,10,10,10,10,50,50,50,50,50,90,90,90,90,90,90,90,50,50,50,50,50,10,10,10,10,10,10];
expected_a=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
peaks_a=1
ramps_a=0
zeroes_a=[16,22,0,0,0,0]

#Pattern B

pattern_b=[10,50,50,50,50,50,90,90,90,90,90,90,90,90,50,50,50,50,50,50,50,90,90,90,90,90,90,90,50,50,50,50,10];
expected_b=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
peaks_b=2
ramps_b=0
zeroes_b=[7,14,22,28,0,0]

#Pattern C

pattern_c=[10,50,50,50,90,90,90,90,90,50,50,50,50,90,90,90,90,90,90,50,50,50,90,90,90,90,90,50,50,50,50,50,10];
expected_c=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0];
peaks_c=3
ramps_c=0
zeroes_c=[5,9,15,19,23,27]

#Pattern D
 
pattern_d=[10,10,10,10,10,10,10,10,10,10,50,50,50,50,90,90,90,90,90,90,90,90,50,50,50,50,50,10,10,10,10,10,10];
expected_d=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
peaks_d=1
ramps_d=0
zeroes_d=[15,19,0,0,0,0]

#Pattern E

pattern_e=[10,50,50,50,50,50,90,90,90,90,90,90,90,90,60,60,50,50,50,60,60,90,90,90,90,90,90,90,50,50,50,50,10];
expected_e=[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
peaks_e=2
ramps_e=0
zeroes_e=[8,14,22,28,0,0]

#Pattern F

pattern_f=[10,10,20,20,30,30,40,40,50,50,60,60,70,70,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90];
expected_f=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
peaks_f=0
ramps_f=1
zeroes_f=[17,0,0,0,0,0]

#Combined pattern examples

#Pattern G (A for meditation//B for attention)

pattern_g_a=[10,50,50,50,50,50,90,90,90,90,90,90,50,50,50,50,50,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10];
expected_g_a=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
pattern_g_b=[10,10,20,20,30,30,40,40,50,50,60,60,70,70,79,79,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90];
expected_g_b=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];

#Pattern H

pattern_h_a=[10,50,50,50,50,50,90,90,90,90,90,90,90,90,50,50,50,50,50,50,50,90,90,90,90,90,90,90,50,50,50,50,10];
expected_h_a=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
pattern_h_b=[10,50,50,50,50,50,90,90,90,90,90,90,90,90,50,50,50,50,50,50,50,90,90,90,90,90,90,90,50,50,50,50,10];
expected_h_b=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0];

#Pattern I

pattern_i_a=[10,50,50,50,50,50,90,90,90,90,90,90,90,90,50,50,50,50,50,50,50,90,90,90,90,90,90,90,50,50,50,50,10];
expected_i_a=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
pattern_i_b=[10,50,50,50,50,50,90,90,90,90,90,90,90,90,50,50,50,50,50,50,50,90,90,90,90,90,90,90,50,50,50,50,10];
expected_i_a=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0];


#Creating the pattern reading matrix
trace=range(33)
timers=range(33)

#Initializing the trace pattern
for i in range(33):
	trace[i]=0

#Option selection
	
option = raw_input("Please choose an option: \n(1)Attention pattern \n(2)Meditation pattern \n(3)Mixed pattern \n")	
clear=0

if option=='1':
    mode = raw_input("What kind of pattern?(a~c)\n")
    if mode=='a':
        selected_pattern = pattern_a
        selected_peaks=peaks_a
        selected_ramps=ramps_a
        selected_ztimes=zeroes_a
        selected_expected=expected_a
    elif mode=='b':
        selected_pattern = pattern_b
        selected_peaks=peaks_b
        selected_ramps=ramps_b
        selected_ztimes=zeroes_b
        selected_expected=expected_b
    elif mode=='c':
        selected_pattern = pattern_c
        selected_peaks=peaks_c
        selected_ramps=ramps_c
        selected_ztimes=zeroes_c
        selected_expected=expected_c
    else:
        clear=1
        print("That is not a valid option, please enter a valid option\n");
elif option=='2':
    mode = raw_input("What kind of pattern?(d~f)\n")
    if mode=='d':
        selected_pattern = pattern_d
        selected_peaks=peaks_d
        selected_ramps=ramps_d
        selected_ztimes=zeroes_d
        selected_expected=expected_d
    elif mode=='e':
        selected_pattern = pattern_e
        selected_peaks=peaks_e
        selected_ramps=ramps_e
        selected_ztimes=zeroes_e
        selected_expected=expected_e
    elif mode=='f':
        selected_pattern = pattern_f
        selected_peaks=peaks_f
        selected_ramps=ramps_f
        selected_ztimes=zeroes_f
        selected_expected=expected_f
    else:
        clear=1
        print("That is not a valid option, please enter a valid option\n");
elif option=='3':
    mode = raw_input("What kind of pattern?(g~i)\n")
    if mode=='g':
        selected_pattern = pattern_g_a
        selected_pattern_1 = pattern_g_b
    elif mode=='h':
        selected_pattern = pattern_h_a
        selected_pattern_1 = pattern_h_b
    elif mode=='i':
        selected_pattern = pattern_i_a
        selected_pattern_1 = pattern_h_b
    else:
        clear=1
        print("That is not a valid option, please enter a valid option\n");
else:
        clear=1
        print("That is not a valid option, please enter a valid option\n");

if clear==0:
        selected_threshold=int(raw_input("Please enter a threshold value(1~99)"))
        for x in range(33):
                graph_threshold[x]=selected_threshold*graph_threshold[x]
        print("Please take a look at the plot and close when ready...\n");
        plt.plot(timers,selected_pattern,'b',selected_pattern_1,'r',graph_threshold,'b--',top,'b--')
        plt.show()
        correct = raw_input("Is this correct?(y/n)")
        if correct=='y':

                #trace=[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0];
                trace=     [12,20,20,45,55,34,26,70,87,54,20,18,25,30,40,50,72,86,15,79,45,35,70,81,80,76,15,23,35,57,60,70,56];
                #Wait for key to be pressed in order to continue
                raw_input("PUT HELMET AND PRESS ENTER WHEN READY...")

                #Define serial port

                ser = serial.Serial('COM4',9600)

                for i in range(33):
                        trace[i]=int(ser.readline())
                        print trace[i]

                plt.plot(timers,selected_pattern,'b',trace,'g',graph_threshold,'b--',top,'b--')
                plt.show()
                
                for x in range(33):
                    expected_threshold[x]=selected_threshold*selected_expected[x]

                for x in range(33):
                    R[x]=trace[x]-expected_threshold[x]
                    if R[x]==trace[x] and R[x]>=80:
                        R[x]=1
                    if R[x]==trace[x] or R[x]<0:
                        R[x]=0
                    if R[x]>0:
                        R[x]=1
                        
                trace=R
                print(trace)
                print(R)
                
                number_of_zeroes=2*selected_peaks
                wrong=0
                looking_for_peaks=-1
                for i in range(number_of_zeroes+1):
                    correct=1
                    peak=0
                    if i==0:
                        for a in range(selected_ztimes[0]):
                            if trace[a]!=0:
                                correct=0
                                wrong=1
                                break
                    if i>0 and i<number_of_zeroes:
                        a=selected_ztimes[i-1]
                        looking_for_peaks=(-1)**i
                        while a<selected_ztimes[i]:
                            if looking_for_peaks==1:
                                if trace[a]!=0:
                                    correct=0
                            elif looking_for_peaks==-1:
                                if trace[a]==1:
                                    peak=1
                            a+=1
                        if peak!=1 and looking_for_peaks==-1:
                            correct=0
                            wrong=1
                            break
                        if correct==0:
                            wrong=1
                            break
                    if i==number_of_zeroes:
                        a=selected_ztimes[i-1]
                        while a<33:
                            if trace[a]!=0:
                                correct=0
                                wrong=1
                                break
                            a+=1


                print("Wrong:")
                print(wrong)
                print(trace)
                
                
                
        elif correct=='n':
                print("Please restart program and make sure to select the right option\n");
