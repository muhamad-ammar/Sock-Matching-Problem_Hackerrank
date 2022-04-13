from collections import Counter

# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
def sockMerchant(n, ar):
    # Count each color socks in a pile
    res=Counter(ar)
    # count
    count=0
    # Iterate through the dictionary res
    for key in res:
        # If number of socks of a color is even
        if res[key]%2==0:
            count+=(res[key])/2
        # If number of socks of a color is Odd
        else:
            count+=(res[key]-1)/2
    return int(count)
n=input("Eneter the number of socks")
ar=input("Enter color of Socks in array")
print(sockMerchant(n,ar))