import requests

def location():
	f = open("vehicle_no", "r")
	v = (f.readline())
	Location = []
	server_ip = "IP of DB server" 
	r = requests.get(f"http://{server_ip}:8000/location/{v}")
	data = r.json()
	lat = float(list(data.values())[0])
	lng = float(list(data.values())[1])

	print(lat)
	print(lng)
	Location.append(lat)
	Location.append(lng)
	return Location
