pessoas = {"id": 1,"nome":"pedro"}

for key, value in pessoas.items():
	
	if key == "id":
		continue
	print(f"key: {key} => value: {value}")