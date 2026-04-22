try:
    with open("./Data/sample1.txt") as fh:
    #data = fh.read()
    # data = fh.readline()
        data = fh.readlines()
        print(data)

except FileNotFoundError:
    print("File doesnot exist")