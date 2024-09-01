# example of sys.argv
'''import sys
if len(sys.argv)<2:
    print("too many arguments")
elif len(sys.argv)>2:
    print("too many arguments")
else :
    print("hello, my name is ", sys.argv[1])


'''
# eample of sys.exit
'''import sys
if len(sys.argv)<2:
    sys.exit("too many arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")
else :
    print("hello, my name is ", sys.argv[1])
'''

# slice example

import sys
if len(sys.argv)>2:
    sys.exit("too many arguments")

for arg in sys.argv[1:] :
    print("hello, my name is ", arg)







