class Solution(object):
    def nearestValidPoint(self, x, y, points):
        min_distance = float('inf')
        min_index = -1

        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                distance = abs(px - x) + abs(py - y)
                if distance < min_distance:
                    min_distance = distance
                    min_index = i
        return min_index