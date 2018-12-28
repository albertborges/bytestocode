file = open("gvmlhexdata.txt", "r") 
str = file.read()
bytearr = str.split(" ")
code = "{"
for byte in bytearr:
    code+="0x"
    code+=byte
    code+=","
code = code[:len(code)-1]
code+="}"

print code