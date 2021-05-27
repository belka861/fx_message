import requests,json,random
url = 'https://raw.githubusercontent.com/belka861/fx_message/main/z.txt'
r = requests.get(url, allow_redirects=True)
open('z.txt', 'wb').write(r.content)

with open('z.txt', 'r', encoding='utf-8', errors='ignore') as file:
	z = file.read().replace('\n', '')
#print(z)
rsize=len(z)
chunk=random.randint(5000,100000)
#print(z[5000:5020])
rstart=random.randint(100,rsize-chunk)
url='https://backend.globalallianceltd.com/api/messages/undefined?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYmFja2VuZC5nbG9iYWxhbGxpYW5jZWx0ZC5jb21cL2FwaVwvYXV0aCIsImlhdCI6MTYyMjEzNTU4MywiZXhwIjoxNjIyMjIxOTgzLCJuYmYiOjE2MjIxMzU1ODMsImp0aSI6IkJKMjJzSFZTVzV5U1VJRlAiLCJzdWIiOjMyNTc3NiwicHJ2IjoiZTcyYTY3MDZjNTY1MDU1ZDg0MTMzYTE4OGI0MDE4MjU4MmRhMDJjNyJ9.kjxSwFUZj1UDir8MmMvcg1mAV64NDjDFrk8Jt0CypYA'
headers = {"Content-Type": "application/json"}

while True:
	chunk=random.randint(5000,100000)
	rstart=random.randint(100,rsize-chunk)

	data={"message":z[rstart:rstart+chunk]}
	response = requests.put(url, data=json.dumps(data), headers=headers)
	res = response.json()
	print(res)
