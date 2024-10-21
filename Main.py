import os
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

if __name__ == "__main__":
    load_dotenv()

    cobotHost = os.getenv('COBOT_HOST')
    cobotPort = int(os.getenv('COBOT_PORT'))
    cobotAcceleration = float(os.getenv('COBOT_ACCELERATION'))
    cobotSpeed = float(os.getenv('COBOT_SPEED'))

    cobotService = CobotService(cobotHost, cobotPort, cobotAcceleration, cobotSpeed)
    time.sleep(5)
    #cobotService.moveL(Coordinates(0.50, 0, 0.2, 3.142, 0, 0))
    # cobotService.moveL(Coordinates(0.7686, -0.037, 0.03, 3.142, 0, 0))
    # time.sleep(5)
    # cobotService.moveL(Coordinates(0.7686, -0.2, 0.03, 3.142, 0, 0))
    # time.sleep(5)
    # cobotService.moveL(Coordinates(0.59, -0.037, 0.03, 3.142, 0, 0))
    drawEscudoDeTigre()