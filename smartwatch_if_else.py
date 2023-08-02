import os

f = open('C:\\smartwatch\\popupresults\\windowsslave4.txt', 'r')

result = int (f.readline())

print(result)

if result ==1:
    os.system('python C:\\Users\\User\\PycharmProjects\\helloworld\\print.py')

else:
    exit()
