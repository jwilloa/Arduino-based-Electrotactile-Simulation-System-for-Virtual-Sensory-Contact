import telnetlib
import re

class Cubes:
    def create_Cube(self):
        ################    First Cube  ######################
        tn.read_until('>>>', 0.1)
        tn.write("name = 'CubeOne'\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube = FBModelCube(name)\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube.Show = True\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube.Translation = FBVector3d(10, 10, 0)\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube.Scaling = FBVector3d(10, 10, 10)\n")

        ################   Plane     ######################
        tn.read_until('>>>', 0.1)
        tn.write("name = ''\n")

        tn.read_until('>>>', 0.1)
        tn.write("plane = FBModelCube(name)\n")

        tn.read_until('>>>', 0.1)
        tn.write("plane.Show = True\n")

        tn.read_until('>>>', 0.1)
        tn.write("plane.Translation = FBVector3d(0, 0, 0)\n")

        tn.read_until('>>>', 0.1)
        tn.write("plane.Scaling = FBVector3d(30, 0.1, 70)\n")

    def first_Cube(self):
        global cubeOne
        tn.read_until('>>>', 0.1)
        tn.write("myCube1 = FBFindModelByLabelName('CubeOne')\n")

        tn.read_until('>>>', 0.11)
        tn.write("cube1 = FBVector3d()\n")

        tn.read_until('>>>', 0.11)
        tn.write("print(myCube1.GetVector(cube1))\n")

        tn.read_until('>>>', 0.11)
        tn.write("print cube1\n")

        raw = str(tn.read_until('>>>', .1))

        numbers = re.compile('-?\d+(?:\.\d+)?')
        cubeOne = map(float, numbers.findall(raw))
        print "First cube: ", cubeOne

        if len(cubeOne) != 4:
            c.first_Cube()

    def second_Cube(self):
        global cubeTwo
        tn.read_until('>>>', 0.1)
        tn.write("myCube2 = FBFindModelByLabelName('CubeTwo')\n")

        tn.read_until('>>>', 0.11)
        tn.write("cube2 = FBVector3d()\n")

        tn.read_until('>>>', 0.11)
        tn.write("print(myCube2.GetVector(cube2))\n")

        tn.read_until('>>>', 0.11)
        tn.write("print cube2\n")

        raw = str(tn.read_until('>>>', .1))

        numbers = re.compile('-?\d+(?:\.\d+)?')
        cubeTwo = map(float, numbers.findall(raw))

        print "Second cube: ", cubeTwo

#class

if __name__ == '__main__':
    tn = telnetlib.Telnet("127.0.0.1", 4242)
    c = Cubes()
    c.create_Cube()

    while True:
        c.first_Cube()
        c.second_Cube()
        if((cubeOne[1] >= 16.5  and cubeOne[1] <= 43.5)
       and (cubeOne[2] >= 3     and cubeOne[2] <= 5)
       and (cubeOne[3] >= -13.5 and cubeOne[3] <= 13.5)):
            print("MATCH")