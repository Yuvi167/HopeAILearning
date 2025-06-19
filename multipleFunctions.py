class MultipleFunctions():
    def Subfields():
        print("Sub-fields in AI are: ")
        print("Machine Learing \nNeural Networks \nVision \nRobotics \nSpeech Processing \nNatural Language Processing")

    def OddEven():
        num=int(input("Enter the number to check: "))
        if num%2==0:
            print(f"Enter {num} is even number")
        elif num%2==1:
            print(f"Enter {num} is odd number")
        else:
            pass

    def eligible(gender, age):
        print("Gender: ", gender)
        print("Age: ", age)
        if (gender=='Male' and age>=21):
            Val='ELIGIBLE'
        elif (gender=='Female' and age>=18):
            Val='ELIGIBLE'
        else:
            Val='NOT ELIGIBLE'
        return Val

    def percentage(num):
        print(f"Number of subject is {num}")
        add = []
    
        for i in range(num):
            mark=float(input(f"Enter Subject mark{i+1}: "))
            add.append(mark)

        total=sum(add)
        print(f"Total marks: {total}")
        per = total / num
        print(f"Percentage: {per}")
        return

    def triangle():
        Hei = int(input("Height: "))
        Bre = int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", (Hei*Bre)/2)
        Hei1 = int(input("Height1: "))
        Hei2 = int(input("Height2: "))
        Bre = int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", Hei1+Hei2+Bre)