import boto3
import playsound
import time

poly = boto3.client(
    'polly',
    region_name='us-east-1',
    aws_access_key_id='AKIA4DLSPRU2WEQGDOOP',
    aws_secret_access_key='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',
    )


	

i=0

while(1==1):
	response = poly.synthesize_speech(Text=str(i),VoiceId='Miguel',OutputFormat='mp3')

	body = response['AudioStream'].read()

	file_name = 'C:\\Users\\braya\\Documents\\GitHub\\Sign-Lenguage-to-speech-Glove\\Python Code\\voice.mp3'

	file = open(file_name,'wb')
	file.write(body)
		#file.close()
	playsound.playsound(file_name, True)
	i=i+1
	time.sleep(1)

