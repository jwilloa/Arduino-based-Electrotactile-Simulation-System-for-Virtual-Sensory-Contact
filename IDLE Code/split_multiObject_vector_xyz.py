import telnetlib
import re

class Cubes:
    def create(self):
        print("we here")
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

        ################    Second Cube ######################
        tn.read_until('>>>', 0.1)
        tn.write("name = 'CubeTwo'\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube = FBModelCube(name)\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube.Show = True\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube.Translation = FBVector3d(30, 0, 0)\n")

        tn.read_until('>>>', 0.1)
        tn.write("cube.Scaling = FBVector3d(10, 0.1, 10)\n")

    def first_Cube(self):
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

        global cubeOne

    def second_Cube(self):
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

        global cubeTwo

if __name__ == '__main__':
    tn = telnetlib.Telnet("127.0.0.1", 4242)
    c = Cubes()
    c.create()
    while True:
        c.first_Cube()
        c.second_Cube()
        print "First cube: ", cubeOne
        print "Second cube: ", cubeTwo
        if((cubeOne[1] >= 16.5 and cubeOne[1] <= 43.5) and (cubeOne[2] >= 3 and cubeOne[2] <= 5) and (cubeOne[3] >= -13.5 and cubeOne[3] <= 13.5)):
            print("MATCH")
        # if(cubeTwo[1] >= (cubeOne[1]+10)):
        #      print("MATCH")
