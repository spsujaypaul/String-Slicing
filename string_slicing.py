import time 

def time_gap():
    print("Please wait",end = " ")
    for i in range(5):
        time.sleep(1)
        print(".", end=" ")

print("\nEnter String Sclicing \n")
while True :
    inp = input("\nDo you want to continue !(Y|N) : ")
    if inp == "Y" or inp =="y":
        x = None
        y = None
        z = None
        statement = input("Enter Your string :")
         
        
        print("\nEnter Some Details")
        time_gap()
        x = input("\nEnter start point :") or x == 0
        y = input("Enter stop point :") or y == 0
        z = input("Enter gap point :") or z == 0

        if x is False:
            y = int(y)
            z = int(z)
            time_gap()
            print(statement[:y:z])
        elif y is False:
            x = int(x)
            z = int(z)
            try:
                time_gap()
                print(statement[x::z])
            except Exception as e:
                time_gap()
                print("Stop value is mandatory")
        elif z is False:
            x = int(x)
            y = int(y)
            time_gap()
            print(statement[x:y])
      
        else:
            x = int(x)
            y = int(y)
            z = int(z)
            time_gap()
            print(statement[x:y:z])
    else:
        exit(0)