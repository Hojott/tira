class Rectangle:
    def __init__(self, p1: (int, int), p2: (int, int)):
        self.corners = [
                (p1[0], p1[1]),
                (p2[0], p1[1]),
                (p1[0], p2[1]),
                (p2[0], p2[1])
            ]

    def area(self) -> int:
        x = abs(self.corners[1][0] - self.corners[0][0])
        y = abs(self.corners[2][1] - self.corners[0][1])
        return x*y

    def intersection(self, rec):
        corners = [(0,0),(0,0),(0,0),(0,0)]
        nocross = 0

        crosspoint = self.__linescross((self.corners[0], self.corners[1]), (rec.corners[2], rec.corners[0]))
        if crosspoint[0]:
            corners[0] = crosspoint[1]
        else:
            crosspoint = self.__linescross((rec.corners[0], rec.corners[1]), (self.corners[2], self.corners[0]))
            if crosspoint[0]:
                corners[0] = crosspoint[1]
            else:
                nocross += 1
                corners[0] = self.corners[0] if self.corners[0][1] < rec.corners[0][1] else rec.corners[0]

        crosspoint = self.__linescross((self.corners[2], self.corners[3]), (rec.corners[3], rec.corners[1]))
        if crosspoint[0]:
            corners[3] = crosspoint[1]
        else:
            crosspoint = self.__linescross((rec.corners[2], rec.corners[3]), (self.corners[3], self.corners[1]))
            if crosspoint[0]:
                corners[3] = crosspoint[1]
            else:
                nocross += 1
                corners[3] = self.corners[3] if self.corners[3][1] > rec.corners[3][1] else rec.corners[3]

        if nocross == 2:
            #print(":c")
            if not self.__linescross((self.corners[2], self.corners[3]), (rec.corners[2], rec.corners[0]))[0] \
                and not self.__linescross((rec.corners[2], rec.corners[3]), (self.corners[2], self.corners[0]))[0]:
                nocross += 1
            if not self.__linescross((self.corners[0], self.corners[1]), (rec.corners[3], rec.corners[1]))[0] \
                and not self.__linescross((rec.corners[0], rec.corners[1]), (self.corners[3], self.corners[2]))[0]:
                nocross += 1

            if nocross == 4:
                if self.isinside(self, rec):
                    #print("self")
                    return self
                if self.isinside(rec, self):
                    #print("rec")
                    return rec
                #print(":C")
                return Rectangle((0, 0), (0, 0))
        #print((corners[0][0], corners[0][1]), (corners[3][0], corners[3][1]))
        return Rectangle((corners[0][0], corners[0][1]), (corners[3][0], corners[3][1]))
    
    @staticmethod
    def isinside(rec1, rec2) -> bool:
        if not ( rec1.corners[0][0] > rec2.corners[0][0] and rec1.corners[1][0] < rec2.corners[1][0] ):
            return False
        if not ( rec1.corners[2][1] > rec2.corners[2][1] and rec1.corners[0][1] < rec2.corners[0][1] ):
            return False
        return True

    @staticmethod
    def __linescross(xline: ((int, int), (int, int)), yline) -> (bool, (int, int)):
        """ Check if two lines cross and also return point where they cross """

        if not (xline[0][0] <= yline[0][0] and xline[1][0] >= yline[0][0]):
            return (False, (0,0))
        if not (yline[0][1] <= xline[0][1] and yline[1][1] >= xline[0][1]):
            return (False, (0,0))
        return (True, (yline[0][0], xline[0][1]))

def area(rec1, rec2, rec3):
    rec1 = Rectangle((rec1[0], rec1[1]), (rec1[2], rec1[3]))
    rec2 = Rectangle((rec2[0], rec2[1]), (rec2[2], rec2[3]))
    rec3 = Rectangle((rec3[0], rec3[1]), (rec3[2], rec3[3]))

    area = rec1.area() + rec2.area() + rec3.area()
    area -= rec1.intersection(rec2).area() + rec1.intersection(rec3).area() + rec2.intersection(rec3).area()
    area += rec1.intersection(rec2).intersection(rec3).area()

    return area

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16

    rec1 = (0,3,3,2)
    rec2 = (-1,3,2,-3)
    rec3 = (-1,0,1,-3)
    print(area(rec1,rec2,rec3)) # 19

    rec1 = (-3,2,1,-2)
    rec2 = (0,2,1,-1)
    rec3 = (0,1,2,-3)
    print(area(rec1,rec2,rec3)) # 21

    rec1 = (-3,-1,0,-3)
    rec2 = (-3,3,3,-2)
    rec3 = (-1,0,1,-1)
    print(area(rec1,rec2,rec3)) # 33

    rec1 = (0,1,2,-2)
    rec2 = (-1,3,3,2)
    rec3 = (-2,3,0,2)
    print(area(rec1,rec2,rec3)) # 11