class CountSquares:

    def __init__(self):
        self.point_map = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.point_map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue

            res += self.point_map[(x, py)] * self.point_map[(px, y)] 

        return res