import argparse
import re
import os.path
from gtts import gTTS

parser = argparse.ArgumentParser(description='Truly innovative version control.')
parser.add_argument('file', type=str, help='source code file')
parser.add_argument('-v', dest='version', default='1.0', help='version of source code (default: 1.0)')
args = parser.parse_args()

vers_re = re.compile('^\\d+\\.\\d+$')
output_name = f'{args.file} - {args.version}.mp3'

if not vers_re.match(args.version):
    print('error: version should be "^\\d+\\.\\d+$"')
    exit()
if not os.path.exists(args.file):
    print('error: such no file')
    exit()
if os.path.exists(args.file):
    print('error: already commit this version')
    exit()

with open(args.file, 'r') as file:
    data = file.read()
    tts = gTTS(data)
    tts.save(output_name)
    print(f'Successfully commited to {output_name}')
