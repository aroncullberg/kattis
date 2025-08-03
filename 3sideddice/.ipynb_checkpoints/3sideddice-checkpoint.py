from typing import Tuple, Iterable

from collections import namedtuple
from itertools import combinations

Vector3 = namedtuple('Vector3', 'x y z')
Vector2 = namedtuple('Vector2', 'x y')

def sub(p: Vector2, q: Vector2) -> Vector2:
    return Vector2(p.x - q.x, p.y - q.y)

def cross(u: Vector2, v: Vector2) -> Vector2:
    return u.x * v.y - u.y * v.x

def dot(u: Vector2, v: Vector2) -> Vector2:
    return u.x * v.x + u.y * v.y

def dist2(p: Vector2, q: Vector2) -> int:
    return (p.x - q.x) ** 2 + (p.y - q.y) ** 2

def furthest_pair(pts: Iterable[Vector2]) -> Tuple[Vector2, Vector2]:
    return max(combinations(pts, 2), key=lambda pair: dist2(*pair))

def not_on_edge(a):
    return a > 0 # colinear no have area

def strictly_inside(A: Vector2, B: Vector2, C: Vector2, P: Vector2) -> bool:
    # case 1: A,B,C make triangle 🙂 
    # https://www.desmos.com/3d/ojhkxuakvd
    area2 = cross(sub(B, A), sub(C, A))
    if area2:
        # cross product give area but idk how direciton work so it give negative area someitmes? Simon pls explain, u smart so you know
        # simon not neede hugo explain 🤓
        area2 = abs(area2) 
        a1 = abs(cross(sub(B, P), sub(C, P)))
        a2 = abs(cross(sub(A, P), sub(C, P)))
        a3 = abs(cross(sub(A, P), sub(B, P)))
        
        
        return not_on_edge(a1) and not_on_edge(a2) and not_on_edge(a3) and a1 + a2 + a3 == area2

    # case 2:
    # if we get here then it no make triangle, the 3 points then make not triangle but instead a line 🤯
    # 🤓☝️ If the area between the triangle and the linear vector space is nonzero then P is not on line and there exists no solution
    # https://www.desmos.com/3d/c80sghjaiw
    if cross(sub(B, A), sub(P, A)) != 0:
        return False

    # 👪 all three points on same pos
    # no desmos for this :|
    if A == B == C:
        return P == A

    # now we know that the 3 points are colinear and they are not all in one place, but is it between the two points or outside that area?
    # https://www.desmos.com/3d/bvvbzzn4yy
    # prubple vector is distanceStart2End
    # orange vector is distanceStart2Starget
    S, T = max(combinations((A, B, C), 2),key=lambda pair: dot(sub(pair[0], pair[1]), sub(pair[0], pair[1])))

    distanceStart2End = sub(T, S)
    distanceStart2Starget = sub(P, S)
    numerator = dot(distanceStart2Starget, distanceStart2End)
    denominator = dot(distanceStart2End, distanceStart2End)
    return 0 < numerator < denominator

def read_vec():
    return Vector3(*map(int, input().split()))

while True:
    d1 = read_vec()
    if d1 == Vector3(0,0,0):
        break
    d2 = read_vec()
    d3 = read_vec() 
    tgt = read_vec()
    
    # who can afford a thrid dimension in this ecconomy??? (telia pls pay more so i can affor z axis)
    A = Vector2(d1.x, d1.y)
    B = Vector2(d2.x, d2.y)
    C = Vector2(d3.x, d3.y)
    P = Vector2(tgt.x, tgt.y)
    
    # results.append("YES" if strictly_inside(A, B, C, P) else "NO")
    print("YES" if strictly_inside(A, B, C, P) else "NO"), input()
