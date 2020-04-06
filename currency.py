def parseCode(codeString):
	
	findIndex = codeString.find(',')
	if(findIndex!=-1):
		indices = [findIndex]
		while(findIndex!=-1):
			findIndex = codeString.find(',',indices[-1]+1)
			if(findIndex!=-1):
				indices+=[findIndex]

		codes = []
		startIndex = 0
		for i in range(len(indices)):
			codes+=[codeString[startIndex:indices[i]]]
			startIndex = indices[i]+1
		codes+=[codeString[startIndex:]]

		rstr = ''
		for i in codes:
			rstr+=chr(int(i))

		return rstr

	else:
		return chr(int(codeString))
	

print(parseCode('1083,1074,1124'))
print(parseCode('1083,1074'))