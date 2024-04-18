import json
import os


# Function to create data.json file
def createfile(file_path="data.json"):
    file = open(file_path, "w+")
    file.write("{}")
    file.close()


# Function to write data to a file
def writetofile(data, file_path="data.json"):
    json_data = json.loads(data)
    
    try:
        file = open(file_path, "r+")
    except FileNotFoundError:
        createfile(file_path)
        file = open(file_path, "r+")

    filedata=json.load(file)
    filedata.update(json_data)

    file.seek(0)
    json.dump(filedata, file)

    file.close()

    return 1

# Function to read data from a file
def readfromfile(file_name, file_path="data.json"):
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        return 0

    filedata = json.load(file)
    file.close()
    try: 
        return filedata[file_name]
    except KeyError:
        return 0


# Function to get uploaded files (files from uploaded_documents folder)
def getuploadedfiles(folder_path):
    files = os.listdir(folder_path)
    files.remove(".gitignore")
    return files


# Function to get list of files in data.json (files which are already scanned)
def getlistoffiles(file_path="data.json"):
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        return 0

    filedata = json.load(file)
    file.close()
    return list(filedata.keys())

# Function to delete a file
def deletefile(file_name, file_path="data.json"):
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        return 0

    filedata = json.load(file)
    file.close()

    try:
        del filedata[file_name]
    except KeyError:
        return "File not found"

    file = open(file_path, "w")
    json.dump(filedata, file)
    file.close()
    return 1


