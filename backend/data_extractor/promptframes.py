correctionPrompt = """
This text snippet was extracted from an important document and may contain OCR errors. 
Correct any spelling mistakes and return only the corrected text.
text snippet: 

"""


dataExtractionFrame="""
Given a factual text document, identify and extract the following information:


Title: title of the document based on the summary
Entities: People, organizations, locations, mentioned in the document.
Events: Actions or occurrences described in the document.
Key Dates: Dates explicitly stated in the document. (dates can be in dd/mm/yy format or can be like two day from the third of march which would mean march 5th)
Significance of Dates: Briefly explain the importance of each extracted date in the context of the document (e.g., the date could mark the start of an event, a deadline, or a historical reference).
Additionally, summarize the document in a concise manner, highlighting the main points.

The input document is provided below: 


"""


formatterPrompt = """From the information about the document provided, format the information and create a json object in the following format: {"title": "Title of the document(understand the summary and make a good title)", "data": [ "important information 1", "important information 2", (value of "data" is a list of important points) ], "dates": [ { "value": "2024-04-03", "description": "...", "shouldTrack": true},  { "value": "2025-10-26", "description": "...", "shouldTrack": false}, (value of "dates" is an array of date objects with value as that date, description - a description about that date and shouldTrack - true if that date needs to be tracked ie if the date is important, false otherwise) ], "summary": "A concise summary of the document" } The response should only contain the json object nothing. Give response in plane text. Information about document :"""