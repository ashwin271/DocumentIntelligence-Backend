from data_extractor import extractor as ext
from OCR import pre_process as pp, converter as cnv

# Function to extract data from a document
def doc_ext(file_name):
    processedimage=pp.process(file_name)

    docData = cnv.convert(processedimage)

    corrected = ext.spellcorrect(docData)

    info = ext.extract(corrected)

    data = ext.format(info, file_name)

    return data