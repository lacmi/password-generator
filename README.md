# password-generator
Password generation tool
## features
* Generates a random password composed of lower and upper case letters, numbers and special characters
* The password will be copied in the clipboard
* Options:  
  *`-l` the length of the password, default length is 20  
  *`-a` generates a password with only alphanumeric characters  
  *`-p` prints the password instead of copying it to the clipboard
## installation
Python version: 3  
Works on Windows and Linux  
The `pyperclip` package must be installed: `pip install pyperclip`  
On Linux, `pyperclip` uses the xclip command: `sudo apt-get install xclip`
