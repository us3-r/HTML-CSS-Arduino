# HTML-CSS-Arduino
This is a simple Python script that converts .html file format to format that can be copied and pasted to .ino files

## Requirements
To run this program you need to have:<br />
~ [Python](https://www.python.org/downloads/)<br />
> If you don't have a package manager such as pip (you should be fine using any other) installed you can follow these steps to do so:<br />
  ~ [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Download%20and%20Install%20pip%3A&text=Download%20the%20get%2Dpip.py,where%20the%20above%20file%20exists.&text=and%20wait%20through%20the%20installation,now%20installed%20on%20your%20system)

## Installation
1. Download code as .zip and extract it to the file of your choosing

## How to use
1. In a terminal move to the directory where you have your main.py;
> ```bash
>  > cd C:\user\...
>  ```
3. To start the program, in terminal write:
```bash
python main.py -c (EthernetClient name !Optional!) -f (filename !Required!) -t (code type !Required!)
```
or
```bash
python3 main.py -c -f (filename !required!) -t (code type !Required!)
```

## What to put in arguments
**Argument -f is required and the program will not work if a value is not given for set argument**
```bash
-c [name of your EthernetClient]
```
```bash
-f [name of your file] e.g.: index.html, style.css, test.txt
```
```bash
-t [type of code] html or css 
```

### TODO
[↳ More advanced html reformating

### ISSUES
>[!] Does not work with .css files [fixed]

## Showcase HTML -> Arduino
![vmplayer_eLvtDNrquT](https://user-images.githubusercontent.com/89808542/159131089-903e9090-2ec0-480e-aa6a-41755497d48c.png)
![vmplayer_tip14HEUZl](https://user-images.githubusercontent.com/89808542/159131103-4d0fc206-0338-455d-a4f1-52e30e1052a2.png)
![vmplayer_J8zvijt2kS](https://user-images.githubusercontent.com/89808542/159131107-a5a7e5ed-3639-4399-b3b2-ff8c084bf04a.png)

## Showcase CSS -> Arduino
![vmplayer_B96DYcqgUM](https://user-images.githubusercontent.com/89808542/159131133-277631fb-fc41-4965-ae22-664d4a10f055.png)
![vmplayer_lWybsMfl1Z](https://user-images.githubusercontent.com/89808542/159131135-c34b4cb6-6982-4777-a364-2f6591e86440.png)
![vmplayer_hF90aUJinE](https://user-images.githubusercontent.com/89808542/159131237-c6f712ea-1731-455e-86e7-5dea5e4aa4df.png)
