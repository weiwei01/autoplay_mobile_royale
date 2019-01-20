#open file
fileName = 'getFreeResource'
fullFileName = fileName + '.txt' 
f = open(fullFileName, 'r')
x = f.read()
f.close()

inputCommand = list()

for line in x.split('\n'):
	#print(line.split(' '))
	print(line)
	first = line.split(' ')[0]
	second = line.split(' ')[1]
	decimalSecond = str(int(second, 16)) 
	
	third = line.split(' ')[2]
	decimalThird = str(int(third, 16)) 

	fourth = line.split(' ')[3]
	decimalFourth = str(int(fourth, 16)) 
	
	afterConvertCommand = first + ' ' + decimalSecond + ' ' + decimalThird + ' '+ decimalFourth
	print(afterConvertCommand)
	inputCommand.append(afterConvertCommand+'\n')

#for command in inputCommand:
#with open(fileName+'_decimal.txt', 'a') as the_file:
fo = open(fileName+'_decimal.txt', "w")
line = fo.writelines( inputCommand )
