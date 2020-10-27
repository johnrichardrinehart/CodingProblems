def main():
    wobt_tests()
    worp_tests()

def wobt_tests():
    tests = [
        ([1,2,], [[1,2],[2,1],]),
        ([1,1,],[[1,1,],[1,1],]),
        ([1,2,3,], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2],])
    ]

    for i in range(len(tests)):
        test = tests[i]
        results = []
        result = without_backtracking(test[0], 0, results)
        if result != test[1]:
            print(f"Failed: without_backtracking test {i}! Got {result}, expected {test[1]}")
        else:
            print("Passed: wobt test {i}")

def without_backtracking(arr, depth, results):
    if depth == len(arr):
        results.append(arr[:])
    for i in range(depth, len(arr)):
        # swap the ith and depth-th values
        tmp = arr[i]
        arr[i] = arr[depth]
        arr[depth] = tmp
        without_backtracking(arr,depth+1, results)
        # backtrack
        arr[depth] = arr[i]
        arr[i] = tmp
    return results

def worp_tests():
    tests = [
        # ([1,2,], [[1,2],[2,1],]),
        ([1,1,],[[1,1,],]),
        ([1,1,2], [[1,1,2],[1,2,1],[2,1,1],],),
        (["a","b","a"],[["a","a","b"],["a","b","a"],["b","a","a",],],),
    ]
    for i in range(len(tests)):
        test = tests[i]
        results = []
        result = without_repeats(test[0], 0, results)
        if result != test[1]:
            print(f"Failed: without_repeats test {i}! Got {result}, expected {test[1]}")
        else:
            print(f"Passed: worp test {i}")
    
def without_repeats(arr, depth, results):
    m = dict()
    vals, counts = [],[]
    for val in arr:
        cnt = m.get(val,0)
        m[val] = cnt + 1
    for k in m:
        vals.append(k)
        counts.append(m[k])
    
    def loop(values, counts, arr, j, n, results):
        if j == n:
            results.append(arr[:])
            return
        for i in range(0, len(values)):
            if counts[i] > 0:
                if len(arr) > j:
                    arr[j] = values[i]
                else:
                    arr.append(values[i])
                counts[i] -= 1
                loop(values, counts, arr, j+1, n, results)
                counts[i] += 1 # restore it
        return results
    
    return loop(vals, counts, [], 0, sum(counts), results)

main()