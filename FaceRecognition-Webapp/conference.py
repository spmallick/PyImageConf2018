import flask
import flask_restful as rest
import werkzeug.routing
import DnnRecognizer
#import DlibRecognizer
import base64

class ConferenceApplication(flask.Flask):
    def __init__(self,name):
        super(ConferenceApplication,self).__init__(name)
        self.recognizer = DnnRecognizer.DnnRecognizer()
        #self.recognizer = DlibRecognizer.DlibRecognizer()

application = ConferenceApplication(__name__)

application.debug = True

class RegexConverter(werkzeug.routing.BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
application.url_map.converters['regex'] = RegexConverter

api = rest.Api(application)

class FilesResource(rest.Resource):
    def get(self,path,extension):
        return flask.send_file("templates/" + path + "." + extension)


class ImageReceiver(rest.Resource):
    def readImage():
        if(flask.request.headers.get('content-type') == 'multipart/form-data'):
            return flask.request.files['file'].read()
        else:
            print(flask.request.headers)

            for key in flask.request.values.keys():
                if(key.startswith('data:')):
                    commaIndex = key.find(',')
                    imageData = key[commaIndex+1:]
                    missingPadding = len(imageData) % 4
                    if missingPadding != 0:
                        imageData += '='* (4 - missingPadding)
                    imageData = imageData.replace(" ","+")
                    return base64.standard_b64decode(imageData)
        return

class EnrollURL(ImageReceiver):
    def post(self):
        name = flask.request.values['name']
        application.recognizer.enroll(ImageReceiver.readImage(), name)
        return {'name':name}
    
class RecognizeURL(ImageReceiver):
    def post(self):
        name = application.recognizer.recognize(ImageReceiver.readImage())
        return {'name':name}


#Static URLs
api.add_resource(FilesResource,"/<regex('[0-9a-zA-Z_./]+'):path>.<regex('xml|html|css|js'):extension>")

#REST Urls
api.add_resource(EnrollURL,"/enroll")
api.add_resource(RecognizeURL,"/recognize")

