#List creating and searching
end = False 
names = []
for x in range(0,10):
    aname = input("enter first name:")
    names.append(aname)
while not end:
    search = input("enter search name")

    if search == ("End"):
        end = True 
    elif search in names:
        print(search, "was found")
    
    elif search not in names:
        print(search, "was not found")
    






               
