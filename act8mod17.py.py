n=int(input("enter n(try 3 or 5):"))
guess=input("how many times does countdown call itself for n="+str(n)+"?")

input("Recursion - watch each call. press enter to run")
def countdown(num):
    print("call-n=",num)
    if num>0:
        countdown(num-1)
countdown(n)
print("calls =",n+1,"your guess:",guess,"->0(n)")

input("watch calls grow with n. press enter")
for size in[5,10,100]:
    print("n=",size,"calls=",size+2,"=>0(n)")