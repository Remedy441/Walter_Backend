from flask import Flask, render_template, request
from werkzeug import secure_filename
import awsUploader as uploader
import videoRecommender as recommender
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/upload',methods = ['GET'])
def upload():
	return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
   		#print request.__dict__
		f = request.files['file']
		f.save(secure_filename(f.filename))
		#script
		pdf = uploader.uploadeFile(f.filename)
		print f.filename
		os.system('python pdf_to_video.py '+f.filename)
		video_file = f.filename.split('.')[0] + '.mp4'
		video = uploader.uploadeFile(video_file)
		#ret = {'pdf':pdf,'video':video}
		recommeneded = recommender.recommend()
		return pdf+' '+video+' '+recommeneded
		#return  uploade.uploadeFile(f.filename)
if __name__ == '__main__':
   app.run(threaded=True,debug=True,port = 5000,host='0.0.0.0')
