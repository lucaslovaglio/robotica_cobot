import numpy as np



class PlaneData:
    def __init__(self, center, planePoint1, planePoint2):
        self.center = np.array(center) 
        self.point1 = np.array(planePoint1)
        self.point2 = np.array(planePoint2)