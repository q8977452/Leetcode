def computeArea(self, A, B, C, D, E, F, G, H):
        
        leBmX = max(A, E)
        leBmY = max(B, F)
        
        rtTpX = min(C, G)
        rtTpY = min(D, H)
        
        overlap = max(rtTpX - leBmX, 0) * max(rtTpY - leBmY, 0)
        
        return abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F) - overlap