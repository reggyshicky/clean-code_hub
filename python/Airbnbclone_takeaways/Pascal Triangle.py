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
    
    """In Pascal's Triangle, each row has a number of elements equal to its row number (starting from row 0). For example:

Row 0 has 1 element.
Row 1 has 2 elements.
Row 2 has 3 elements.
Row 3 has 4 elements.
And so on. This pattern is represented by the loop condition y <= x. When x is 0, the loop will iterate only once (for y = 0). When x is 1, the loop will iterate twice (for y = 0 and y = 1), and so on.

The purpose of this loop is to iterate over the elements in the current row (ct) and calculate their values based on the conditions specified in the if-else block. It ensures that the loop iterates over the correct range of indices for the current row in Pascal's Triangle.

So, in summary, the condition y <= x ensures that the loop iterates over the valid indices for the current row, where y varies from 0 to the row number (x).
    """