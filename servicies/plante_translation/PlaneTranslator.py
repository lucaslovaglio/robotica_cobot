from .PlaneData import PlaneData
import numpy as np

class PlaneTranslator:
    def __init__(self, plane1 : PlaneData, plane2 : PlaneData) -> None:
        self.T = self._translation_vector(plane1.center, plane2.center)
        u1 = self._normalize(plane1.point1-plane1.center)
        u2 = self._normalize(plane1.point2-plane1.center)
        v1 = self._normalize(plane2.point1-plane2.center)
        v2 = self._normalize(plane2.point2-plane2.center)
        self.R = self._rotation_matrix(u1, u2, v1, v2)

    def transform_point(self, point):
        return self.R @ point + self.T


    def _translation_vector(self, origin1, origin2):
        return  origin2 - origin1

    def _rotation_matrix(self, u1, u2, v1, v2):
        n1 = self._normal_vector(u1, u2)
        n2 = self._normal_vector(v1, v2)
        
        U = np.array([u1, u2, n1]).T
        V = np.array([v1, v2, n2]).T
        
        R = V @ np.linalg.inv(U)
        return R

    def _normal_vector(self, u1, u2):
        return np.cross(u1, u2)

    def _normalize(self, v):
        return v / np.linalg.norm(v)
