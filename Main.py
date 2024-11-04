import os
import numpy as np
from dotenv import load_dotenv
import time
from servicies.cobot.CobotService import CobotService
from servicies.cobot.Coordinates import Coordinates

def drawEscudoDeTigre(cobotService):
    z = 0.055
    x1 = 0.54
    y1 = 0.10
    x2 = 0.68
    y2 = 0.25
    y3 = 0.15
    x3 = 0.62
    x4 = 0.6

    p1 = Coordinates(x1, y1, z, 3.142, 0, 0)
    p2 = Coordinates(x2, y1, z, 3.142, 0, 0)
    p3 = Coordinates(x2, y2, z, 3.142, 0, 0)
    p4 = Coordinates(x1, y2, z, 3.142, 0, 0)
    p5 = Coordinates(x1, y3, z, 3.142, 0, 0)
    p6 = Coordinates(x2, y3, z, 3.142, 0, 0)
    p7 = Coordinates(x3, y3, z, 3.142, 0, 0)
    p8 = Coordinates(x4, y3, z, 3.142, 0, 0)
    p9 = Coordinates(x2, y3, z, 3.142, 0, 0)
    p10 = Coordinates(x2, y3, z, 3.142, 0, 0)
    p11 = Coordinates(0.61, 0.26, z, 3.142, 0, 0) 
    p12 = Coordinates(0.62, y2, z, 3.142, 0, 0)
    p13 = Coordinates(x4, y2, z, 3.142, 0, 0)

    #square
    cobotService.moveL(p1)
    time.sleep(5)
    cobotService.moveL(p2)
    time.sleep(5)
    cobotService.moveL(p3)
    time.sleep(5)
    cobotService.moveL(p4)
    time.sleep(5)
    cobotService.moveL(p1)
    time.sleep(5)

    cobotService.moveL(p5)
    time.sleep(5)
    cobotService.moveL(p8)
    time.sleep(5)
    cobotService.moveL(p10)
    time.sleep(5)

    cobotService.moveL(p13)
    time.sleep(5)
    cobotService.moveL(p11)
    time.sleep(5)
    cobotService.moveL(p12)
    time.sleep(5)

    cobotService.moveL(p9)
    time.sleep(5)
    cobotService.moveL(p7)
    time.sleep(5)
    cobotService.moveL(p6)
    time.sleep(5)


#TRANSLATE
# Función para calcular el vector normal
def normal_vector(u1, u2):
    return np.cross(u1, u2)

# Función para calcular la matriz de rotación entre dos planos
def rotation_matrix(u1, u2, v1, v2):
    n1 = normal_vector(u1, u2)
    n2 = normal_vector(v1, v2)
    
    U = np.array([u1, u2, n1]).T
    V = np.array([v1, v2, n2]).T
    
    R = V @ np.linalg.inv(U)
    return R

# Función para calcular el vector de traslación entre dos puntos
def translation_vector(O1, O2):
    return O2 - O1

def transform_point(P, R, T):
    return R @ P + T


def draw_triangle(cobotService):
    z = 0.048
    x1 = 0.7
    x2 = 0.58
    y1 = -0.166
    y2 = -0.012
    coordinates = [
        Coordinates(x1, y1, z, 3.142, 0, 0),
        Coordinates(x1, y2, z, 3.142, 0, 0),
        Coordinates(x2, y1, z, 3.142, 0, 0),
        Coordinates(x1, y1, z, 3.142, 0, 0),
        Coordinates(x1, y1, z+1, 3.142, 0, 0),
    ]
    for c in coordinates:
        cobotService.moveL(c)
        time.sleep(5)

def translate_coordinate(coordinate, R, T):
    P = np.array([coordinate.x, coordinate.y, coordinate.z])
    P2 = transform_point(P, R, T)
    return Coordinates(P2[0], P2[1], P2[2], coordinate.rx, coordinate.ry, coordinate.rz)


def draw_in_board(cobotService):
    z = 0
    x1 = 0.7-0.3
    x2 = 0.58-0.3
    y1 = -0.166+0.5
    y2 = -0.012+0.5

    rx = 4.712
    ry = 0
    rz = 0
    coordinates = [
        Coordinates(0, 0, 0, rx, ry, rz),
        Coordinates(x1, y1, z, rx, ry, rz),
        Coordinates(x1, y2, z, rx, ry, rz),
        Coordinates(x2, y1, z, rx, ry, rz),
        Coordinates(x1, y1, z, rx, ry, rz),
        Coordinates(x1, y1, z, rx, ry, rz),
        #Coordinates(0.2, 0, 0, rx, ry, rz),
        #Coordinates(0, 0, 0.2, rx, ry, rz),
        Coordinates(0, 0, 0, rx, ry, rz),
    ]

    # Definimos los vectores base del plano xy (u1: eje x, u2: eje y)
    u1_xy = np.array([1, 0, 0])
    u2_xy = np.array([0, 1, 0])

    #p1 = np.array([-0.130, 0.540, 0.790])
    #p2 = np.array([0.175, 0.520, 0.790])
    #p3 = np.array([0.175, 0.520, 0.552])
    p1 = np.array([1, 0.7, 0])
    p2 = np.array([0, 0.7, 1.25])
    origin_board = np.array([0, 0.7, 0.25])


    # Calculate directional vectors in the yz plane
    v1_yz = p1 - origin_board
    v2_yz = p2 - origin_board

    # Normalize vectors to get unit vectors
    v1_yz = v1_yz / np.linalg.norm(v1_yz)
    v2_yz = v2_yz / np.linalg.norm(v2_yz)

    # Calculamos la matriz de rotación
    R_xy_to_yz = rotation_matrix(u1_xy, u2_xy, v1_yz, v2_yz)

    # El origen del plano xy es (0, 0, 0), y también el del plano yz
    O_xy = np.array([0, 0, 0])
    O_yz = origin_board

    # Calculamos el vector de traslación
    T_xy_to_yz = translation_vector(O_xy, O_yz)

    coordinates = list(map(lambda c: translate_coordinate(c, R_xy_to_yz, T_xy_to_yz), coordinates))
    for c in coordinates:
        cobotService.moveL(c, time=5)
        time.sleep(6)

if __name__ == "__main__":
    load_dotenv()

    cobotHost = os.getenv('COBOT_HOST')
    cobotPort = int(os.getenv('COBOT_PORT'))
    cobotAcceleration = float(os.getenv('COBOT_ACCELERATION'))
    cobotSpeed = float(os.getenv('COBOT_SPEED'))

    cobotService = CobotService(cobotHost, cobotPort, cobotAcceleration, cobotSpeed)
    time.sleep(5)
    draw_in_board(cobotService)