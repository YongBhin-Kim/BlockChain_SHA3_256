# print(len("1143ca9042497929851e4507f4edf4a80be8bd741143e5f0644c8415c0e7e459"))
'''
hex1 = "2b7f2009cd08ac17c81b87917bcfe5f296a755ff8f6e5bc36dae21ad0ab34ed8" # 256 -> 96+160 24개||40개
# hex1 = "2b7f2009cd08ac17c81b87918bcfe5f296a755ff8f6e5bc36dae21ad0ab34ed8" # 256 -> 96+160
byte1 = b'+\x7f \t\xcd\x08\xac\x17\xc8\x1b\x87\x91{\xcf\xe5\xf2\x96\xa7U\xff\x8fn[\xc3m\xae!\xad\n\xb3N\xd9'

print(byte1)
print(byte1.hex())
print(byte1.hex()[:5])
print(byte1.hex()[:5].encode())
print(bytes(byte1.hex()[:5].encode()))
print(bytes.fromhex(byte1.hex()[:40]))


# print(bin( int(hex116) ))
# print(bin( int(hex116)&( (1<<160)-1 ) ))
# print(bin( int(byte1.hex(),16)&((1<<160)-1) ))
# print(hex( int(hex1,16)&((1<<160)-1) )) 
# if (len(bin( int(hex1,16)&( (1<<160)-1 ) )))==161:
    # print(bin( int(hex1,16)&( (1<<160)-1 )^(1<<159) ))
# else:
    # bin( int(hex1,16)&( (1<<160)-1 ) )
    
    
# print(bin((1<<160)-1))
# print(len(bin( (1<<160)-1 )))
# print(bin( ((1<<4)-1)))
# print(bin( ((1<<4)-1) ^(1<<3)))
# print(len("2b7f2009cd08ac17c81b87917bcfe5f296a755ff8f6e5bc36dae21ad0ab34ed8"[24:]))
# print(b'0'*160)

# print("30616563343432396564663831623537626164356262653261303964373536363235633530323862".encode().hex())

print(len("5c59acdf312726d39c136c0e87b2a42ad47b3301"))
'''

# buf = 0
# off = 1
# for _ in range(5):
#     buf += off
# print(buf)
# a = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
# b = "00 "
# c = "a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 a3 "
# print(len(c)/3)
# print((len(a)-1)/3)
# a = "0 0 8 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 "
# b = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 "
# c = "163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 163 "
# d = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 "

# print(len(a)//2)
# print(len(b)//2)
# print(len(c)//4)
# print(len(d)//2)

# import inspect
# import _sha3
# print(inspect.getfile(_sha3))

# a = "79 f3 8a de c5 c2 03 07 a9 8e f7 6e 83 24 af bf d4 6c fd 81 b2 2e 39 73 c6 5f a1 bd 9d e3 17 87 "
# a = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000013k'\xedS\xe6\x91b\x04i(\xdc\xda\xae\n\x17!\x02\xee\xfeT0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008191000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000056196983056536306434355956045959846846233318503819312743915155875669167698920463986137033695621581099763900605771228745959582133824525141779284499292594475570677300795691039214710998669256101489124769286779824293245508985158389001074805851106955934746208175188"
# print(len(a))
# blockID = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000053"
# print(len(blockID))
# prev_hash="\x12\x80@\xa1\xa7\xcd\xcf\x89L\x83\xe8\xad\xdbl\x0cT\xae\x94\x15\x17"
# print(len(prev_hash))
# data = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008191000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000120013877050777213315480131216183176066072841647664840428448419153202128391858350256671754508666919463236107070652655640057940431527484977436910553518077141485648887117420056955625857024982330397810712625736381089975489471996761318474057758393865904336722391914"
# print(len(data))

# input1 = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001242c02be943eefc62e020bdc1fa97c6f514480c940000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008191000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000066128142544489507289598500011895501759273002631664723723365031235141287095200865346302739351424623454442877766085179508150544701452209497158621744186014133333134797821405990572072486255894190821957880887795566207044972992225344099976288452390501951614107009030"
# print(len(input1))
import random
# a = hex(100)
# print(100//16,100%16)
# a=format(100//16 * 10 + 100%16,'0160')
# print(a)
# a=format(random.randrange(0, 1<<864))
# print(a)
# print()
# print(len(hex(int(a))))
# print(hex(int(a))[2:])
# # print(format(hex(int(a)), '0216x'))
# print(hex(int(a))[2:].ljust(216,'0'))
# print(256*8192)
a = b'0'*20
print(len((a).hex()))