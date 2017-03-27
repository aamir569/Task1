import requests
import csv
base_url = 'https://api.typeform.com/v1/forms?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d'
responseFromServer = requests.get(base_url)
responseInJson = responseFromServer.json()

def ResponseInCSV( formId,outputFileName ):
    base_url = "https://api.typeform.com/v1/form/" + formId + "?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d"
    responseFromServer = requests.get(base_url)
    responseInJson = responseFromServer.json()
    outfile = open("customers.csv", "w")
    writer = csv.writer(outfile,delimiter=';')
    responseNumber = 0;

    # Creates heading of the CSV file
    headings = []
    headings.append("Question")
    for question in responseInJson['responses']:
        responseNumber = responseNumber + 1
        heading = "Response " + str(responseNumber)
        headings.append(heading)
    writer.writerow(headings)


    # Extracts answers from each response
    rows = []
    for question in responseInJson['questions']:
        questionRow = question['question']
        rows.append(questionRow)
        for response in responseInJson['responses']:
            if (response['answers'].get(question['id']) != None):
                row = str(response['answers'].get(question['id'])).replace("\n", "")
            elif (response['answers'].get(question['id']) is None):
                row = "NaN"
            rows.append(row)
        print(rows)
        writer.writerow(rows)
        del rows[:]
    outfile.close()
    return

# gets response with all form ids and extract data into CSV file
for response in responseInJson:
    formId = response['id']
    outputFileName = "customers.csv"
    # Gets response with CSV for each Form
    ResponseInCSV(formId,outputFileName)

