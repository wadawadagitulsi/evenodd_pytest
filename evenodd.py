import sys 
def evenodd(num):
    return f"num:{num}"

if __name__ == "__main__" :
 num =int(sys.argv[1])
 evenodd(num)

 if(num%2==0):
    print ("Even")
else:
    print("Odd")