import os

def parsefiles(file_in, file_out):
    count = 0
    while True:
        count += 1
        line = file_in.readline()
        if not line:
            break
        if line[0] == '0':
            line = line[:-1]  #remove newline
            #split by spaces, 1=ID, 2=data separated by '/', 3=time H:M:S.ms 
            line_sp = line.split()
            if len(line_sp) < 4:
                continue

            line_sp[3] = line_sp[3].replace(".",":")
            output = "" + line_sp[3] + ";"
            line_sp[1] = line_sp[1].zfill(4)
            output += "0x" + line_sp[1] + ";8;" #now we just need to add data

            data = line_sp[2].split('/')
            for segment in data:
                segment = segment.zfill(2)
                output += segment
            file_out.writelines(output + "\n")
            #print(output)


file_in = open("nongps03-13_03-01.txt", 'r')
file_out = open("parsed/parsed03-13.txt", 'w')
for filename in os.listdir('./'):
    if filename.startswith("nongps"):
        file_in = open(filename, 'r')
        file_out = open("./parsed/" + filename, 'w')
        parsefiles(file_in, file_out)
        file_in.close()
        file_out.close()
#parsefiles(file_in, file_out)
count = 0


file_in.close()
file_out.close()

