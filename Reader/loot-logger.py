path = r"C:\Users\Akabane Bussan 48\Downloads\loot.bin"

file=open(path,"rb")
number=list(file.read())
print (number)
file.close()