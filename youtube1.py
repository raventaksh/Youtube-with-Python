import youtube_dl as d
import sys
lis=[]
x = {'no_warnings':True,'listformats':True , 'quiet': True}
def check(URL):
	lis.append(URL)
	s = d.YoutubeDL(x)	
	vid_info = s.extract_info(lis[0], download = False)	

	file = open('ret.txt','r')
	main_str = file.read()
	file.close()
	type_code = []
	type = []
	extension = []
	for text in  main_str.split(']'):
		mid_text = text.split(',')
		if (mid_text[0]=='[u\'22\''):
			type_code.append(mid_text[0].split('\'')[1])
			type.append("720p")
			extension.append(mid_text[1].split('\'')[1])
		if (mid_text[0]=='[u\'83\''):
			type_code.append(mid_text[0].split('\'')[1])
			type.append("480p")
			extension.append(mid_text[1].split('\'')[1])
		if (mid_text[0]=='[u\'18\''):
			type_code.append(mid_text[0].split('\'')[1])
			type.append("360p")
			extension.append(mid_text[1].split('\'')[1])
		if (mid_text[0]=='[u\'17\''):
			type_code.append(mid_text[0].split('\'')[1])
			type.append('144p')	
			extension.append(mid_text[1].split('\'')[1])
		if (mid_text[0]=='[u\'171\''):
			type_code.append(mid_text[0].split('\'')[1])
			type.append('audio')
			extension.append(mid_text[1].split('\'')[1])
	for f in range(0 , len(type)):
		print str(int(f)+1) , type[f]
	return type , type_code , extension

def dwd(code,type,extension , q):
	def my_hook(d):
		if d['status'] =='downloading':
			q.put((float(d['downloaded_bytes'])/float(d['total_bytes']))*100)
			print '{:.2f}'.format((float(d['downloaded_bytes'])/float(d['total_bytes']))*100),'\r',
	x1  = {'no_warnings':True , 'quiet':True}
	with d.YoutubeDL(x1) as ydl :
		yy = ydl.extract_info(lis[0] , download = False)

	x1 = {'format':code, 'no_warnings':True ,'outtmpl':yy['title']+'@'+type+"."+extension , 'progress_hooks':[my_hook] , 'quiet' :True}
	with d.YoutubeDL(x1) as down:
		down.download(lis)