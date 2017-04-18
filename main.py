import web
import json

urls = (
    '/diagnoses/(.*)', 'Diagnoses'
)

app = web.application(urls, globals())

class Diagnoses:
    
    def __init__(self):
        """
        Load the list of diagnoses from a file on the bootstrap of the app

        """
        self.diagnoses = []
        with open('short-diagnoses.txt') as object_file:
            for line in object_file:
                # The '\n' is removed from the string
                self.diagnoses.append(line[:-1].lower())

    def GET(self, input_diagnosis):
        """
        Find matching between input diagnosis and list of available diagnoses

        @param input_diagnosis:     the diagnosis as a string.
        @returns:                   JSON response, array of possible matches
        
        """
        matched = []
        
        for diagnosis in self.diagnoses:
            if input_diagnosis.lower() in diagnosis:
                matched.append(diagnosis)
        web.header('Content-Type', 'application/json')
        return json.dumps(matched)
        

if __name__ == "__main__":
    print "starting..."
    d = Diagnoses()
    app.run()

