class Coordinates:
    def __init__(self, x: float, y: float, z: float, rx: float, ry: float, rz: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz

    def _to_tuple(self) -> Tuple[float, float, float, float, float, float]:
        return (self.x, self.y, self.z, self.rx, self.ry, self.rz)