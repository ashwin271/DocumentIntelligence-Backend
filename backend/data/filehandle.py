import json
import os


# Function to create data.json file
def createfile(file_path="data.json"):
    file = open(file_path, "w+")
    file.write("{}")
    file.close()
    # this function needs to be improved such that it can also add content to the file from params


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
        createfile(file_path)
        return "Data not found"

    filedata = json.load(file)
    file.close()
    try: 
        return filedata[file_name]
    except KeyError:
        return "Data not found"


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
        createfile(file_path)
        return []

    filedata = json.load(file)
    file.close()
    return list(filedata.keys())


# Function to delete extracted data of a file
def deletefiledata(file_name, file_path="data.json"):
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        createfile(file_path)
        return 0

    filedata = json.load(file)
    file.close()

    try:
        del filedata[file_name]
    except KeyError:
        return 0

    file = open(file_path, "w")
    json.dump(filedata, file)
    file.close()
    return 1


# Function to delete a file from uploaded_documents folder
def deletefile(file_name, folder_path="./uploaded_documents"):
    try:
        os.remove(f"{folder_path}/{file_name}")
    except FileNotFoundError:
        return 0
    return 1


