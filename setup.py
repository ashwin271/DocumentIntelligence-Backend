import os 
import time 


token = input("Enter the token: ")
model = input("Enter the model: ")
os.system("cls")

content = f'TOKEN = "{token}"\nMODEL = "{model}"'

with open('backend/data_extractor/API_CONFIG.py', 'w') as f:
    f.write(content)
    
print("API config file created successfully")
time.sleep(2)
os.system("cls")

req = input("Do you want to install the dependencies now? (y/n): ")
if req.lower() == "y":
    os.system("pip install -r requirements.txt")
    time.sleep(2)
    print("if you encounter any error, please install the dependencies manually by running 'pip install -r requirements.txt' or by installing the requirements one by one using 'pip install <package_name>'")
    time.sleep(5)
else:
    print("Please install the dependencies by running 'pip install -r requirements.txt' or by installing the requirements one by one using 'pip install <package_name>'")
    time.sleep(2)

print("Make sure you have installed the Tesseract OCR and added it to the PATH variable")
time.sleep(1)
print("You can now run the program by running 'backend.py' inside backend folder")
time.sleep(5)