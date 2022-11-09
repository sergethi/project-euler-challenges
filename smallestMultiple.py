# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.


# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# from 1 to 10 => 2450 is the smallest number
# from 1 to  4
# cur = 7
# cur// 1, cur//2, cur //3 cur//4

#range 1 to 20
def smallMultiple():
    cur = 1 # because any number between 1 and 19 is not divible by 20
    while cur:
        boolCheck = True
        for i in range(1, 20+1):
            if cur % i != 0:
                boolCheck = False
                break
        if boolCheck:
            return cur
        cur += 1
print(smallMultiple())

#0(n) time
#0(1) space
            
