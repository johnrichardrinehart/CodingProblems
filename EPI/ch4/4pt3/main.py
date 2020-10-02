def main():
  cases = [
  (0b1101,0b1011),
  (0b1001,0b1001),
  (0b0,0b0),
  (0b1,0b1),
  (0b1101101, 0b1011011),
  (0b101<<12, 0b101),
]

  print("testing it takin's edit...")
  for fwd, rev in cases:
    if rev != reverse1(fwd):
      print("uh oh. Got: ", reverse1(fwd), ". Expected: ", rev)
  print("all done!")

# https://stackoverflow.com/a/16660062
# assumes that the bit string is fine to be interpreted as a number, not an array. We can add a num2array method to actually reverse the "bits" and add an array2num method to convert the input from one form to the other...
def reverse1(n):
  # initialize local variables
  res = 0
  cursor = 0
  num_bits = 0

  # how many bits
  if n == 0:
    return 0    

  tmp = n
  while (tmp !=0):
    tmp >>= 1
    num_bits += 1
  
  while (n != 0):
    idx = num_bits - (cursor + 1)
    res += ((n % 2) << idx)
    n >>= 1
    cursor += 1
  return res

# reverse2: Book's solution
# Use a LUT to maintain a list of common bit-swapping key-value pairs
def reverse2(n):
  lut = dict()
  for key in range(2<<16-1):
    lut[key] = reverse1(key)
  print(lut)
  
main()