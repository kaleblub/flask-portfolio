---
title: PicoCTF – Beginner picoMini 2022
author: Kaleb Humpal
date_created: 2022-1-16
summary: This post is my writeup for the beginner level picoMini CTF for the year of 2022. I will be avoiding disclosure of the flags within, for until the event is over with after Feb 4, 2022.
tags: [picoCTF, cyber security, offensive security, hacking, pentest, penetration testing, pentesting, cracking, event, capture the flag, CTF, python, scripting, scripts, writeup, beginner, beginner level]
---
## Introduction
This is the second capture the flag styled event that I will be participating in. It is called PicoCTF [Beginner picoMini 2022](https://play.picoctf.org/events/69), started on January 10, 2022; and ending on February 4, 2022. I am substituting each flag with `picoCTF{FLAG_HIDDEN_BY_KALEB}` so that I am not disclosing the flags before the event is over. I hope everything makes sense, and that you can possibly learn something from me.

---
## runme.py
##### 5 Points
###### AUTHOR: SUJEET KUMAR
##### Description
Run the `runme.py` script to get the flag. Download the script with your browser or with `wget` in the webshell.
[Download runme.py Python script](https://artifacts.picoctf.net/c/92/runme.py)
##### Write up
To get started on the first challenge, we should download the script, you can do that through the command line simply with:
```console
$ wget https://artifacts.picoctf.net/c/92/runme.py
--2022-01-11 10:27:22--  https://artifacts.picoctf.net/c/92/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 52.85.3.2, 52.85.3.86, 52.85.3.85, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|52.85.3.2|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: ‘runme.py’

runme.py                  100%[=====================================>]     270  --.-KB/s    in 0s      

2022-01-11 10:27:23 (11,3 MB/s) - ‘runme.py’ saved [270/270]
```
All right, we got that python script, let's first `cat` it to see what will happen if we run it:
```console
$ cat runme.py
#!/usr/bin/python3
################################################################################
# Python script which just prints the flag
################################################################################

flag ='picoCTF{FLAG_HIDDEN_BY_KALEB}'
print(flag)
```
##### Flag
There's the flag, it is `picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## ncme
##### 10 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Connect to a remote computer using nc and get the flag.
`$ nc saturn.picoctf.net 57688`
##### Write up
##### Flag
After we run the given command, we can see the flag as `picoCTF{FLAG_HIDDEN_BY_KALEB}`.

---
## convertme.py
##### 15 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Run the Python script and convert the given number from decimal to binary to get the flag.
[Download Python script](https://artifacts.picoctf.net/c/36/convertme.py)
##### Write up
Let's download the Python script the same way that we did in the first challenge(`runme.py`):
```console
$ wget https://artifacts.picoctf.net/c/36/convertme.py
--2022-01-11 10:41:21--  https://artifacts.picoctf.net/c/36/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 52.85.3.26, 52.85.3.2, 52.85.3.85, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|52.85.3.26|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1,2K) [application/octet-stream]
Saving to: ‘convertme.py’

convertme.py              100%[=====================================>]   1,16K  --.-KB/s    in 0s      

2022-01-11 10:41:22 (24,3 MB/s) - ‘convertme.py’ saved [1189/1189]
```
Now, let's check what is inside the script again:
```console
$ cat convertme.py 

import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x10) + chr(0x57) + chr(0x0f) + chr(0x5e) + chr(0x51) + chr(0x5c) + chr(0x46) + chr(0x53) + chr(0x13)

num = random.choice(range(10,101))

print('If ' + str(num) + ' is in decimal base, what is it in binary base?')

ans = input('Answer: ')

try:
  ans_num = int(ans, base=2)
  
  if ans_num == num:
    flag = str_xor(flag_enc, 'enkidu')
    print('That is correct! Here\'s your flag: ' + flag)
  else:
    print(str(ans_num) + ' and ' + str(num) + ' are not equal.')
  
except ValueError:
  print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')
```
From here, we can see some complicated stuff going on at the top with a function to perform a XOR operation on a string, followed by the encrypted flag as a bunch of `chr()`s concatenated together.
Then we can see a random number choice between 10 and 100 being assigned to a variable called `num`, then we are told to enter in the binary base value of the `num` number.
Then the script `try`s to see if our answer reversed back into decimal is the same as the random number. If it is, then it will print the flag which is the `flag_enc` variable being run as the argument for the `str_xor` function with the key as `'enkidu'`. All I decided to do, instead of answering the correct binary input, is to comment out(`#`) the `26`th line where it reconverts our given binary input into decimal again and replace it as the following.
```python
try:
  # ans_num = int(ans, base=2)
  ans_num = num
```
So essentially, what happens is the answer we give is rendered useless because we are just assigning the decimal number that is supposed to be checked(`ans_num`) with the original random decimal number that was chosen(`num`), so in the if statement `if ans_num == num:`, they are equal to eachother, so the script outputs the flag as if we gave it the right answer.

##### Flag
The flag that was outputted that was XOR'd with the key 'enkidu' is `picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## Codebook
##### 20 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Run the Python script `code.py` in the same directory as `codebook.txt`.
- [Download code.py](https://artifacts.picoctf.net/c/103/code.py)
- [Download codebook.txt](https://artifacts.picoctf.net/c/103/codebook.txt)
##### Write up
Let's go ahead and `wget` those two files:
```console
$ wget https://artifacts.picoctf.net/c/103/code.py https://artifacts.picoctf.net/c/103/codebook.txt
--2022-01-11 11:10:21--  https://artifacts.picoctf.net/c/103/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 52.85.3.86, 52.85.3.2, 52.85.3.85, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|52.85.3.86|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1,2K) [application/octet-stream]
Saving to: ‘code.py’

code.py                   100%[=====================================>]   1,25K  --.-KB/s    in 0s      

2022-01-11 11:10:22 (28,8 MB/s) - ‘code.py’ saved [1278/1278]

--2022-01-11 11:10:22--  https://artifacts.picoctf.net/c/103/codebook.txt
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: ‘codebook.txt’

codebook.txt              100%[=====================================>]      27  --.-KB/s    in 0s      

2022-01-11 11:10:23 (2,54 MB/s) - ‘codebook.txt’ saved [27/27]

FINISHED --2022-01-11 11:10:23--
Total wall clock time: 1,5s
Downloaded: 2 files, 1,3K in 0s (23,8 MB/s)
```
And as usual, let's take a look at what is inside both files.
(To save space on this write up, we can see that at the end of the file, if the two files are in the same directory, `code.py` will read the `codebook.txt` file and do a calculation to print out the flag.)

##### Flag
So if we run the following, we get the flag:
```console
$ python3 code.py
picoCTF{FLAG_HIDDEN_BY_KALEB}
```

---
## fixme1.py
##### 25 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Fix the syntax error in this Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/38/fixme1.py)
##### Write up
Again, we can `wget` the script with `$ wget https://artifacts.picoctf.net/c/38/fixme1.py`. Then let's take a look inside with `$ cat fixme1.py`:
```python
import random



def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x5e) + chr(0x52) + chr(0x0c) + chr(0x01) + chr(0x42) + chr(0x57) + chr(0x59) + chr(0x0a) + chr(0x14)

  
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)
```
Now if you don't know what to look for, or you don't see it right away, you can simply run `$ python3 fixme1.py` to just run the code to see if it gives us an errer(since we can see it's not doing much other than the `XOR operation` function, so we should be safe)
```console
$ python3 fixme1.py 
  File "fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
    ^
IndentationError: unexpected indent
```
Nice! Python's Interpreter is such a great help with hunting for bugs!

##### Flag
Now we just need to go in and delete the indent before the last `print()`(Also the last line in the script.). Then we simply run the python script again:
```console
$ python3 fixme1.py 
That is correct! Here's your flag: picoCTF{FLAG_HIDDEN_BY_KALEB}
```

---
## fixme2.py
##### 25 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Fix the syntax error in the Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/66/fixme2.py)
##### Write up
Run `wget https://artifacts.picoctf.net/c/66/fixme2.py` to download the script. Then let's see what kind of syntax errors we can maybe find this time. REMEMBER, we can always try to see the hint from the Python Interpreter by running the script to see if any errors come up.
For this one, near the end we have this block of code:
```python
# Check that flag is not empty
if flag = "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```
When we are checking if a variable is equal to something else, we must use the double-equals/`==` to compare, so we can fix that from `if flag = "":` to `if flag == "":`
##### Flag
Then we can run the script to see:
```console
$ python3 fixme2.py 
That is correct! Here's your flag: picoCTF{FLAG_HIDDEN_BY_KALEB}
```

---
## PW Crack 1
##### 25 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/51/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/51/level1.flag.txt.enc) in the same directory too.
##### Write up
Let's go ahead and run `$ wget https://artifacts.picoctf.net/c/51/level1.flag.txt.enc https://artifacts.picoctf.net/c/51/level1.py` to get started. Then we can take a peek inside of the files and see what we need to do.
If we `cat` the contents of the given files, we can see in the Python script, the function at the end of the file, the function that is called on the last line:
```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_1_pw_check()
```
We can see that the entered password is checked with a hardcoded string, `"691d"`
```python
	if user_pw == "691d":
```
So we simply enter that as the password when prompted:
```console
$ python3 level1.py 
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{FLAG_HIDDEN_BY_KALEB}
```
##### Flag
`picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## Glitch Cat
##### 30 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Our flag printing service has started glitching!
`$ nc saturn.picoctf.net 52026`
##### Write up
If we run that command, we get the following:
```console
$ nc saturn.picoctf.net 52026
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x65) + chr(0x63) + chr(0x66) + chr(0x33) + chr(0x38) + chr(0x36) + chr(0x31) + '}'
```
Nice, now they are finally gonna make us have to deal with the `chr()`'s with no loophole. Luckily, we have the `Python Interpreter` we can run that text through. Simply copy and paste that code after running `$ python3` in the terminal, and Python will do all the work.
##### Flag
`picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## PW Crack 2
##### 35 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/17/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level2.flag.txt.enc) in the same directory too.
##### Write up
Let's start with running `$ wget https://artifacts.picoctf.net/c/17/level2.py https://artifacts.picoctf.net/c/17/level2.flag.txt.enc` to download the files. Within the script is the following code:
```python
flag_enc = open('level2.flag.txt.enc', 'rb').read()

def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_2_pw_check()
```
The main line we should look at is that `if` statement, it is checking the `user_pw` against 4 characters. We can copy those characters `chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)` and paste them into the Python interpreter to see what that string is:
```console
$ python3
Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
'4ec9'
```
Okay, so the user password is `'4ec9'`, let's input that into the script:
```console
$ python3 level2.py 
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{FLAG_HIDDEN_BY_KALEB}
```
##### Flag
`picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## HashingJobApp
##### 40 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
If you want to hash with the best, beat this test!
`$ nc saturn.picoctf.net 65352`
##### Write up
If we run the given command, we are prompted with the following string:
```console
$ nc saturn.picoctf.net 65352
Please md5 hash the text between quotes, excluding the quotes: 'Cleopatra'
Answer: 
```
So we just need to quickly hash the string given. We can head here: https://www.md5hashgenerator.com/ for the hashing part, and in our terminal let's run it and hop back and forth:
```console
$ nc saturn.picoctf.net 65352
Please md5 hash the text between quotes, excluding the quotes: 'Hollywood'
Answer: 
1ac441036f927b9815ba1137464ee064
1ac441036f927b9815ba1137464ee064
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'a cheap motel'
Answer: 
d51908671c7603ec46c7379887509894
d51908671c7603ec46c7379887509894
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'cleaning the bathroom'
Answer: 
0c8acab58314dbcf54dbc158470a8047
0c8acab58314dbcf54dbc158470a8047
Correct.
picoCTF{FLAG_HIDDEN_BY_KALEB}
```
##### Flag
`picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## Serpentine
##### 50 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Find the flag in the Python script!
[Download Python script](https://artifacts.picoctf.net/c/95/serpentine.py)
##### Write up
We'll start with downloading the script with `wget https://artifacts.picoctf.net/c/95/serpentine.py`. Inside are a few functions, one in particular is the `print_flag` function:
```python
def print_flag():
  flag = str_xor(flag_enc, 'enkidu')
  print(flag)
```
Near the bottom of the script is the basic menu that will give us the option to print encouragement, print the flag, and quit:
```python
print('Welcome to the serpentine encourager!\n\n')
  
  while True:
    print('a) Print encouragement')
    print('b) Print flag')
    print('c) Quit\n')
    choice = input('What would you like to do? (a/b/c) ')
    
    if choice == 'a':
      print_encouragement()
      
    elif choice == 'b':
      print_flag()
      #print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
      
    elif choice == 'c':
      sys.exit(0)
      
    else:
      print('\nI did not understand "' + choice + '", input only "a", "b" or "c"\n\n')
```
We can see that the option to print the flag won't actually print it. So we need to call the `print_flag` function after we select `'b'`. So we will just make the following addition:
```python
elif choice == 'b':
      print_flag()
      #print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
```
Now when we run the script and select `'b'`, it will actually print the flag for us:
```console
$ python3 serpentine.py 

    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \
                   /   /               \  \
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~

Welcome to the serpentine encourager!


a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b
picoCTF{FLAG_HIDDEN_BY_KALEB}
a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) c
```
##### Flag
There's the flag, `picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## PW Crack 3
##### 75 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/25/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/25/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/25/level3.hash.bin) in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.
##### Write up
Let's run `$ wget https://artifacts.picoctf.net/c/25/level3.py https://artifacts.picoctf.net/c/25/level3.flag.txt.enc https://artifacts.picoctf.net/c/25/level3.hash.bin` to download the files that they give us. Then let's take a look inside of each file. From what I see inside of the python script, I feel like we don't even need to try very hard for this one. They give us 7 passwords at the bottom declared in a variable:
```python
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```
So we can just try each password until we get the correct password:
```console
$ python3 level3.py 
Please enter correct password for flag: d3ab
That password is incorrect
$ python3 level3.py 
Please enter correct password for flag: 8799
That password is incorrect
$ python3 level3.py 
Please enter correct password for flag: 1ea2
Welcome back... your flag, user:
picoCTF{FLAG_HIDDEN_BY_KALEB}
```
Well that was a success, but I want to challenge myself to get it in a different way, automated without my input. I'll just alter the script by moving the possible password list(`pos_pw_list`) above the declaration of the `level_3_pw_check` function, then comment out the `user_pw` input, and then indent all the rest of the code and make that into a for loop going through the `pos_pw_check` list. 
The code should go *`FROM`* this:
```python
def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_3_pw_check()

# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```
*`TO`* this:
```python
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

def level_3_pw_check():
    #user_pw = input("Please enter correct password for flag: ")
    for user_pw in pos_pw_list:
        user_pw_hash = hash_pw(user_pw)
        
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        print("That password is incorrect")

level_3_pw_check()
```
Now when we run the script, we should get the following:
```console
$ python3 level3.py 
That password is incorrect
That password is incorrect
Welcome back... your flag, user:
picoCTF{FLAG_HIDDEN_BY_KALEB}
```
##### Flag
`picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## PW Crack 4
##### 85 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/62/level4.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/62/level4.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/62/level4.hash.bin) in the same directory too.
There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.
##### Write up
Let's download the given files with `$ wget https://artifacts.picoctf.net/c/62/level4.py https://artifacts.picoctf.net/c/62/level4.flag.txt.enc https://artifacts.picoctf.net/c/62/level4.hash.bin`. When you take a look at the Python script, we can see a similar thing happening with this challenge as in `PW Crack 3`. At the end of the script, there is a list being created with 100 possibilities:
```python
# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["6b3e", "989c", "4b17", "d06f", "f495", "6ea1", "44e4", "1d45", "3e1a", "b0b4", "8c65", "3276", "c496", "9d3d", "2476", "6ef4", "6b7f", "c184", "c2a8", "9708", "7bea", "9a2d", "4a22", "93ae", "826b", "9a50", "8b39", "5410", "a86c", "3760", "6426", "ec8e", "c294", "a909", "cbc6", "2e75", "f137", "9cb3", "79e7", "469f", "a9f9", "3e37", "b33e", "3f31", "4b27", "2f06", "cc2f", "d9e4", "2de7", "7328", "b4d4", "8e74", "a677", "b139", "9c74", "8ea4", "36f6", "613b", "7a7a", "5710", "838c", "44d5", "7190", "99d9", "c0a6", "b218", "3223", "477e", "38e5", "19b4", "3267", "2287", "b947", "a8d0", "fd9c", "e99c", "d8b7", "4c82", "b289", "332b", "bba5", "716d", "653e", "eb5d", "ad77", "ad3a", "3922", "7565", "947d", "928c", "2937", "823f", "f362", "79cf", "4582", "c0d0", "ed20", "d89a", "129c", "4e81"]
```
We can't go through each and every possible password manually, that would take too long! Good thing we got our bruteforcing practice in level3. Let's do the same thing, move the list at least above the function call, comment/remove the input for the `user_pw` and create a loop at that point, indenting the rest of the function to be inside the new loop.
So we will go *`FROM`* this:
```python
def level_4_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_4_pw_check()

# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["6b3e", "989c", "4b17", "d06f", "f495", "6ea1", "44e4", ...]
```
And make it look something like this:
```python
pos_pw_list = ["6b3e", "989c", "4b17", "d06f", "f495", "6ea1", "44e4", ...]

def level_4_pw_check():
    #user_pw = input("Please enter correct password for flag: ")
    for user_pw in pos_pw_list:
        user_pw_hash = hash_pw(user_pw)
        
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        print("That password is incorrect")

level_4_pw_check()
```
Then when we run the script, we should see the script bruteforcing with the passwords stored within itself:
```console
$ python3 level4.py
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
Welcome back... your flag, user:
picoCTF{FLAG_HIDDEN_BY_KALEB}
```
##### Flag
`picoCTF{FLAG_HIDDEN_BY_KALEB}`

---
## PW Crack 5
##### 100 Points
###### AUTHOR: LT 'SYREAL' JONES
##### Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/83/level5.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/83/level5.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/83/level5.hash.bin) in the same directory too.
Here's a [dictionary](https://artifacts.picoctf.net/c/83/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.
##### Write up
We can download the given files with the following command: `$ wget https://artifacts.picoctf.net/c/83/level5.py https://artifacts.picoctf.net/c/83/level5.flag.txt.enc https://artifacts.picoctf.net/c/83/level5.hash.bin https://artifacts.picoctf.net/c/83/dictionary.txt`. This challenge will pretty obviously be a dictionary based bruteforce attack. I'll show some simple list comprehension in Python so that we can create a list variable in the script to use the given dictionary file in the script. </br>
First, let's get access to the dictionary file and read it:
```python
with open('dictionary.txt', 'r') as dictionary_file:
	print(dictionary_file.readlines())
```
These two lines of code will open the `dictionary.txt` file in `read` mode, and give it the name `dictionary_file` in the script, then on line 2, the `.readlines()` reads all the lines from a file, and we have that in a `print()` statement which will give us all of the lines in the file. With that knowledge, we will just insert this where we had been adding our code in the last levels, but then the `for loop` will be inside of the code above. The code should end up looking like this:
```python
def level_5_pw_check():
    #user_pw = input("Please enter correct password for flag: ")
    with open('dictionary.txt', 'r') as dictionary:
        passwords = [pw.strip() for pw in dictionary.readlines()]
        for user_pw in passwords:
            user_pw_hash = hash_pw(user_pw)
            
            if( user_pw_hash == correct_pw_hash ):
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), user_pw)
                print(decryption)
                return
            print("That password is incorrect")

level_5_pw_check()
``` 
The function will now open the file, read the lines into a list and clean them incase any whitespace is in one of the strings, then use that list and loop through it trying each password that was found in the file.
##### Flag
After the script tries quite a few, it finally finds the correct one and gives us the flag, `picoCTF{FLAG_HIDDEN_BY_KALEB}`.

---
## Conclusion
I got some good basic practice with this event. It makes me happy that these were easy to me at this point. [Pico](https://picoctf.org/) did a great job with this event in the step by step increase in difficulty of each challenge. 