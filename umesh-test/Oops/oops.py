from enum import Enum
class position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom
    
    def log(self):
        print(str(self.pan), str(self.tilt), str(self.zoom))

# p = position(10, 11, 12)
# p.log()

class Camera:
    def __init__(self, serila_num , position, camera_type):
        self.serila_num = serila_num
        self.position = position
        self.camera_type = camera_type

    def log(self):
        print(self.serila_num, str(self.camera_type))
        self.position.log()


    class CameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2

c = Camera("abcdfgh121246" , position(10,11,13), Camera.CameraType.stationary)
c.log()





























# import enum
# class days(enum.Enum):
#     sun = 1
#     mon = 2
#     tue = 3
# print("The enum member as a string is : ",end=" ")
# print(days.mon)

# print ("he enum member as a repr is : ",end="")
# print (repr(days.sun))

# print ("The type of enum member is : ",end ="")
# print (type(days.mon))

# print ("The name of enum member is : ",end ="")
# print (days.tue.name)









        