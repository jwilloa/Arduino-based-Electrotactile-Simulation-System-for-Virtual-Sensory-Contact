import telnetlib
tn = telnetlib.Telnet("127.0.0.1", 4242)

#Needed to get to the point in the PythonShell where you can write code
while True:
    tn.read_until('>>>', 0.1)
    tn.write("myCube2 = FBFindModelByLabelName('5DTGlove1:indexD')\n")

    tn.read_until('>>>', 0.11)
    tn.write("cube2 = FBVector3d()\n")

    tn.read_until('>>>', 0.11)
    tn.write("print(myCube2.GetVector(cube2))\n")

    tn.read_until('>>>', 0.11)
    tn.write("print cube2\n")

    raw = str(tn.read_until('>>>', .1))

    print raw

tn.close()