import datetime
import openai
import whisper

model = whisper.load_model('base.en')
option = whisper.DecodingOptions(language='en', fp16=False)
result = model.transcribe('Done/DC-U02-2.1.3a Simon V02.mp4')

print("result is:", result['segments'])

save_target = 'Done/DC-U02-2.1.3a Simon V02.vtt'

with open(save_target, 'w') as file:
    #file.write('WEBVTT' + '\n')
    for indx, segment in enumerate(result['segments']):
        #file.write(str(indx + 1) + '\n')
        start = (str(datetime.timedelta(seconds=segment['start'])))

        if len(start) < 10:
            if start[-1] == '.':
                start = start + '000'
            else:
                start = start + '.000'
        #end = ('0' + str(datetime.timedelta(seconds=segment['end'])))
        #file.write('0' + (str(datetime.timedelta(seconds=segment['start']))[:11]) + ' --> ' + ('0' + str(datetime.timedelta(seconds=segment['end']))[:11] + '\n'))
        if (indx == 0) or (indx % 10 == 0):
            file.write(start[3:7] + '\n')
        file.write(segment['text'].strip())
        file.write('\n')