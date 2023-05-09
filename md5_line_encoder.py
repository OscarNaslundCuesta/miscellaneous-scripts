import hashlib

with open("ctf/clear.txt", "r") as input:
    lines = input.readlines()


for line in lines:
    line = line.strip()
    result = hashlib.md5(f"{line}".encode("utf-8")).hexdigest()
    
    f = open("ctf/output.txt", "a")
    f.write(result + "\n")
    f.close()
    