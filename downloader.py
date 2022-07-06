import requests
import ffmpeg
import m3u8
import sys
from tqdm import tqdm
from TStoMP4 import ts_to_mp4

#コマンドラインから受け取る場合
#args = sys.argv
#url = args[1]
#raw_cookies = args[2]
#m3u8_path = args[3]
#filename = args[4]

url = "tsファイル配置URL"

raw_cookies = "自分のwebclassのcookie情報"

m3u8_path = "m3u8ファイルパス"

filename = "出力ファイル名"

cookies = {}

raw_cookies = raw_cookies.replace(";",'\n')
raw_cookies = raw_cookies.split()

for i in raw_cookies:
    i = i.replace("=","\n")
    i = i.split()
    cookies[i[0]] = i[1]

playlist = m3u8.load(m3u8_path)
ts_list = []

total = len(playlist.segments)

for index,segment in enumerate(playlist.segments):
    segment = segment.absolute_uri
    file_url = requests.get(url+segment,cookies=cookies).content
    ts_list.append("ts_files/"+segment)

    print(f"[ TS File {segment} downloading ] -> ({index+1} / {total})")
    with open("ts_files/"+segment,"wb") as f:
        f.write(file_url)

print("[ CONVERTING ]")
ts_to_mp4(ts_list,filename)
