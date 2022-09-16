import time

# Local time check
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

print()



# Checking Runtime of While Loop
initial = time.time()
k = 0
while(k<46):
	print(k,"This While Loop")
	k+=1
print("While Loop Run time: ",time.time()-initial)

print()

# Checking Runtime of forloop
initial2 = time.time()
for i in range(45):
	print(i,"This is For Loop")
	time.sleep(2) # it will sleep the print function everytime after printing
print("For Loop Running time: ",time.time()-initial2)
