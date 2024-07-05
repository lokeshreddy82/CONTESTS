class SegmentTree2D:
    def __init__(self, matrix):
        #Here if not matrix then raise the exception
        if not matrix or not matrix[0]:
            raise ValueError("Matrix cannot be empty")
        
        self.n = len(matrix)#here the how many rows
        self.m = len(matrix[0])#how many coloumns in a matrx
        self.data = matrix#Here matrix we are doing here global or public type we can use any time
        self.tree = [[0] * (4 * self.m) for _ in range(4 * self.n)]#Here a creating the non overlaping tree data structure
        self.build_x(1, 0, self.n - 1)# Here a building the tree 

    def build_y(self, vx, lx, rx, vy, ly, ry):
        if ly == ry:
            if lx == rx:
                self.tree[vx][vy] = self.data[lx][ly]
            else:
                self.tree[vx][vy] = self.tree[vx * 2][vy] + self.tree[vx * 2 + 1][vy]
        else:
            my = (ly + ry) // 2
            self.build_y(vx, lx, rx, vy * 2, ly, my)
            self.build_y(vx, lx, rx, vy * 2 + 1, my + 1, ry)
            self.tree[vx][vy] = self.tree[vx][vy * 2] + self.tree[vx][vy * 2 + 1]

    def build_x(self, vx, lx, rx):
        if lx != rx:
            mx = (lx + rx) // 2
            self.build_x(vx * 2, lx, mx)
            self.build_x(vx * 2 + 1, mx + 1, rx)
        self.build_y(vx, lx, rx, 1, 0, self.m - 1)
 
    def sum_y(self, vx, vy, tly, try_, ly, ry):
        if ly > ry:
            return 0
        if ly == tly and ry == try_:
            return self.tree[vx][vy]
        tmy = (tly + try_) // 2
        return self.sum_y(vx, vy * 2, tly, tmy, ly, min(ry, tmy)) + \
               self.sum_y(vx, vy * 2 + 1, tmy + 1, try_, max(ly, tmy + 1), ry)

    def sum_x(self, vx, tlx, trx, lx, rx, ly, ry):
        if lx > rx:
            return 0
        if lx == tlx and rx == trx:
            return self.sum_y(vx, 1, 0, self.m - 1, ly, ry)
        tmx = (tlx + trx) // 2
        return self.sum_x(vx * 2, tlx, tmx, lx, min(rx, tmx), ly, ry) + \
               self.sum_x(vx * 2 + 1, tmx + 1, trx, max(lx, tmx + 1), rx, ly, ry)

    def update_y(self, vx, lx, rx, vy, ly, ry, x, y, new_val):
        if ly == ry:
            if lx == rx:
                self.tree[vx][vy] = new_val
            else:
                self.tree[vx][vy] = self.tree[vx * 2][vy] + self.tree[vx * 2 + 1][vy]
        else:
            my = (ly + ry) // 2
            if y <= my:
                self.update_y(vx, lx, rx, vy * 2, ly, my, x, y, new_val)
            else:
                self.update_y(vx, lx, rx, vy * 2 + 1, my + 1, ry, x, y, new_val)
            self.tree[vx][vy] = self.tree[vx][vy * 2] + self.tree[vx][vy * 2 + 1]

    def update_x(self, vx, lx, rx, x, y, new_val):
        if lx != rx:
            mx = (lx + rx) // 2
            if x <= mx:
                self.update_x(vx * 2, lx, mx, x, y, new_val)
            else:
                self.update_x(vx * 2 + 1, mx + 1, rx, x, y, new_val)
        self.update_y(vx, lx, rx, 1, 0, self.m - 1, x, y, new_val)

    def sum(self, x1, y1, x2, y2):
        return self.sum_x(1, 0, self.n - 1, x1, x2, y1, y2)

    def update(self, x, y, new_val):
        self.data[x][y] = new_val
        self.update_x(1, 0, self.n - 1, x, y, new_val)


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

st = SegmentTree2D(matrix)

print("Sum of submatrix (0,0) to (2,2):", st.sum(0, 0, 2, 2))  # Should output 45
print("Sum of submatrix (1,1) to (2,2):", st.sum(1, 1, 2, 2))  # Should output 28

st.update(1, 1, 10)  # Update element at (1, 1) to 10

print("Sum of submatrix (0,0) to (2,2) after update:", st.sum(0, 0, 2, 2))  # Should output 50
