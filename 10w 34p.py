outFp = open(outFname, 'w', encoding ='utf-8')
while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr=""
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum=ord(ch)
        chNum=chNum+secu
        ch2 =chr(chNum)
        outStr=outStr+ch2

    outFp.write(outStr)

outFp.close()
inFp.close()
print('%s-->변환 완료' % (inFname, outFname))