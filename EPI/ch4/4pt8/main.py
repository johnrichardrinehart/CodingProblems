import time
import uuid
import math

class point:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

class rec:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.w}, {self.h})"

def main():
  cases = [
      (rec(0,0,2,2),rec(1,1,3,3), True, 1),
      (rec(0,0,2,2),rec(3,3,5,5), False, -1),
      (rec(0,0,2,2),rec(0,0,2,2), True, 4),
      (rec(0,0,5,5),rec(1,1,10,10), True, 16),
      (rec(5,0,2,5),rec(5,-5,2,20), True, 10),
  ]
  for case in cases:
      res = problem4pt8(case[0],case[1])
      if res[0] != case[2] or res[1] != case[3]:
          print(f"failed at {case[0]} and {case[1]}. Got {res[0]} and {res[1]}: Expected {case[2]} and {case[3]}")
          continue
      print("YAY!")

  cases = [
        ([point(0,0), point(1,1),point(0,1),point(1,0)], True),
        ([point(0,2), point(2,3), point(0,0), point(1,3)], False),
  ]

  for case in cases:
    if problem4pt8variant1(case[0]) != case[1]:
        print(f"failed")

def is_intersect(rec1, rec2):
    return rec1.x + rec1.w > rec2.x and \
        rec2.x + rec2.w > rec1.x and \
        rec1.y + rec1.h > rec2.y and \
        rec2.y + rec2.h > rec1.y

def area(rec1, rec2):
    x= max(rec1.x,rec2.x)
    y= max(rec1.y,rec2.y)
    return (min(rec1.x+rec1.w, rec2.x+rec2.w)-x)*(min(rec1.y+rec1.h, rec2.y+rec2.h)-y)


def problem4pt8(rec1,rec2):
    a = -1
    ist = is_intersect(rec1,rec2)
    if ist:
        a = area(rec1,rec2)
    return (ist, a)

# Determine if 4 points in a plane are the vertices of a rectangle
def problem4pt8variant1(points):
    # Find the center of mass and the distances from each
    com = point(
        (points[0].x+points[1].x+points[2].x+points[3].x)/4,
        (points[0].y+points[1].y+points[2].y+points[3].y)/4,
    )
    dd1 = (points[0].x-com.x)**2 + (points[0].y-com.y)**2
    dd2 = (points[1].x-com.x)**2 + (points[1].y-com.y)**2
    dd3 = (points[2].x-com.x)**2 + (points[2].y-com.y)**2
    dd4 = (points[3].x-com.x)**2 + (points[3].y-com.y)**2

    return dd1 == dd2 and dd1 == dd3 and dd1 == dd4

main()