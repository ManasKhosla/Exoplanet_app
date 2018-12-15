from csv import reader

item = input("Enter the planet you want to search about: ")

def csv_search(item):
    with open("oec.csv", "r") as fo:
        read = reader(fo)
        ans = "Not Found"
        for row in read:
            if item in row:
                fo.close()
                return row
    fo.close()
    return ans 
    


print(csv_search(item))
