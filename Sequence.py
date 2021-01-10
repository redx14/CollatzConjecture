#Andrey Ilkiv midterm exam question 3

integer = int(input("Please enter a positive integer: "))
steps = 0
greatestint = 0
secondgreatest = 0
getstepS = 0
getstepG = 0

if integer != 1 :
    while integer < 0 :
        integer = int(input("Please enter a positive integer: "))
    if integer != 0:    
        while integer != 1 :
            if greatestint < integer :
                greatestint = integer
                getstepG = steps
            if integer < greatestint and secondgreatest < integer :
                secondgreatest = integer
                getstepS = steps
            steps += 1
            if integer % 2 == 0:
                isOdd = False
            else:
                isOdd = True
                
            if isOdd == True :
                integer = (integer * 3) + 1
            else:
                integer = integer / 2
    if integer != 0:                
        print("It took" , steps , "steps for the sequence to reach 1.")
        print("The largest number in the sequence was" , greatestint , "(step =" , getstepG , ").")
        print("The second largest number was" , int(secondgreatest) , "(step =" , getstepS , ").")
else:
    greatestint = 1
    secondgreatest = 1
    print("The largest number in the sequence was" , greatestint , "(step =" , getstepG , ").")
    print("The second largest number was" , int(secondgreatest) , "(step =" , getstepS , ").")
