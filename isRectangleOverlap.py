    def isRectangleOverlap(self, rec1, rec2):
        leBmX = max(rec1[0], rec2[0])
        leBmY = max(rec1[1], rec2[1])
        
        rtTpX = min(rec1[2], rec2[2])
        rtTpY = min(rec1[3], rec2[3])
        
        overlap = max(rtTpX - leBmX, 0) * max(rtTpY - leBmY, 0)
        return overlap !=0