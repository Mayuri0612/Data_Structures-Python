# ugly umber are those numbers which is inly divisible by 2,3 and 5

# Function to get the nth ugly number 
def getNthUglyNo(n): 
  
    ugly = [0] * n # To store ugly numbers 
  
    # 1 is the first ugly number 
    ugly[0] = 1
  
    # i2, i3, i5 will indicate indices for 2,3,5 respectively 
    i2 = i3 =i5 = 0
  
    # set initial multiple value 
    nextmul2 = 2
    nextmul3 = 3
    nextmul5 = 5
  
    # start loop to find value from ugly[1] to ugly[n] 
    for l in range(1, n): 
  
        # choose the min value of all available multiples 
        ugly[l] = min(nextmul2, nextmul3, nextmul5) 
  
        # increment the value of index accordingly 
        if ugly[l] == nextmul2: 
            i2 += 1;
            nextmul2 = ugly[i2] * 2
  
        if ugly[l] == nextmul3: 
            i3 += 1;
            nextmul3 = ugly[i3] * 3
  
        if ugly[l] == nextmul5:  
            i5 += 1;
            nextmul5 = ugly[i5] * 5

    return ugly[-1] 
  
def main(): 
  
    n = int(input());
    print(getNthUglyNo(n) )

if __name__ == '__main__': 
    main()