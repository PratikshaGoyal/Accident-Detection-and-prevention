import requests

def get_contact():
	f = open("vehicle_no", "r")
	v = (f.readline())
	server_ip = "IP of DB server" 
	r = requests.get(f"http://{server_ip}:8000/users/{v}")
	data = r.json()
	enum = str(list(data.values())[0])
	
	print(enum)
	return enum