#function that takes n and converts it into stair case made of ### to right
def mario_stairs(n):
    i = 0
    s = n
    while i !=n:
        i+=1
        s-=1
        stairs =' '*s +"#"*i
        print(stairs)
    

#prompt user fo input if a number n (int)
n = int(input("Enter the number of stairs you would like to make for mario:"));
(mario_stairs(n))

