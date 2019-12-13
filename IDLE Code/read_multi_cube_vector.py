import telnetlib

class Cubes:
    def first_Cube(self):
        tn.read_until('>>>', 0.1)
        tn.write("myCube2 = FBFindModelByLabelName('Cube')\n")

        tn.read_until('>>>', 0.11)
        tn.write("cube2 = FBVector3d()\n")

        tn.read_until('>>>', 0.11)
        tn.write("print(myCube2.GetVector(cube2))\n")

        tn.read_until('>>>', 0.11)
        tn.write("print cube2\n")

        raw = str(tn.read_until('>>>', .1))

        print "First cube: ", raw

    def second_Cube(self):
        tn.read_until('>>>', 0.1)
        tn.write("myCube2 = FBFindModelByLabelName('Cube 1')\n")

        tn.read_until('>>>', 0.11)
        tn.write("cube2 = FBVector3d()\n")

        tn.read_until('>>>', 0.11)
        tn.write("print(myCube2.GetVector(cube2))\n")

        tn.read_until('>>>', 0.11)
        tn.write("print cube2\n")

        raw = str(tn.read_until('>>>', .1))

        print "Second cube: ", raw


if __name__ == '__main__':
    tn = telnetlib.Telnet("127.0.0.1", 4242)
    c = Cubes()
    while True:
        c.first_Cube()
        c.second_Cube()
