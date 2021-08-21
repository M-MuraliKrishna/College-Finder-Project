import os

def renamer():
    i = 0 # initiate/iterate over files or lists
    path = "D:/CF-DS/Project 6.0 goodRenamer Files/img/"
    for filename in os.listdir(path):
        names = f"pic {i}.jpg"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()

