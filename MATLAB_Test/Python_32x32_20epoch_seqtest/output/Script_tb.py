#Author - Luca Fiore

#this script is developed to organize data of weights and biases from files generated by 'Script_Weights&Biases.py'. In particular this script organize data in column. For each layer are developed others particular scripts to organize data in the right way for testing. 

import os

####### Variables to organize data for FC data in the correct way #########

N_MAC_FC1=24
N_MAC_FC2=21
N_MAC_FC3=10

INPUT_FC1=400
INPUT_FC2=120
INPUT_FC3=84

OUTPUT_FC1=120
OUTPUT_FC2=84
OUTPUT_FC3=10

#############################################################################


target_folder=["Bias","Weights"]
for fold in target_folder:
	folder="./" + fold + "/"
	list_file=os.listdir(folder)
	print(list_file)

	for file_ in list_file:
		namefile='./{0}_Column/Column'.format(fold) + file_
		try:		
			with open(namefile, "x") as file_output:
				with open(folder + file_, "r+") as file1:
					for line in file1:
						line=line.replace(' ', '')
						lista=line.split(',')
						if (fold == target_folder[1]): #if we are considering data of weights

							if (file_ == 'Weights_dense_1.txt'):
								#this lines if I want to put data in column and organize them with respect to the rights way for testbench because N_MAC is lower than output number of neurons
								for j in range(0,int(OUTPUT_FC1/N_MAC_FC1)): #da 0 a 4
									for k in range(0,INPUT_FC1): #da 0 a 399
										for i in range(0,N_MAC_FC1): # da 0 a 23
											file_output.write(lista[i+k*OUTPUT_FC1+j*N_MAC_FC1] + "\n")

							elif (file_ == 'Weights_dense_2.txt'):
								#this lines if I want to put data in column and organize them with respect to the rights way for testbench because N_MAC is lower than output number of neurons
								for j in range(0,int(OUTPUT_FC2/N_MAC_FC2)): #da 0 a 3
									for k in range(0,INPUT_FC2): #da 0 a 119
										for i in range(0,N_MAC_FC2): # da 0 a 20
											file_output.write(lista[i+k*OUTPUT_FC2+j*N_MAC_FC2] + "\n")
							else:
								#this two lines if I want only to put data in column
								for i in range(0,len(lista)): 
									file_output.write(lista[i] + "\n")

						else:
							#this two lines if I want only to put data in column
							for i in range(0,len(lista)): 
								file_output.write(lista[i] + "\n")

		except FileExistsError:
			print("File output already exists! Do you want to remove it? Y - N")
			ans=input()
			if (ans=='yes' or ans=='y' or ans=='Y'):
				os.system('rm ' + './{0}_Column/'.format(fold) + 'Column*')
				exit()
			else:						
				exit()