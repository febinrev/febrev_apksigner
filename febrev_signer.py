import os
print(""" 
 _____ _____ ____  ____  _______     __      _                       
|  ___| ____| __ )|  _ \| ____\ \   / /  ___(_) __ _ _ __   ___ _ __ 
| |_  |  _| |  _ \| |_) |  _|  \ \ / /  / __| |/ _` | '_ \ / _ \ '__|
|  _| | |___| |_) |  _ <| |___  \ V /   \__ \ | (_| | | | |  __/ |   
|_|   |_____|____/|_| \_\_____|  \_/    |___/_|\__, |_| |_|\___|_|   
                                               |___/                 
                              FOR ANDROID METASPLOIT PAYLOADS
                                                 ---->coded by febin rev
 """)
def signer():
    a=input("have you installed apksigner?[Y/n] :")
    if a =="y" or a=="Y":
         print("HERE WE GO......!")
         app_path=input("enter the path of your app (eg: /root/Desktop/app.apk): ")
         if os.path.isfile(app_path):
             os.system("apksigner sign -key febrev.pk8 -cert febrev.x509.pem "+app_path)
             print("signed successfully........!!")
         else:
             print("ERROR : PATH/FILE NOT FOUND BY FEBREV signer!!!")
             print("please input a valid path/file...")
             
    elif a =="n" or a=="N":
           app_path=input("enter the path of your app: ")
           os.system("chmod +x apksigner && ./apksigner sign -key febrev.pk8 -cert febrev.x509.pem "+app_path)
           print("###########################################")
           print("signed successfully..............!!")
    else:
         print("please provide valid input.....")

if __name__=="__main__":
  try:
   signer()
  except KeyboardInterrupt:
   print("  User Interrupt Exit.........")
