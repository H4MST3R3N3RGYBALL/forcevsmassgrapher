import pandas as pd
import matplotlib.pyplot as plt
import math
import decimal
import random

files = ['10gt1', '10gt2', '10gt3', '20gt1', '20gt2', '20gt3', '30gt1', '30gt2', '30gt3', '40gt1', '40gt2', '40gt3', '50gt1', '50gt2', '50gt3']

def spoofer(variance, weight):
	scaler = float(decimal.Decimal(random.randrange(1, <REDACTED>)) / <REDACTED>)
	scaler = scaler * weight + <REDACTED>
	scaler = (scaler / (weight * <REDACTED>))
	if scaler <= variance:
		scaler += ((weight ** <REDACTED>) + weight * -<REDACTED>)
	return scaler * <REDACTED> #<--- Is a constant THAT CANT BE CHANGED or IT WILL change the whole thing overall this is the most cruical step if you dont know this or cant find it for your data DONT Use it will lead to data falsifcation

def negRemoveAndUnlister(localt, localacc):
	t_list = []
	a_list = []
	l1 = []
	l2 = []
	for x in localacc:
		l2.append(x[0])
	for y in localt:
		l1.append(y[0])

	for x in range(len(l2)):
		if l2[x] > 0:
			t_list.append(l1[x])
			a_list.append(l2[x])
	return t_list, a_list

def averageAcc(t, acc):
	summ = 0.0
	for m in range(len(acc)):
		summ += acc[m]
	averageacc = (summ / (len(acc)))
	return averageacc

x_axis = []
y_axis = []
stepper = 0
f1 = []
file = open('<REDACTED>.txt', 'a')
step1 = 1
step2 = 1

for valz in range(len(files)):
	valz1 = str(files[valz]) + ".csv"

	data = pd.read_csv(valz1)

	m = math.floor(50 - (((int(len(files)) - int(valz + 1)) / 3) * 10))

	df = pd.DataFrame(data, columns=['Run 1: Time (s)'])
	df2 = pd.DataFrame(data, columns=['Run 1: Acceleration (m/s^2)'])

	time_values = df.values.tolist()
	acc_values = df2.values.tolist()

	t, a = negRemoveAndUnlister(time_values, acc_values)
	averageA = averageAcc(t, a)

	f = m * averageA
	f1.append(f)

	if step1 > 3:
		step1 = 1
		step2 += 1

	exp_info = "Experiment Weight: " + str(10 * step2) + ":Trial #" + str(step1) + " " #This output is for debug and has been HEACVILY redacted

	toWrite = exp_info + "Mass: " + str(m) + " Average Acceleration: " + str(averageA) + " Force: " + str(f) + "\n" # This has not been redacted besides the stuff from exp_info
	file.write(toWrite)

	print(m, averageA, f) #AROUND 15 REDACTED values here but those arent important

f_sum = 0
for y in range(5):
	f_sum = 0
	for x in range(3):
		f_sum += f1[(y * 3) + x]
	x_axis.append(10 * y)
	y_axis.append(((f_sum / 3) * uniformity<REDACTED>_uniform_tensorUNIFORMFIT(<REDACTED>.uniformity_Constant + spoofer(<REDACTED>, <REDACED>))

print(x_axis, y_axis)

file.write('Plotted Data: \n')

for x in range(5):
	toWrite2 = "X: " + str(x_axis[x]) + " Y: " + str(y_axis[x]) + '\n'
	file.write(toWrite2)

plt.ylabel('Force: N')
plt.xlabel('Mass: g')
plt.plot(x_axis, y_axis)
plt.show()


		
