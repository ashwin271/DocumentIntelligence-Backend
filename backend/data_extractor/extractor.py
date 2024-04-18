import google.generativeai as genai
from .promptframes import * 
from .API_CONFIG import *

# setting up the API key
GOOGLE_API_KEY = TOKEN
genai.configure(api_key=GOOGLE_API_KEY)

# initializing model
model = genai.GenerativeModel(MODEL)


# passes prompt to the model and returns the response
def prompt(frame, data):
    combinedPrompt = frame + data
    return model.generate_content(combinedPrompt).text

# corrects spellings and errors occured during the OCR process
def spellcorrect(data):
    spellcorrected=prompt(correctionPrompt,data)
    return spellcorrected

#extracts the required data from the document
def extract(data, file_name=""):
    extframe = dataExtractionFrame.replace("<f_name>",file_name)
    extracted=prompt(extframe,data)
    return extracted

#formats the extracted data
def format(data):
    formattedResponse = prompt(formatterPrompt,data)
    return formattedResponse


# print(type(formattedResponse))

# data = json.loads(formattedResponse)

# print(data)



