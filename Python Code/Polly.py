import boto3

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

if __name__ == '__main__':
	play_sound('Me quede sin pila')