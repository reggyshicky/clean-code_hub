# Pascal Triangle

def pascal_triangle(n):
    pt = []
    
    for x in range(n):
        ct = []
        for y in range(x + 1):
            if y == 0 or y == x:
                ct.append(1)
            else:
                ct.append(pt[x - 1][y] + pt[x - 1][y -1])
        pt.append(ct)
    return pt 

result = pascal_triangle(5)

for row in result:
    print(row)