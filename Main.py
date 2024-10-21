import os
from dotenv import load_dotenv
import time
from servicies.cobot.CobotService import CobotService
from servicies.cobot.Coordinates import Coordinates

if __name__ == "__main__":
    load_dotenv()

    cobotHost = os.getenv('COBOT_HOST')
    cobotPort = int(os.getenv('COBOT_PORT'))
    cobotAcceleration = float(os.getenv('COBOT_ACCELERATION'))
    cobotSpeed = float(os.getenv('COBOT_SPEED'))

    cobotService = CobotService(cobotHost, cobotPort, cobotAcceleration, cobotSpeed)
    time.sleep(5)
    cobotService.moveL(Coordinates(10, 10, 10, 10, 10, 10))