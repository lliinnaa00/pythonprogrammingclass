inFp=None
inList, inStr = [], ""

inFp =open("/Users/hyerim/11w test.file/11w data 1.txt", "r" )

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end = "")

inFp.close()