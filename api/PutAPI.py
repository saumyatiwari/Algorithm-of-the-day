from flask import Flask, request
import json
app=Flask(__name__) #function name is app  
# use to create the flask app and intilize it
@app.route("/", methods	=['PUT']) #Defining route and calling methods. GET will be in caps intalized as an arrya
# if giving the giving any configuration then function name will proceed with @ else it will use name alone for example we are using @app name to updae the config of @app name  
def helloworld():
	content = request.get_json()
	# name= content["Name"]
	with open('personal.json', 'w') as json_file:
		json.dump(content, json_file)
	return "data saved"

if __name__ == '__main__':
		app.run()
# by default flask uses 5000 port and host as 0.0.0.0

# Run steps
#1. Run with python FirstAPI.py 
#2. Flask will auto. create a server & start the flask app in dev mode
#3. U can call ur API with address http://0.0.0.0:5000/ 
#4. First install the flask by command "pip3 install flask" before running the code