import speech_recognition as s_r


def get_string():
    mic = s_r.Recognizer()
    my_mic_device = s_r.Microphone(device_index=1)
    with my_mic_device as source:
        print("Say what you want regarding Basic Programs")
        mic.adjust_for_ambient_noise(source)
        audio = mic.listen(source)
    try:
        my_string = mic.recognize_google(audio)
    except:
        print("pronounce correctly")
        print("\n ------------------------------------------------------ \n")
        my_string = 1
    return my_string

def get_armstrong(lower,upper):
    a = []
    for num in range(lower, upper + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            a.append(num)
    print(a)
    print("\n ------------------------------------------------------ \n")
        

def get_palin(lower,upper):
    p = []
    for num in range(lower, upper + 1):
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            p.append(rev)
    print(p)
    print("\n ------------------------------------------------------ \n")
        

def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num == sum:
       print(num,"is an Armstrong number")
       print("\n ------------------------------------------------------ \n")
    else:
       print(num,"is not an Armstrong number")
       print("\n ------------------------------------------------------ \n")

def get_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
    print("\n ------------------------------------------------------ \n")

def get_factorial(num):
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
       print("\n ------------------------------------------------------ \n")
    elif num == 0:
       print("The factorial of 0 is 1")
       print("\n ------------------------------------------------------ \n")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)
       print("\n ------------------------------------------------------ \n")

def is_year(year): 
    import calendar
    if (calendar.isleap(year)):  
        print("Yes,It's a leap Year")
        print("\n ------------------------------------------------------ \n")

    else:  
        print("No,It's not a Leap Year")
        print("\n ------------------------------------------------------ \n")

def is_palin(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
        print("\n ------------------------------------------------------ \n")
    else:
        print("Not a palindrome!")
        print("\n ------------------------------------------------------ \n")

def get_alphabet(n): 
    num = 65 
    for i in range(0, n):  
        for j in range(0, i+1):  
            ch = chr(num) 
            print(ch, end=" ") 
        num = num + 1
        print("\r")
    print("\n ------------------------------------------------------ \n")
def get_num(n):   
    num = 1 
    for i in range(0, n): 
        num = 1
        for j in range(0, i+1): 
            print(num, end=" ")  
            num = num + 1 
        print("\r")
    print("\n ------------------------------------------------------ \n")

def get_triangle(n):  
    k = 2*n - 2 
    for i in range(0, n):  
        for j in range(0, k): 
            print(end=" ")  
        k = k - 1 
        for j in range(0, i+1): 
            print("* ", end="")  
        print("\r") 
    print("\n ------------------------------------------------------ \n")

def get_right(n): 
       
    k = 2*n - 2
  
    for i in range(0, n): 

        for j in range(0, k): 
            print(end=" ")  
        k = k - 2
        for j in range(0, i+1):  
            print("* ", end="")  
        print("\r")
    print("\n ------------------------------------------------------ \n")
        
def get_left(n): 
    for i in range(0, n): 
        for j in range(0, i+1):
            print("* ",end="") 
        print("\r")
    print("\n ------------------------------------------------------ \n")

def get_fibonacci(n):
    n1, n2 =0, 1
    count = 0
    f = []
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < n:
        f.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(f)
    

def get_evens(n1, n2):
    e = []
    for i in range(n1, n2+1):
        if(i % 2 == 0):
            e.append(i)
    print(e)
    print("\n ------------------------------------------------------ \n")
    
def get_odds(n1, n2):
    o = []
    for i in range(n1, n2+1):
        if(i % 2 == 1):
            o.append(i)
    print(o)
    print("\n ------------------------------------------------------ \n")
    
def is_odd(i):
    if( i % 2 != 0):
        print(i, "is a odd number")
        print("\n ------------------------------------------------------ \n")
    else:
        print(i, "is not a odd number")
        print("\n ------------------------------------------------------ \n")

def is_even(i):
    if( i % 2 == 0):
        print(i, "is a even number")
        print("\n ------------------------------------------------------ \n")
    else:
        print(i, "is not a even number")
        print("\n ------------------------------------------------------ \n")

def isprime(i):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0

def get_primes(n1, n2):
    p = []
    for i in range(n1,n2+1):
        result = isprime(i)
        if(result == 1):
            p.append(i)
    print(p)
    print("\n ------------------------------------------------------ \n")

c = 0
while(c != 1):
    my_string = get_string()
    if (my_string == "exit"):
        print("\nSee yaa\n")
        c = 1
    elif (my_string == 1):
        continue
    else:
        print("\n",my_string,"\n")
        l = my_string.split(" ")
        if(("f***" in l) or ("bitch" in l) or ("a******" in l) or ("shit" in l)):
            print("\nDon't use unparliamentary language\n")
            break
        else:
            values = []
            for i in l:
                try:
                    a = int(i)
                except:
                    continue
                values.append(a)
            if(("prime" in l) or ("prime" in l)):
                if(("range" in l) or ("between" in l) and ("numbers" in l)):
                    get_primes(min(values),max(values))
                elif(len(values) == 1):
                    res = isprime(values[0])
                    if res == 1 :
                        print(values[0], "is a prime number")
                        print("\n ------------------------------------------------------ \n")
                    else:
                        print(values[0], "is not a prime number")
                        print("\n ------------------------------------------------------ \n")
            elif("even" in l):
                if(("range" in l) or ("between" in l) and ("numbers" in l)):
                    get_evens(min(values),max(values))
                elif(len(values) == 1):
                    is_even(values[0])
            elif("odd" in l):
                if(("range" in l) or ("between" in l) and ("numbers" in l)):
                    get_odds(min(values),max(values))
                elif(len(values) == 1):
                    is_odd(values[0])
            elif(("fibonacci" in l) or ("Fibonacci" in l) ):
                if(len(values) == 1):
                    get_fibonacci(values[0])
            elif(("pattern" in l) or ("Pattern" in l)):
                if(("left" in l) or ("Left" in l)):
                    get_left(values[0])
                elif(("right" in l) or ("Right" in l)):
                    get_right(values[0])
                elif(("centre" in l) or ("Centre" in l)):
                    get_triangle(values[0])
                elif(("number" in l) or ("Number" in l)):
                    get_num(values[0])
                elif(("alphabet" in l) or ("Alphabet" in l)):
                    get_alphabet(values[0])
            elif(("palindrome" in l) or ("Palindrome" in l)):
                if(("range" in l) or ("between" in l) or("Range" in l) or ("Between" in l)):
                    get_palin(min(values),max(values))
                else:
                    if(len(values) == 1):
                        is_palin(values[0])
                    else:
                        for i in range(0,len(values)):
                            is_palin(values[i])
            elif(("leap" in l) or ("Leap" in l)):
                if(len(values) == 1):
                    is_year(values[0])
                else:
                    for i in range(0,len(values)):
                        is_year(values[i])
            elif(("factorial" in l) or ("Factorial" in l)):
                if(len(values) == 1):
                    get_factorial(values[0])
                else:
                    for i in range(0,len(values)):
                        get_factorial(values[i])
            elif(("factors" in l) or ("Factors" in l)):
                if(len(values) == 1):
                    get_factors(values[0])
                else:
                    for i in range(0,len(values)):
                        get_factors(values[i])
            elif(("armstong" in l) or ("Armstrong" in l)):
                if(("range" in l) or ("between" in l) or("Range" in l) or ("Between" in l)):
                    get_armstrong(min(values),max(values))
                else:
                    if(len(values) == 1):
                        is_armstrong(values[0])
                    else:
                        for i in range(0,len(values)):
                            is_armstrong(values[i])
