# Accepts input number from user
n = int(input()) 

# UPPER HALF OF DESIGN (from 0 to n-1)
for i in range(n):
    # For every i, prints (n-1) spaces, followed by left half(0 to i-1)
    # then prints right half from i to 0 
    print(*" "*(n-i),*range(i),*range(i, -1, -1))

# LOWER HALF IS THE SAME AS UPPER HALF
# It prints the middle lane from 0 to n-1 and from n to 0. 
# Rememeber i = n = input number for the middle lane. Hence n - i = 0; so no space. 
# Then prints lower half which is same as upper half.  
for i in range(n, -1, -1):
    print(*" "*(n-i),*range(i),*range(i, -1, -1))

