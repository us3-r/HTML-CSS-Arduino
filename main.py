import re
import os
import sys
import argparse
from clr import colors

os.system("")

pp=argparse.ArgumentParser(description="Commands for program")

pp.add_argument('-c',help="Name of your Ethernet Client ", type=str, default="client")
pp.add_argument('-f', help="File you want formated to html for Arduino", type=str)
pp.add_argument('-t', help="File type \"html\" or \"css\"", type=str, default="html")

args = pp.parse_args()


client_name = args.c
file_name_raw = args.f

### set preset for writing html in arduino file
preset_ln = f'{client_name}.println(\"'
preset_ = f'{client_name}.print(\"'
### check if file is .txt
if file_name_raw.endswith(".txt"):
    base = os.path.splitext(file_name_raw)[0]
else:
    ### if its not, rename it to .txt [os.rename()]
    base = os.path.splitext(file_name_raw)[0]
    file_name_change = os.rename(file_name_raw, base + '.txt')

### sets name for file which containins html or css code
new_file_name=f'{base}.txt'
### sets file name in which reformed code will be
reform_file=f'reform_{base}.txt'

### [check] function is used to check if there are  "  in line and if they are it pits \ in front of it so there are no errors
def check(string):
    line=""
    swap=chr(92)
    swap=str(swap)
    for i, w in enumerate(string):
        if w == "\"":
            line=line+swap+w
        else:
            line=line+w
    # line=re.sub('"','\\\"', string)
    return line


### tries to open file
try:
    file=open(new_file_name,'r')
    print(f'{colors.green}{colors.bold}File successfully opened{colors.rst}')
except IOError:
    print(f'{colors.red}{colors.bold}{new_file_name} could not be opened{colors.rst}')

### opens a reform_file
write = open(reform_file,'a+')

line_num=0

if args.t == "html":
    ### goes through lines and reforms them so they can be pasted in arduino
    for line in file:
        line_num+=1
        line_=line
        line_clean=check(line_)
        #makes shore its not a blank line
        if line_.startswith('<') or line_.startswith(" "):
            if "<h" in line_clean or "<p" in line_clean:
                line_ref=preset_+line_clean
                line_ref=line_ref+"\");"
                write.write(str(line_ref.rsplit('\n')))
                write.write("\n")
            ### form here till "else:" it checks if it belongs to <style> if it does it changes from println to print so its printed in the same line
            elif "<style>" in line_ or "</style>" in line_:
                line_ref=preset_+line_clean
                line_ref=line_ref+"\");"
                write.write(str(line_ref.rsplit('\n')))
                write.write("\n")
            elif ";" in line_:
                line_ref=preset_+line_clean
                line_ref=line_ref+"\");"
                write.write(str(line_ref.rsplit('\n')))
                write.write("\n")
            elif "." in line_ and "{" in line_:
                line_ref=preset_+line_clean
                line_ref=line_ref+"\");"
                write.write(str(line_ref.rsplit('\n')))
                write.write("\n")
            ### if none of the above arguments are fulfilled it does println
            else:
                line_ref = preset_ln+line_clean
                line_ref=line_ref+"\");"
                write.write(str(line_ref.rsplit('\n')))
                write.write("\n")
            print(f'{colors.green}[↲] success reformed line')
        else:
            print(f'{colors.yellow}[!] Warning failed to reform at line :{line_num}')
    print(f'{colors.blue}[>] File reformed, cleaning it up now :) [<]')

### /\ till here is ok

elif args.t == "css":
    print(f'{colors.red}wrong way {colors.rst}')
    file_mem = []
    group_line = []
    line_num = 0
    for line in file:
        file_mem.append(line)
        line_num+=1
        line_a=line
        line_=check(line_a)
        if line_num == 0:
            old_num=0
        else:
            old_num=line_num-1
        old_line=file_mem[old_num]
        ### if line ends with ',' is applyed that there will be at least one more line connected to this so we put it in the same file line
        if ',' in line_:
            line_=str(line_.rsplit('\n'))
            group_line.append(line_)
            print(f'{colors.green}[↲] success reformed line')

        if '{' in line_:
            line_=str(line_.rsplit('\n'))
            group_line.append(line_)
            print(f'{colors.green}[↲] success reformed line')

        if  ';' in line_:
            line_=str(line_.rsplit('\n'))
            group_line.append(line_)
            print(f'{colors.green}[↲] success reformed line')

        if '}' in line_ and group_line:
            to_file=""
            for i in range(len(group_line)):
                to_file=to_file+" "+group_line[i]
            to_file=to_file+" "+"}"+"\");"
            for_write=preset_ln+to_file
            #write.write(str(for_write.rsplit('\n')))
            write.write(for_write)
            write.write("\n")
            group_line.clear()

        else:
            line_write=line_
            write.write(str(line_write.rsplit('\n')))
            write.write("\n")
            print(f'{colors.yellow}[!] Warning (but probably fine) to reform at line :{line_num}')

        if line_.startswith(" ") and not line_.endswith(';'):
            group_line.clear()
        else:
            pass
### FOR CLEANING THE FILE UP ###
reform_file=reform_file

### tries to open reformated version of the file
try:
    recheck=open(reform_file,'r+')
    #print("opened")
except IOError:
    pass
    #print("unable to read")

### creates fresh.txt file where clean reformated code will be
write=open("fresh.txt","a+")
css_clean=open("mid_clean.txt","a+")
print(f'{colors.cyan}Cleaning up')



### Cleans the code up using string.replace() function
for line in recheck:
    line__=line
    line_1_1=line__.replace("\', \'","")
    line_1_1=line_1_1.replace("\']", "")
    line_1_1=line_1_1.replace("\\\\","\\")
    line_1_1=re.sub(' +','',line_1_1)
    if args.t == "css":
        line_1_1=line_1_1.replace("[\'","")
        css_clean.write(line_1_1)
    else:
        write.write(line_1_1)

css_clean.close
css_clean=open("mid_clean.txt","a+")

if args.t == "css":
    for line in css_clean:
        if str(client_name) not in line:
            write.write(" ")
        else:
            write.write(line)
    write.close

if args.t == "css":
    write2=open("clean.txt","a+")
    write=open("fresh.txt","r")
    for line in write:
        cl=re.sub(' +','', line)
        write2.write(cl)
    write2.close


### closes both files
if args.t == "css":
    os.remove("fresh.txt")
else:pass

os.remove("mid_clean.txt")
recheck.close
write.close
### removes the dirty file
os.remove(reform_file)

print(f'{colors.green}SUCCESSFULLY CLEANED{colors.rst}\nYour cleanned file is fresh.txt')
