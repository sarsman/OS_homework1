import random					#by 資網四B D1004342054 劉定岳
import os

Ram1 =[random.randint(0,5)*1024,random.randint(10,30)*1024]
Ram2 =[Ram1[0]+Ram1[1]+random.randint(0,5),random.randint(10,30)*1024]
Ram3 =[Ram2[0]+Ram2[1]+random.randint(0,5),random.randint(10,30)*1024]
Ram4 =[Ram3[0]+Ram3[1]+random.randint(0,5),random.randint(10,30)*1024]
Ram5 =[Ram4[0]+Ram4[1]+random.randint(0,5),random.randint(10,30)*1024]
Stop = 0
HowMany = 0
Job = []
def show():
	print("起始位置\t區塊大小")
	print("%s\t\t%s" % (Ram1[0],Ram1[1]))
	print("%s\t\t%s" % (Ram2[0],Ram2[1]))
	print("%s\t\t%s" % (Ram3[0],Ram3[1]))
	print("%s\t\t%s" % (Ram4[0],Ram4[1]))
	print("%s\t\t%s" % (Ram5[0],Ram5[1]))
show()

HowMany = int(input("欲創造多少個Job?"))
for x in range(HowMany):
	Job.append(int(input("請輸入Job%s：" % (x+1) )))
print(Job)

HowToDo = input("如何配置？best、first、worst：")

def Best():
	print("--使用最適配置法--")
	for x in Job:
		Compare = {}
		Compare.update({'Ram1':Ram1[1]-x})
		Compare.update({'Ram2':Ram2[1]-x})
		Compare.update({'Ram3':Ram3[1]-x})
		Compare.update({'Ram4':Ram4[1]-x})
		Compare.update({'Ram5':Ram5[1]-x})
		small = (min(Compare.items(), key=lambda x: x[1]))
		over=0
		while(over==0):
			if(small[1] < 0):
				del Compare[small[0]]
				try:
					small = (min(Compare.items(), key=lambda x: x[1]))
				except:
					show()
					print("記憶體空間不足，無法配置！")
					os.system("pause")
					quit()
			else:
				over+=1
		print("%s放入%s,剩餘空間%d" % (x,small[0],small[1]))
		exec("%s[0] += %d" % (small[0],x))
		exec("%s[1] -= %d" % (small[0],x))
	show()
	return

def First():
	print("--使用先適配置法--")
	Ram = [Ram1,Ram2,Ram3,Ram4,Ram5]
	RamName = ["Ram1","Ram2","Ram3","Ram4","Ram5"]
	for x in Job:
		#big = (max(Compare.items(), key=lambda x: x[1]))
		count = 0
		for y in Ram:
			if(y[1]>x):
				y[1]-=x
				y[0]+=x
				print("%s放入%s,剩餘空間%d" % (x,RamName[count],y[1]))
				break
			else:
				count+=1
	show()
	return("First")

def Worst():
	print("--使用最不適配置法--")
	for x in Job:
		Compare = {}
		Compare.update({'Ram1':Ram1[1]-x})
		Compare.update({'Ram2':Ram2[1]-x})
		Compare.update({'Ram3':Ram3[1]-x})
		Compare.update({'Ram4':Ram4[1]-x})
		Compare.update({'Ram5':Ram5[1]-x})
		big = (max(Compare.items(), key=lambda x: x[1]))
		over=0
		while(over==0):
			if(big[1] < 0):
				del Compare[big[0]]
				try:
					big = (max(Compare.items(), key=lambda x: x[1]))
				except:
					show()
					print("記憶體空間不足，無法配置！")
					os.system("pause")
					quit()
			else:
				over+=1
		print("%s放入%s,剩餘空間%d" % (x,big[0],big[1]))
		exec("%s[0] += %d" % (big[0],x))
		exec("%s[1] -= %d" % (big[0],x))
	show()
	return("Worst")

if(HowToDo=="best"):
	Best()
elif(HowToDo=="first"):
	First()
elif(HowToDo=="worst"):
	Worst()

os.system("pause")