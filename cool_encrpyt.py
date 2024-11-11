#!/usr/bin/env python3
from colorama import Fore,init,Back,Style
from beepy import beep
from cryptography.fernet import Fernet
import os
import time


#------------------------------------------------------------------------------------------------------
init(autoreset=True)
figlet='''
      ____            _ _____                             _
     / ___|___   ___ | | ____|_ __   ___ _ __ _   _ _ __ | |_
    | |   / _ \ / _ \| |  _| | '_ \ / __| '__| | | | '_ \| __|
    | |__| (_) | (_) | | |___| | | | (__| |  | |_| | |_) | |_
     \____\___/ \___/|_|_____|_| |_|\___|_|   \__, | .__/ \__|
                                              |___/|_|
               Instant Encrypt or Decrypt  
---------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------
def Art():
    os.system("clear")
    print(figlet)
#----------------------------------------------------------------------------------------------------------
def inpcheck():
    Art()
    print(Fore.BLUE+Back.WHITE+"Please enter the full path of your file ")
    absolute_path=os.path.split(input('[path#>>]'))
    if not absolute_path[0] =="":
      try:
       os.chdir(absolute_path[0])
      except:
          pass
    if  not os.path.exists(absolute_path[1]): 
        print(Fore.RED+Style.BRIGHT+"Please enter correct path")
        beep(sound=5)
        inpcheck()
    else:
        print(Fore.WHITE+"This is  the file you selected"+ Style.BRIGHT + " " + absolute_path[1])
        time.sleep(2)
    return absolute_path[1]  

#----------------------------------------------------------------------------------------------------------
def options():
    Art()
    print("""            Select any option you like
           [1]Instant Encrypt with Random key (Recommended)
           [2]Instant Decrypt with lastly  used key 
           [3]Encrypt it with a  key
           [4]Decrypt it with a key


            """)
    c1=input("[Enter Your Choice No#>>")
    if c1 == "":
     print("Choice cannot be empty")
     beep(5)
     options()
    if c1=="exit":
      print("So you want to exit")
      time.sleep(0.25)
      print(Fore.Blue+Back.WHITE+"Thanks for using CoolEncrypt")
      exit()

    if c1=="1" or c1=="first" or c1=="Instant Encrypt with Random key":
        print("So You Have Choosen Instant Encrypt With Random Key Option")
        Art()
        return "1"
    elif c1=="2"or c1=="second" or c1=="Instant Decrypt with lastly used key":
        print("So you have Choosen Instant Decrypt with last key")
        Art()
        return"2"
    elif c1=="3" or c1=="third" or c1=="Encrypt it with a  key":
        print("So you have Choosen Instant Encrypt it with a key")
        Art()
        return"3"
    elif c1=="4" or c1=="fourth" or c1=="Decrypt it with a key":
      print("So you have choosen Instant Decrypt with a key ")
      Art()
      return"4"
    else:
        print("Some internal occoured error")
        exit()

#-----------------------------------------------------------------------------------------------------------
class Engima:
    def __init__(self,file_name):
     self.file_name=file_name
     self.file_read=open(self.file_name,"rb")
   
    def InstantEncrypt(self):
        self.last_key=open(".lastkey.key","wb+")
        self.key=Fernet.generate_key()
        encoder=Fernet(self.key)
        newdata=encoder.encrypt(self.file_read.read())
        with open(self.file_name,"wb") as file:
         file.write(newdata)
         file.close()
         print("File encrypted successfully .This is the key to decrypt it\n\n",self.key.decode())
         self.last_key.write(self.key)
         self.last_key.close()


    def InstantDecrypt(self):
        self.last_key=open(".lastkey.key","rb+")
        last_key=self.last_key.read()
        decoder=Fernet(last_key)
        newdata=decoder.decrypt(self.file_read.read())
        with open(self.file_name,"wb") as file:
            file.write(newdata)
            file.close()
            print(Fore.RED+"File has been decrypted successfully".center(80))
    
    def Encrypt(self):
       print("Please enter a key to do encryption")
       c2=input("[#>>]")
       if c2=="":
           print("Key Cannot Be Empty")
           Encrypt()
       given_key=c2.encode()
       encoder=Fernet(given_key)
       newdata=encoder.encrypt(self.file_read.read())
       with open(self.file_name,"wb") as file:
           file.write(newdata)
           print("Encrypt succesfully with the given key")

    def Decrypt(self):
        print("Please enter a key to decrypt it ")
        c3=input("[#>>]")
        if c3=="":
          Decrypt()
        given_key=c3.encode()
        decoder=Fernet(given_key)
        newdata=decoder.decrypt(self.file_read.read())
        with open(self.file_name,"wb") as file:
            file.write(newdata)
        print("Decrypt successfull")


#----------------------------------------------------------------------------------------------------------


if __name__=="__main__":
    Art()
    input(Fore.RED+"Enter Any Key To Continue".center(80))
    choosed_options=options()
    valdiated_path=inpcheck()
    start=Engima(valdiated_path)
    if choosed_options=="1":
        start.InstantEncrypt()
    elif choosed_options=="2":
        start.InstantDecrypt()
    elif choosed_options=="3":
        start.Encrypt()
    elif choosed_options=="4":
        start.Decrypt()
    print(Fore.YELLOW+Style.BRIGHT+"Hope you got everyting you were looking".center(82))

