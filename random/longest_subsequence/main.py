import time

def main():
    tests = [
        ([1,2,3],3),
        ([1,2,3,4,1,12],5),
        ([1,2,4,3,1],3),
        ([1,2,4,3,0],3),
        ([5,4,3,2,1],1),
        ([5,4,3,2,1,6],2),
    ]
    tests.extend([([x for x in range(y)],y) for y in range(15,23)])
    memoized = lambda: LISmax(dict())
    unmemoized = lambda: LISmaxWithoutMemo
    run_tests(tests, memoized, "memoized")
    run_tests(tests, unmemoized, "unmemoized")

def LIS(arr,n,f):
    max = 0
    for i in range(n+1):
        tmp = f(arr,i)
        if tmp > max:
            max = tmp
    return max

memo = dict()
def LISmax(memo):
    def inner(arr,n):
        if n == 0:
            return 1
        if n in memo:
            return memo[n]
        max = 0
        for i in range(n):
            if arr[i] < arr[n]:
                tmp = inner(arr, i)
                if tmp > max:
                    max = tmp
        memo[n] = max+1
        return memo[n]
    return inner

def LISmaxWithoutMemo(arr,n):
    if n == 0:
        return 1
    max = 0
    for i in range(n):
        if arr[i] < arr[n]:
            tmp = LISmaxWithoutMemo(arr, i)
            if tmp > max:
                max = tmp
    return max+1

def run_tests(tests, gen_f, name):
    count = 0
    print(f"{name} tests")
    start = time.time()
    for test in tests:
        test_start = time.time()
        lst = test[0]
        res = LIS(lst,len(lst)-1,gen_f())
        if res != test[1]:
            print(lst,len(lst)-1)
            print(f"test {count} failed: got {res} vs. expected{test[1]}")
        count += 1
        print(f"--- test {count} took {time.time() - test_start} seconds ---")
    print("--- Total: %s seconds ---" % (time.time() - start))
main()