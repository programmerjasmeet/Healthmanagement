import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if (k==1):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("harry-ex.txt","a") as op: #append data
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif (c==2):
            value = input("type here\n")
            with open("harryex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("succesfully written")
    elif (k==2):
            c = int(input("enter 1 for excersise and 2 for food"))
            if (c == 1):
                value = input("type here\n")
                with open("hammadf.txt",a) as op:
                    op.write(str([str(gettime())]) + ";" + value + "\n")
                print("succesfully written")
            elif (c == 2):
                value = input("type here\n")
                with open("hammadex.txt",a) as op:
                    op.write(str([str(gettime())]) + ";" + value + "\n")
                print("succesfully written")
    elif (k==3):
            c = int(input("enter 1 for excersise and 2 for food"))
            if (c == 1):
                value = input("type here\n")
                with open("jasmeetf.txt",a) as op:
                    op.write(str([str(gettime())]) + ";" + value + "\n")
                print("succesfully written")
            elif (c == 2):
                value = input("type here\n")
                with open("jasmeetex.txt",a) as op:
                    op.write(str([str(gettime())]) + ";" + value + "\n")
                print("succesfully written")
    else: print("enter the valid option")

def retrive(k):
    if (k==1):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("harryf.txt") as op: #read is default
                for i in op:
                    print(i,end="")
        elif (c==2):
                  with open("harryex.txt") as op:
                      for i in op:
                          print(i,end="")
    elif (k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
                with open("hammadf.txt") as op:
                    for i in op:
                        print(i, end="")
        elif (c == 2):
                            with open("hammadex.txt") as op:
                                for i in op:
                                    print(i, end="")
    elif (k==3):
            c = int(input("enter 1 for excersise and 2 for food"))
            if (c == 1):
                with open("jasmeetf.txt") as op:
                    for i in op:
                        print(i, end="")
            elif (c == 2):
                with open("jasmeetex.txt") as op:
                    for i in op:
                        print(i, end="")
    else:
          print("enter the valid input 1 for haary 2 hamad 3 for jasmeet")


print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for harry 2 for rohan 3 for jasmeet "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for jasmeet "))
    retrive(b)
