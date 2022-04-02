# HTML-CSS-Arduino
This is a simple Python script that converts ``` .html ``` or ```.css``` file format to format that can be copied and pasted to .ino files

## Requirements
To run this program you need to have:<br />
~ [Python](https://www.python.org/downloads/)<br />
> If you don't have a package manager such as pip (you should be fine using any other) installed you can follow these steps to do so:<br />
  ~ [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Download%20and%20Install%20pip%3A&text=Download%20the%20get%2Dpip.py,where%20the%20above%20file%20exists.&text=and%20wait%20through%20the%20installation,now%20installed%20on%20your%20system)

## Installation
1. Download code as .zip and extract it to the file of your choosing

## How to use (main_e.py)
1. In a terminal move to the directory where you have your main.py;
> ```bash
>  > cd C:\user\...
>  ```
3. To start the program, in terminal write:
```bash
python3 main_e.py
```
4. Follow the rules displayed on the window

## How to use (main.py)
1. In a terminal move to the directory where you have your main.py;
> ```bash
>  > cd C:\user\...
>  ```
3. To start the program, in terminal write:
```bash
python main.py -a (EthernetClient name !Optional!) -f (filename !Required!) -t (code type !Required!)
```
or
```bash
python3 main.py -a -f (filename !required!) -t (code type !Required!) -c (t or f)
```

## What to put in arguments
**Argument -f is required and the program will not work if a value is not given for set argument**
```bash
-a [name of your EthernetClient]
```
```bash
-f [name of your file] e.g.: index.html, style.css, test.txt
```
```bash
-t [type of code] html or css 
```
```bash
-c [t or f] enter f if you want your comments to stay and be added to .ino code
```

### TODO
[↳ Add skip/leave comments option for .css

### ISSUES
>[!] No multy line comments <br>
>[!] Comments in .css files <br>

## Showcase HTML -> Arduino
![vmplayer_WdA0iTMASV](https://user-images.githubusercontent.com/89808542/159575130-dbdfdd16-9eaf-4d75-ae20-f4f3dd141278.png)
![vmplayer_TXBauYR6WV](https://user-images.githubusercontent.com/89808542/159575244-c6cfad2c-47cb-4240-9861-749fac7a6f68.png)
![vmplayer_bcyBznAm2t](https://user-images.githubusercontent.com/89808542/159575599-373b821c-e758-447f-9d83-6557ba70cd21.png)

## Showcase CSS -> Arduino
![vmplayer_B96DYcqgUM](https://user-images.githubusercontent.com/89808542/159131133-277631fb-fc41-4965-ae22-664d4a10f055.png)
![vmplayer_ElgqgwZsXA](https://user-images.githubusercontent.com/89808542/159131361-33b92895-c980-42e0-b7a4-c9d32a081d60.png)
![vmplayer_hF90aUJinE](https://user-images.githubusercontent.com/89808542/159131237-c6f712ea-1731-455e-86e7-5dea5e4aa4df.png)
