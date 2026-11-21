import os

def find_files_in_folder():
	folder_list= input("Please enter the folder names with space in between---").split()
	for folders in folder_list:
		try:
			files_list = os.listdir(folders)
		except FileNotFoundError:
			print("Please provide a valid folder name to continue --- ", folders)
			input("Press Enter to Continue--- ")
			continue
		for files in files_list:
			print(files)
		input("Press Enter to Continue--- ")


find_files_in_folder()
