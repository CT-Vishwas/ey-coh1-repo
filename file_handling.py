try:
    with open("./Data/sample1.txt") as fh:
    #data = fh.read()
    # data = fh.readline()
        data = fh.readlines()
        print(data)

except FileNotFoundError:
    print("File doesnot exist")


try:
     with open("sample1.txt", "r") as fh:              
            data = fh.readlines()
            print(data)
     with open("sample1.txt", "a+") as fh:
            data = fh.writelines("my name is moorthi")
     with open("sample1.txt", "r") as fh:
            data = fh.readlines()
            print(data)
 
except FileNotFoundError:
    print("File doesnot exist")