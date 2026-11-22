import requests
#In this small python-github integration project , we are demonstrating github repo pull request by python and then processing it into dictionary to get wanted information .

github_pull_list = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls").json()


element_no = int(input ("Please enter the directory number on which you want to request information - "))

operations = github_pull_list[element_no]

print(operations.keys())

request_key = input ("Please enter the request key from above to get the information")


if request_key == "user":
	print ("You've selected the user as keyname. ")
	print (operations["user"].keys())
	keyname = input ("please enter the operation you want to continue" )
	if keyname:
		if keyname in operations["user"]:
			print (operations["user"][keyname])
		else: print ("Invalid User Key... ")
	else: print (operations["user"])
else:
	if request_key in operations:
		print (operations[request_key])
	else: print ("Invalid Request Key Name...")
