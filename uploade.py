#!/usr/bin/python
# pip install boto3
# sudo apt-get install awscli
# aws configure
# Access key ID,Secret access key
# AKIAJ3V3GOC2QCVNBBPQ,OJivGxUbh14OgCHmTYSdREScj/gFQkrh5juk5MvX

import boto3

def uploadeFile(filename):
	# Let's use Amazon S3
	s3 = boto3.resource('s3')

	s3c = boto3.client('s3')
	#s3c.create_bucket(Bucket='hulkbuster-ebooks')
	#filename = 'sample5.mp4'
	bucket_name = 'hackathonwie'

	s3c.upload_file(filename,bucket_name,filename)
	URL = "https://s3.amazonaws.com/hackathonwie/"+filename
	object_acl = s3.ObjectAcl(bucket_name,filename)
	response = object_acl.put(ACL='public-read')
	
	return URL
	#s3.Bucket(bucket_name).download_file(filename,filename)
	# Print out bucket names
	#for bucket in s3.buckets.all():
	#    print(bucket.name)
