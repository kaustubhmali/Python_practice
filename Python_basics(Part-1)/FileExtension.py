filename = input("Enter file name: ")
extension = filename.split(".")
print(f"Extension: {extension[1]}")

print ("The extension of the file is : " + repr(extension[-1]))