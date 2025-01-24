import os
try:

    filename=input("enter name of the file")
    file=open("filename","r")
    data=file.read
    print(data)
    new_filename=open("NewFile","w")
    for line in filename:
        new_filename.write(line)
except FileNotFoundError:
    print(f"file {filename} not found")
except Exception as e:
    print(f"An error occured {e}")


if __name__=="__main__":
   filename=input("enter name of file")