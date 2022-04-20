import re
import os
from os import error
import argparse
import platform

from clr import colors

lb = "↳"
dlb = "↘"

os.system("")
os_ = platform.system()
print(f"{colors.Lyellow}SYSTEM: {os_}{colors.rst}")
if os_ == "Windows":
    lb = "|_"
    dlb = "|__"
else:
    lb = lb
    dlb = dlb
client_name = input(f"{colors.purple}Name of your Ethernet Client: ")
file_name_raw = input(f"{colors.purple}File you want formated to html for Arduino: ")
file_type = input(f'{colors.purple}File type "html" or "css": ')
skip_comment = input(f"{colors.purple}skip comments? (y/n): ")

if file_type == "css":
    try:
        os.remove("clean.txt")
        print(
            f"{colors.bold}{colors.Lyellow}[!] Previous file: clean.txt has been removed for cleaner file look{colors.rst}"
        )
    except OSError:
        pass
elif file_type == "html":
    try:
        os.remove("fresh.txt")
        print(
            f"{colors.bold}{colors.Lyellow}[!] Previous file: fresh.txt has been removed for cleaner file look{colors.rst}"
        )
    except:
        pass

css_comment_0 = "/*"
css_comment_1 = "*/"

html_comment_0 = "<!--"
html_comment_1 = "-->"

if skip_comment == "y":
    skip_comment = True
elif skip_comment == "n":
    skip_comment = False

### set preset for writing html in arduino file
preset_ln = f'{client_name}.println("'
preset_ = f'{client_name}.print("'
### check if file is .txt
if file_name_raw.endswith(".txt"):
    base = os.path.splitext(file_name_raw)[0]
else:
    ### if its not, rename it to .txt [os.rename()]
    base = os.path.splitext(file_name_raw)[0]
    file_name_change = os.rename(file_name_raw, base + ".txt")

### sets name for file which containins html or css code
new_file_name = f"{base}.txt"
### sets file name in which reformed code will be
reform_file = f"reform_{base}.txt"

### [check] function is used to check if there are  "  in line and if they are it puts \ in front of it so there are no errors
def check(string):
    line = ""
    swap = chr(92)
    swap = str(swap)
    for i, w in enumerate(string):
        if w == '"':
            line = line + swap + w
        else:
            line = line + w
    # line=re.sub('"','\\\"', string)
    return line


### tries to open file
try:
    file = open(new_file_name, "r")
    print(f"{colors.green}{colors.bold}[↣ ] File successfully opened{colors.rst}")
except IOError:
    print(f"{colors.red}{colors.bold}{new_file_name} could not be opened{colors.rst}")


### opens a reform_file
write = open(reform_file, "a+")
line_num = 0

if file_type == "html":
    ### goes through lines and reforms them so they can be pasted in arduino
    style_lines = []
    comment_lines = []
    for line in file:
        comment = False
        line_num += 1
        line_ = line
        line_clean = check(line_)
        # makes shore its not a blank line
        if line_.startswith("<") or line_.startswith(" "):
            if html_comment_0 in line_:
                if skip_comment:
                    write.write("")
                    comment = True
                    print(f"   [{dlb}]  Comment ignored")
                elif not skip_comment:
                    to_write = "// " + line_
                    write.write(to_write)
                    comment = True
                    print(f"   [{dlb}]  Comment added")
            if comment == False:
                if "." in line_ and "{" in line_clean:
                    style_lines.append(line_clean)
                if ";" in line_clean:
                    style_lines.append(line_clean)
                if "}" in line_ and style_lines:
                    to_file = ""
                    for sl in style_lines:
                        to_file = to_file + sl
                    to_write = preset_ln + to_file + '");'
                    write.write(str(to_write.rsplit("\n")))
                    write.write("\n")
                    style_lines.clear()
                if "<" in line_clean:
                    line_ref = preset_ + line_clean
                    line_ref = line_ref + '");'
                    write.write(str(line_ref.rsplit("\n")))
                    write.write("\n")
                    print(f"{colors.Lgreen}  [{lb}]  success reformed line")
            else:
                print(
                    f"{colors.yellow}[ignore] Warning failed to reform at line :{line_num}"
                )
    print(f"{colors.Lblue}[>]  File reformed, cleaning it up now :) [<]")


elif file_type == "css":
    file_mem = []
    group_line = []
    line_num = 0
    comment_lines_css = []
    for line in file:
        comment = False
        file_mem.append(line)
        line_num += 1
        line_a = line
        line_ = check(line_a)
        if line_num == 0:
            old_num = 0
        else:
            old_num = line_num - 1
        old_line = file_mem[old_num]
        ### if line ends with any of down bellow listed characters is applied,
        ### that there will be at least one more line connected to this so we put it in the same file line

        ### comments still not work

        if comment == False:
            if "," in line_:
                line_ = str(line_.rsplit("\n"))
                group_line.append(line_)
                print(f"{colors.Lgreen} [{lb}]  success reformed line")
            if "{" in line_:
                line_ = str(line_.rsplit("\n"))
                group_line.append(line_)
                print(f"{colors.Lgreen} [{lb}]  success reformed line")
            if ";" in line_:
                line_ = str(line_.rsplit("\n"))
                group_line.append(line_)
                print(f"{colors.Lgreen} [{lb}]  success reformed line")
            if line_.startswith(":"):
                line_ = str(line_.rsplit("\n"))
                group_line.append(line_)
                print(f"{colors.Lgreen} [{lb}]  success reformed line")
            if "@" in line_:
                line_ = str(line_.rsplit("\n"))
                group_line.append(line_)
                print(f"{colors.Lgreen} [{lb}]  success reformed line")
            if "*" in line_:
                line_ = str(line_.rsplit("\n"))
                group_line.append(line_)
                print(f"{colors.Lgreen} [{lb}]  success reformed line")
            if "/*" in line_:
                pass

            ### if line ends with '}' its assumed that the current block of code has ended;
            ### in this case if there was any code above that belongs to set block it all combines it together
            ### and adds it to the file in the same line with preset_ln
            if "}" in line_ and group_line:
                to_file = ""
                for i in range(len(group_line)):
                    to_file = to_file + " " + group_line[i]
                to_file = to_file + " " + "}" + '");'
                for_write = preset_ + to_file
                # write.write(str(for_write.rsplit('\n')))
                write.write(for_write)
                write.write("\n")
                group_line.clear()

            else:
                line_write = line_
                write.write(str(line_write.rsplit("\n")))
                write.write("\n")
                print(
                    f"{colors.yellow}[ignore]  Warning (but probably fine) fail to reform at line :{line_num}"
                )
            ### when the line starts with blank space and does not end with  ';' (is assumed that the previous block of code has ended,
            ###     and the new block will bigene so it clears the list)
            if line_.startswith(" ") and not line_.endswith(";"):
                group_line.clear()
            else:
                pass
        else:
            pass

### FOR CLEANING THE FILE UP ###
reform_file = reform_file

### tries to open reformated version of the file
try:
    recheck = open(reform_file, "r+")
    # print("opened")
except IOError:
    pass
    # print("unable to read")

### creates fresh.txt file where clean reformated code will be
write = open("fresh.txt", "a+")
if file_type == "css":
    css_clean = open("mid_clean.txt", "a+")
else:
    pass
print(f"{colors.cyan}[]   Cleaning up")


### Cleans the code up using string.replace() function
for line in recheck:
    line__ = line
    line_1_1 = line__.replace("', '", "")
    line_1_1 = line_1_1.replace("']", "")
    line_1_1 = line_1_1.replace("\\\\", "\\")
    line_1_1 = line_1_1.replace("['", "")
    line_1_1 = re.sub(" +", " ", line_1_1)
    if file_type == "css":
        ### if code type is css >
        # line_1_1=line_1_1.replace("[\'","")
        css_clean.write(line_1_1)
    else:
        write.write(line_1_1)


### IF CODE TYPE IS CSS ###
if file_type == "css":
    css_clean.close
    css_clean = open("mid_clean.txt", "r")

### if there are any lines that are not propaly formated this removes them
if file_type == "css":
    s = client_name[0]
    for line in css_clean:
        if line.startswith(s):
            write.write(line)
        else:
            write.write(" ")
    write.close

### removes all blank spaces in code
if file_type == "css":
    write2 = open("clean.txt", "a+")
    write = open("fresh.txt", "r")
    for line in write:
        cl = re.sub(" +", "", line)
        write2.write(cl)
    write2.close


### CLOSING FILES ###
if file_type == "css":
    ### if code is css it needs an extra file to clean it up, so here it removes the set file
    os.remove("fresh.txt")
    os.remove("mid_clean.txt")
else:
    pass


### closes open files
recheck.close
write.close
### removes the dirty file
os.remove(reform_file)


print(
    f"{colors.Lgreen}SUCCESSFULLY CLEANED{colors.rst}\nYour cleanned file is fresh.txt"
)
