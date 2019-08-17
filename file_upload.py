from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import os

#text = pd.read_csv('only_text.csv')


app = Flask(__name__)
api= Api(app)
UPLOAD_FOLDER = "/home/ayan/Desktop/uploads/"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




class upload(Resource):
	def post(self):
		if request.files:
			f = request.files.get('file')

			filename = f.filename
			f.save(os.path.join(UPLOAD_FOLDER,filename))
			print(os.path.join(UPLOAD_FOLDER,filename))
			df = pd.read_csv(os.path.join(UPLOAD_FOLDER,filename))
			print(len(df))                           
			print(len(df.index))                   
			print(df)      
			total_data = len(df)
			a = df.columns
			
			return {'message': 'sucess', 'status': True,"no_of_record":total_data,"column":list(a)}
		else:
			return {'message': 'please upload file'}


api.add_resource(upload,'/')



if __name__ == "__main__":
	app.run()