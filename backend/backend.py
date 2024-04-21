from flask import Flask, request, jsonify
import data.filehandle as fh
import ocr_extract as oe
from flask_cors import CORS

DOC_FOLDER = "./uploaded_documents"
DATA_FILE = './data/data.json'

app = Flask(__name__)
CORS(app)

# sample route
@app.route("/")
def home():
    return jsonify({"status": "success", "message": "API is working"}), 200


# Get methods

# route to get list of documents
@app.route("/getfiles",methods=['GET'])
def getfiles():
    files = fh.getuploadedfiles(DOC_FOLDER)
    return jsonify(files)


# route to get list of scanned documents
@app.route("/getscannedfiles",methods=['GET'])
def getscannedfiles():
    files = fh.getlistoffiles(DATA_FILE)
    return jsonify(files)


# route to scan a document
@app.route("/scan",methods=['GET'])
def scan():
    file_name = request.args.get('file_name')
    file_list = fh.getlistoffiles(DATA_FILE)
    if file_name in file_list: 
        file_data = fh.readfromfile(file_name,DATA_FILE)
        return jsonify({file_name:file_data})
    elif file_name in fh.getuploadedfiles(DOC_FOLDER):
        response = oe.doc_ext(file_name)
        fh.writetofile(response,DATA_FILE)
        return response
    else: 
        return jsonify({"status": "error", "message": "file not found"}),404



# Post methods

# route to upload a document
@app.route("/postfile",methods=['POST'])
def postfile():
    file = request.files['file']
    if file.filename == '': 
        return jsonify({"status": "error", "message": "no file selected"}),400
    elif file.filename in fh.getuploadedfiles(DOC_FOLDER):
        return jsonify({"status": "error", "message": "file name already exists"}),409
    else:
        file.save(DOC_FOLDER+'/'+file.filename)
        return jsonify({"status": "success", "filename": file.filename}), 201



# Put methods

# route to update/rescan extracted data of a document
@app.route("/rescandata",methods=['PUT'])
def rescandata():
    file_name = request.args.get('file_name')
    file_list = fh.getlistoffiles(DATA_FILE)
    if file_name in file_list: 
        response = oe.doc_ext(file_name)
        fh.writetofile(response,DATA_FILE)
        return response
    else:
        return jsonify({"status": "error", "message": "file not found"}),404



# Delete methods

# route to delete a document
@app.route("/deletefile",methods=['DELETE'])
def deletefile():
    file_name = request.args.get('file_name')
    if fh.deletefile(file_name,DOC_FOLDER) == 1:
        return jsonify({"status": "success", "message": "file deleted"}), 200
    else:
        return jsonify({"status": "error", "message": "file not found"}),404
    

# route to delete extracted data of a document
@app.route("/deletefiledata",methods=['DELETE'])
def deletedata():
    file_name = request.args.get('file_name')
    if fh.deletefiledata(file_name,DATA_FILE) == 1:
        return jsonify({"status": "success", "message": "data deleted"}), 200
    else:
        return jsonify({"status": "error", "message": "data not found"}),404


# route to delete file and extracted data of a document
@app.route("/deletefileanddata",methods=['DELETE'])
def deletefileanddata():
    file_name = request.args.get('file_name')
    status = fh.deletefileanddata(file_name,DOC_FOLDER,DATA_FILE)
    if status == 1:
        return jsonify({"status": "success", "message": "file and data deleted"}), 200
    elif status == -1:
        return jsonify({"status": "error", "message": "file not found   "}),404
    else: 
        return jsonify({"status": "partial_success", "message": "file deleted but data not found"}), 206



if __name__ == "__main__":
    app.run(debug=True)