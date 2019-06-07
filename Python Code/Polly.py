import boto3
import playsound
import time

poly = boto3.client(
    'polly',
    region_name='us-east-1',
    aws_access_key_id='AKIA4DLSPRU2WEQGDOOP',
    aws_secret_access_key='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',
    )

def play_sound(text):
	response = poly.synthesize_speech(Text=text,VoiceId='Miguel',OutputFormat='mp3')

	body = response['AudioStream'].read()

	file_name = 'voice.mp3'

	with open(file_name,'wb') as file:
		file.write(body)
		file.close()
	playsound.playsound('voice.mp3', True)
i=0
while(1==1):
	play_sound(str(i))
	i=i+1
	time.sleep(1)

