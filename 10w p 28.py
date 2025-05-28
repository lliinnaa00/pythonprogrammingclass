inFp, outFp = None, None
inStr = ""

inFp = open("/Users/hyerim/11w test.file/11w data 1.txt", "r")
outFp = open("/Users/hyerim/11w test.file/11w data 1.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")