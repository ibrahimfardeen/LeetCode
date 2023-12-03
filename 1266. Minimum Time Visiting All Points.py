class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            while points[i][0] != points[i+1][0] or points[i][1] != points[i+1][1]:
                time += 1
                if points[i][0] != points[i+1][0]:
                    if points[i][0] < points[i+1][0]:
                        points[i][0] += 1
                    if points[i][0] > points[i+1][0]:
                        points[i][0] -= 1
                if points[i][1] != points[i+1][1]:
                    if points[i][1] < points[i+1][1]:
                        points[i][1] += 1
                    if points[i][1] > points[i+1][1]:
                        points[i][1] -= 1
        return time 
