def main():
    cases=[
        [vec(0,0),vec(2,2),vec(1,0),vec(0,1), True],
        [vec(0,0),vec(2,2),vec(1,1),vec(3,3), True], # colinear and intersecting
        [vec(0,0),vec(2,2),vec(1,2),vec(3,4), False], # parallel and offset
        [vec(0,0),vec(0,1),vec(0,3),vec(0,.5), True], # colinear and intersecting (negative)
        [vec(0,0),vec(0,1),vec(0,1),vec(0,2),True],
        [vec(0,0),vec(1,0),vec(1,0),vec(1,-1),True]
    ]
    case_cnt = 0
    for case in cases:
        print(f"case {case_cnt} is running")
        case_cnt += 1
        if do_intersect(case[0],diff(case[1],case[0]),case[2],diff(case[3],case[2])) != case[4]:
            print(f"FAIL!")

class vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def cross(v1, v2):
        return v1.x*v2.y-v1.y*v2.x

def diff(v1, v2):
    return vec(v1.x-v2.x, v1.y-v2.y)

def add(v1,v2):
    return vec(v1.x+v2.x, v1.y+v2.y)

def dot(v1, v2):
    return v1.x*v2.x+v1.y*v2.y

# r and s are the vectors to add to q and p to get to their endpoint
def do_overlap(q,r,p,s):
    t0 = dot(s, diff(q,p))/dot(s,s)
    t1 = dot(s, diff(add(q,r),p))/dot(s,s)
    print(f"t0 and t1: {t0} {t1}")
    # if dot(r,s) > 0:
        # print("colinear and same direction")
    return 0 <= t0 <= 1 or 0 <= t1 <= 1
    # return 0 >= t0 >= -1 or 0 >= t1 >= -1

def do_intersect(q,r,p,s):
    num_a = cross(diff(q,p), r)
    num_b = cross(diff(q,p), s)
    den = cross(s,r)
    # on the same axis
    if den == 0 and num_a == 0:
        if num_a != 0: # not on the same axis
            return False
        return do_overlap(q,r,p,s)
    if den != 0:
        return 0 <= num_a / den <= 1 and 0 <= num_b/den <= 1
    return False
    
main()