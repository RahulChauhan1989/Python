import os

#with open("text.txt","w") as W:
    #W.write("Data Automation1")
with open("text.txt","r") as R:
    with open("text_copy.txt","w") as W:
        for line in R:
         W.write(line)

#os.makedirs("Test_Directory")
#os.removedirs("Test_Directory")
#print(os.__file__)
#print(os.listdir())
#print(os.path.split(os.getcwd()))
#print(os.path.splitext("text.txt"))
#print(os.path.exists("text.txt"))
#print(os.path.isdir("Test_Directory"))
#print(os.stat("text.txt"))

if not os.path.isdir("Test_Directory"):
    os.makedirs("Test_Directory")
    print("Directory Created Successfully")
else:
    print("Directory ALready Present")


#print(os.getcwd())
