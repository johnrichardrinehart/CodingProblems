def main():
    cases = [
        [[1,2,3],[1,2,3]],
        [[1,1,2],[1,2]],
        [[1,1,2,3,3,4,5],[1,2,3,4,5]],
        [[1,1,1,2,3,4,4,5,6,6,6,7,7,8],[1,2,3,4,5,6,7,8]]
    ]
    cnt = 0
    for case in cases:
        cnt += 1
        print(f"case {cnt} ", end ='')
        if remove_dupes(case[0]) != case[1]:
            print("failed!")
            continue
        print("succeeded!")
        
    
def remove_dupes(v):
    cur = v[0]
    removed = 0
    for i in range(len(v)):
        if i+1-removed > len(v)-1:
            return v
        if v[i+1-removed] == cur:
            v =  v[0:i+1-removed]+v[i+2-removed:]
            removed += 1
            continue
        cur = v[i+1-removed]

main()