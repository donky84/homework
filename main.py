import web
import json

urls = (
    '/(.*)', 'find_diagnoses'
)

app = web.application(urls, globals())

class find_diagnoses:
    
    def __init__(self):
        self.diagnoses = []
        # Load diagnoses from file
        with open('short-diagnoses.txt') as object_file:
            for line in object_file:
                self.diagnoses.append(line[:-1])

    def GET(self, word):
        matches = []
        # find matching strings comparing user input and diagnoses array
        for d in self.diagnoses:
            if word in d:
                matches.append(d)
        web.header('Content-Type', 'application/json')
        return json.dumps(matches)
        

if __name__ == "__main__":
    print "starting..."
    f = find_diagnoses()
    app.run()

