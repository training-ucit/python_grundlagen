

def lotto () :
    seq = []

    while len(seq) < 6 :
        try:
            num = int(input("Enter number please: "))
            if num not in range (1, 49) :
                print ("Value must be between 1 and 49")
            else :    
                if num in seq :
                    print ("Duplicate value")
                else :
                    seq.append(num)
        except Exception as e:
            print ("Wrong input, repeate please")
    seq.sort()
    return seq

if __name__ == "__main__":
    arr = lotto ()
    print (type(arr))
    print ("Test ", *arr)