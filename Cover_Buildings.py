'''
There are N rectangular buildings standing along the road next to each other.

Renovation of all of the buildings is planned,
we want to cover them with rectangular banners until the renovations are finished.
Of course, to cover a building, the banner has to be at least as high as the building.
We can cover more than one building with a banner if it is wider than 1.

For example, to cover buildings of heights 3, 1, 4 we could use a banner of size 4×3 (i.e. of height 4 and width 3)
we can order at most two banners and we want to cover all of the buildings.
Also, we want to minimize the amount of material needed to produce the banners.
What is the minimum total area of at most two banners which cover all of the buildings?

[5,3,2,4]
(we have covered using two banner's, so first we separate the buildings into two)
(max height + width = cover the building)
[5]+[3,2,4] --> 5 X 1 + 4 X 3 = 17
[5,3]+[2,4] --> 5 X 2 + 4 X 2 = 26
[5,3,2]+[4] --> 5 X 3 + 4 X 1 = 19
(there is a possible continue building division)
so we return the least area of the banner that is 17


1. Given H = [3, 1, 4], the function should return 10. (3×2 and the third building with a banner of size 4×1)
2. Given H = [5, 3, 2, 4], the function should return 17.(5×1 and the other buildings with a banner of size 4×3)
3. Given H = [5, 3, 5, 2, 1], your function should return 19. (5×3 and the other two with a banner of size 2×2)
4. Given H = [7, 7, 3, 7, 7], your function should return 35. (7×5)
5. Given H = [1, 1, 7, 6, 6, 6], your function should return 30. (1×2 and 7×4)
'''
def solution(H):
    # write your code in Python 3.6
    banner = []
    for i in range(len(H)-1):
        a = H[0:i+1]
        b = H[i+1:]
        c = max(a) * len(a)
        d = max(b) * len(b)
        e = c+d
        banner.append(e)
    return min(banner)
H = [5,3,2,4]
print("Banner area : ",solution(H))
input()
