import telnetlib

tn = telnetlib.Telnet("127.0.0.1", 4242)

#Needed to get to the point in the PythonShell where you can write code.
tn.read_until('>>>', 5)

tn.write( '1+1\n' )


raw = str(tn.read_until('>>>', .1))

print raw


tn.close()
