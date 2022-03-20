import numpy as np
import matplotlib.pyplot as plt
arr = []
input=int(input("Enter number here:"))
arr.append(input)
label_num=input
while True:
    if input!=1:
        if input%2==0:
            input=input/2
            arr.append(input)
            print("Since the number was even we divide it by 2")
            print("The answer is:",int(input))
        else:
            input=(input*3)+1
            arr.append(input)
            print("Since the number was odd we multiply by 3 and add 1")
            print("The answer is:",int(input))
    else:
        break
print("Your number was applicable to the 3x+1 formula with a total of", len(arr) ,"tries")
x= np.array([i for i in range(len(arr))])
plt.plot(x, arr, "-o",c="black", mfc="yellow", mec="black")
plt.xlabel('count')
plt.ylabel('answer')
plt.title('3x+1 in '+ str(label_num))
plt.show()