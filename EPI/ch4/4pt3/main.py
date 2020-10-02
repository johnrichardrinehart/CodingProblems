import time
import uuid

def main():
  # cases = [
  #   (0xFFFFFFFFAAAAAAAA,0x55555555FFFFFFFF),
  #   (0x55555555AAAAAAAA,0x55555555AAAAAAAA),
  #   (0xFF00000000000000,0x00000000000000FF),
  #   (0xFFFF000000000000,0x000000000000FFFF),
  #   (0xFFFFFF0000000000,0x0000000000FFFFFF),
  #   (0xFFFFFFFF00000000,0x00000000FFFFFFFF),
  #   (0xFFFFFFFFFF000000,0x000000FFFFFFFFFF),
  #   (0xFFFFFFFFFFFF0000,0x0000FFFFFFFFFFFF),
  # ]
  cases = []

  for _ in range(10**5):
    num = uuid.uuid4().int & (1<<64)-1
    cases.append((num, reversen(num,64)))

  start = time.time()
  for fwd, rev in cases:
    obt = reverse1(fwd)
    if rev != obt:
      print("Naive reverse failed. Got: ", obt, ". Expected: ", rev)
  print(time.time()-start)
  
  start = time.time()
  for fwd, rev in cases:
    obt = reverse2(fwd)
    if rev != obt:
      print("LUT reverse failed. Got: ", obt, ". Expected: ", rev)
  print(time.time()-start)
  print("all done!")

def reversen(n,m):
  # simple case
  if n == 0:
    return 0    
  
  # initialize local variables
  res = 0
  i = 0
  while (i < m):
    res |= ((n % 2) << ((m-1)-i))
    n >>= 1
    i += 1
  
  return res

# https://stackoverflow.com/a/16660062
# assumes that the bit string is fine to be interpreted as a number, not an array. We can add a num2array method to actually reverse the "bits" and add an array2num method to convert the input from one form to the other...
def reverse1(n):
  return reversen(n,64)

lut = dict()
CHUNK_SIZE=16
MASK = 2**(CHUNK_SIZE)-1
for key in range(1<<CHUNK_SIZE):
  lut[key] = reversen(key,CHUNK_SIZE)

# reverse2: Book's solution
# Use a LUT to maintain a list of common bit-swapping key-value pairs
def reverse2(n):
  res = 0
  if n == 0:
    return res

  for chunk in range(64//CHUNK_SIZE):
    res |= lut[(n>>(CHUNK_SIZE*chunk)) & MASK] << (64-(chunk+1)*CHUNK_SIZE)
  return res

main()