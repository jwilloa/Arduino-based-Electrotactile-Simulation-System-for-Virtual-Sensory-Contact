import telnetlib

vec = []
vec1 = []

class Cubes:
    def first_Cube(self, vec):
        tn.read_until('>>>', 0.1)
        tn.write("myCube2 = FBFindModelByLabelName('Cube')\n")

        tn.read_until('>>>', 0.11)
        tn.write("cube2 = FBVector3d()\n")

        tn.read_until('>>>', 0.11)
        tn.write("print(myCube2.GetVector(cube2))\n")

        tn.read_until('>>>', 0.11)
        tn.write("print cube2\n")

        raw = str(tn.read_until('>>>', .1))

        vec.append(raw[raw.find("(") + 1:].split()[0])
        vec.append(raw[raw.find(",") + 0:].split()[1])
        vec.append(raw[raw.find(",") + -1:].split()[2])

        print "First cube: ", vec
        vec *= 0

    def second_Cube(self, vec1):
        tn.read_until('>>>', 0.1)
        tn.write("myCube2 = FBFindModelByLabelName('Cube 1')\n")

        tn.read_until('>>>', 0.11)
        tn.write("cube2 = FBVector3d()\n")

        tn.read_until('>>>', 0.11)
        tn.write("print(myCube2.GetVector(cube2))\n")

        tn.read_until('>>>', 0.11)
        tn.write("print cube2\n")

        raw = str(tn.read_until('>>>', .1))

        vec1.append(raw[raw.find("(") + 1:].split()[0])
        vec1.append(raw[raw.find(",") + 0:].split()[1])
        vec1.append(raw[raw.find(",") + -1:].split()[2])

        print "Second cube: ", vec1
        vec1 *= 0


if __name__ == '__main__':
    tn = telnetlib.Telnet("127.0.0.1", 4242)
    c = Cubes()
    while True:
        c.first_Cube(vec)
        c.second_Cube(vec1)
        # if(vec[0] == vec1[0]):
        #     print("MATCH")
