import datetime
import openai
import whisper
import os

directory = 'Videos'

model = whisper.load_model('base.en')
option = whisper.DecodingOptions(language='en', fp16=False)

for filename in os.scandir(directory):
    if filename.is_file():
        print("FILENAME IS:", filename.path)
        save_target = (filename.path[:-3] + 'vtt')
        print("SAVE TARGET IS:", save_target)
        result = model.transcribe(filename.path)

        with open(save_target, 'w') as file:
            file.write('WEBVTT' + '\n')
            file.write('\n')
            for indx, segment in enumerate(result['segments']):
                file.write(str(indx + 1) + '\n')
                start = (str(datetime.timedelta(seconds=segment['start'])))
                end = ('0' + str(datetime.timedelta(seconds=segment['end'])))
                if len(start) < 10:
                    if start[-1] == '.':
                        start = start + '000'
                    else:
                        start = start + '.000'
                if len(end) < 10:
                    if end[-1] == '.':
                        end = end + '000'
                    else:
                        end = end + '.000'
                #file.write('0' + (str(datetime.timedelta(seconds=segment['start']))[:11]) + ' --> ' + ('0' + str(datetime.timedelta(seconds=segment['end']))[:11] + '\n'))
                file.write(('0' + start)[:12] + ' --> ' + end[:12] + '\n')
                file.write(segment['text'].strip() + '\n')
                file.write('\n')






