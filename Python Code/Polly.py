import boto3

poly = boto3.client(
    'polly',
    region_name='us-east-1',
    aws_access_key_id='ASIAQ45KW5BRMPEIT7EE',
    aws_secret_access_key='w722gsCz2KUQbjDjG7E2UFzPgxwObUcE1eyvx3Te',
    aws_session_token='FQoGZXIvYXdzEHIaDHpfUFQ7KE6KmQAIOCKJA2DeGEPCsDdNz5xBomjOg6nbJFyictq/eUK4LbMhRNny9nXnPE6WRDYO1SlNeVEh2eGv1QeFJeFVUrSV8cdhgUuOTi8ellClw50oqNvuqC/v8S7/cFHk1rno10p0IG5t+aPMsDLxmwyK7yHRynlVh/kzR+2Pvo0Nxg8fBc+qwn6NjVGQI8/SfJSt6BNvAlMqw6UzVIJkOK2k9h7v4+1g/0G4AjoBdq5G3qCCVlKhtG0YVCzKcWl/riLVO9H1mlaUvHHsG6b3w9ONK7JDLMS1G2MZHrjslGodXYEB5zAP9Z9KlRVObTy8BVPUOmIX/4fUI/LnQGYN58dBFsyoBuIIjP5fwx4vOjcSkEz80c1EBP335YKJg+6OGs+8vX4hAJRVS+upWH4xyLyglLRWwnSS+Tekj1Am8keOqMSgar+kxD2LRF7V+EWO0QsM3PKiUyTfifd1VgvaGeEVaJ4Uw5UV+UFwFCDXm089XOZ1XlrURPYwQpg9nNhZusd9FfZQ68MOz5r7lfpKzD3vWyjXlN/lBQ=='
)

def play_sound(text):
	response = poly.synthesize_speech(Text=text,VoiceId='Miguel',OutputFormat='mp3')

	body = response['AudioStream'].read()

	file_name = 'voice.mp3'

	with open(file_name,'wb') as file:
		file.write(body)
		file.close()

if __name__ == '__main__':
	play_sound('Me la pelas, con canela')