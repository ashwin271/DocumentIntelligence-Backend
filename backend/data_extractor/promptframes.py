correctionPrompt = """
This text snippet was extracted from an important document and may contain OCR errors. 
Correct any spelling mistakes and return only the corrected text.
text snippet: 

"""


dataExtractionFrame="""
Given a factual text document, identify and extract the following information:

File Name: "<f_name>"
Title: title of the document based on the summary
Entities: People, organizations, locations, mentioned in the document.
Events: Actions or occurrences described in the document.
Key Dates: Dates explicitly stated in the document. (dates can be in dd/mm/yy format or can be like two day from the third of march which would mean march 5th)
Significance of Dates: Briefly explain the importance of each extracted date in the context of the document (e.g., the date could mark the start of an event, a deadline, or a historical reference).
Additionally, summarize the document in a concise manner, highlighting the main points.

The input document is provided below: 


"""


formatterPrompt = """
from the information about the document provided, format the information and create a json object in the following format:
{
	"file_name": { 
		"title": "Title of the document", //understand the summary and make a good title
		"data": [
			"important information 1", 
			"important information 2", 
			// ... Add more data entries 
		], 
		"dates": [ 
			{ "value": "2024-04-03", "description": "...", "shouldTrack": true},  
	        // shouldTrack is true if the date is like a deadline or a significant event or a future event that will occur that the user needs to be alerted when the time comes
	        // shouldTrack is false if the date is not of the above category
			{ "value": "2025-10-26", "description": "...", "shouldTrack": false}, 
			// ... Add more date entries 
		],
		"summary": "A concise summary of the document"
	}
}

the information about the document will be provided below provide the response in the above given format
and the response should only contain the json object nothing else give response in plane text 
do not use any markdown formatting

information about document :

"""
