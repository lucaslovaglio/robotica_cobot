import os
import numpy as np
from dotenv import load_dotenv
import time
from servicies.cobot.CobotService import CobotService
from servicies.cobot.Coordinates import Coordinates
from servicies.plante_translation.PlaneData import PlaneData
from servicies.plante_translation.PlaneTranslator import PlaneTranslator

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

def translate_coordinate(coordinate, translator):
    P = np.array([coordinate.x, coordinate.y, coordinate.z])
    P2 = translator.transform_point(P)
    return Coordinates(P2[0], P2[1], P2[2], coordinate.rx, coordinate.ry, coordinate.rz)


def draw_in_board(cobotService, translator, rx, ry, rz):
    # z = 0
    # x1 = 0.7-0.3
    # x2 = 0.58-0.3
    # y1 = -0.166+0.5
    # y2 = -0.012+0.5

    # rx = 4.712
    # ry = 0
    # rz = 0
    # coordinates = [
    #     Coordinates(0, 0, 0, rx, ry, rz),
    #     Coordinates(x1, y1, z, rx, ry, rz),
    #     Coordinates(x1, y2, z, rx, ry, rz),
    #     Coordinates(x2, y1, z, rx, ry, rz),
    #     Coordinates(x1, y1, z, rx, ry, rz),
    #     Coordinates(x1, y1, z, rx, ry, rz),
    #     #Coordinates(0.2, 0, 0, rx, ry, rz),
    #     #Coordinates(0, 0, 0.2, rx, ry, rz),
    #     Coordinates(0, 0, 0, rx, ry, rz),
    # ]

    x1 = 0
    x2 = 0.1
    y1= 0
    y2 = 0.1

    z = 0.07

    coordinates = [
        Coordinates(x1, y1, z, rx, ry, rz),
        Coordinates(x2, y1, z, rx, ry, rz),
        Coordinates(x2, y2, z, rx, ry, rz),
        Coordinates(x1, y2, z, rx, ry, rz),
        Coordinates(x1, y1, z, rx, ry, rz),
    ]

    coordinates = list(map(lambda c: translate_coordinate(c, translator), coordinates))
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

    plane1 = PlaneData([0, 0, 0], [1,0,0], [0,1,0])

# master of all things
    # plane2 = PlaneData(
    #     [0.159, 0.572, 0.809],
    #     [0.423, 0.572, 0.809], 
    #     [0.159, 0.572, 0.541]
    # )
    plane2 = PlaneData(
        [-0.126, 0.425, 0.450], 
        [-0.143, 0.421, 0.635],
        [0.121, 0.482, 0.470]
    )

    translator = PlaneTranslator(plane1, plane2)

    rx = 4.602
    ry = 0.853
    rz = -0.408
    draw_in_board(cobotService, translator, rx, ry, rz)


    