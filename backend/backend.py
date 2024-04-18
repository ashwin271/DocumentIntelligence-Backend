from flask import Flask, request, jsonify
import data.filehandle as fh
import ocr_extract as oe

DOC_FOLDER = "./uploaded_documents"
DATA_FILE = './data/data.json'

app = Flask(__name__)

# sample route
@app.route("/")
def home():
    return "home"


# route to upload a document
@app.route("/postfile",methods=['POST'])
def postfile():
    file = request.files['file']
    if file.filename == '': 
        return jsonify({"status": "error", "message": "no file selected"}),400
    elif file.filename in fh.getuploadedfiles("DOC_FOLDER"):
        return jsonify({"status": "error", "message": "file already exists"}),409
    else:
        file.save(f"DOC_FOLDER/{file.filename}")
        return jsonify({"status": "success", "filename": file.filename}), 201


# route to get list of documents
@app.route("/getfiles",methods=['GET'])
def getfiles():
    files = fh.getuploadedfiles("DOC_FOLDER")
    return jsonify(files)


# route to scan a document
@app.route("/scan",methods=['GET'])
def scan():
    file_name = request.args.get('file_name')
    file_list = fh.getlistoffiles(DATA_FILE)
    if file_name in file_list: 
        file_data = fh.readfromfile(file_name,DATA_FILE)
        return jsonify({file_name:file_data})
    elif file_name in fh.getuploadedfiles("DOC_FOLDER"):
        response = oe.doc_ext(file_name)
        fh.writetofile(response,DATA_FILE)
        return response
    else: 
        return jsonify({"status": "error", "message": "file not found"}),404



if __name__ == "__main__":
    app.run(debug=True)