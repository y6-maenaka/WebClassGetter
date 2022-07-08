import requests
import ffmpeg
import m3u8
import sys
from tqdm import tqdm
from TStoMP4 import ts_to_mp4

#コマンドラインから受け取る
args = sys.argv
url = args[2]
filename = args[1]

cookies = {"WCAC":"Authenticated"}

parse_url = url.split("/")
parse_url = parse_url[0:len(parse_url)-1]

m3u8_path = 'm3u8.m3u8'

#m3u8ファイルのダウンロード
m3u8Data = requests.get(url,cookies=cookies).content
with open(m3u8_path ,mode='wb') as f: # wb でバイト型を書き込める
      f.write(m3u8Data)

#TSファイルの保管URL
source_path = "/".join(parse_url) + "/"

playlist = m3u8.load(m3u8_path)
ts_list = []

total = len(playlist.segments)

#TSファイルのダウンロード
for index,segment in enumerate(playlist.segments):
    segment = segment.absolute_uri
    file_url = requests.get(source_path+segment,cookies=cookies).content
    ts_list.append("download_ts_files/"+segment)

    print(f"[ TS File {segment} downloading ] -> ({index+1} / {total})")
    with open("download_ts_files/"+segment,"wb") as f:
        f.write(file_url)

print("[ CONVERTING ]")
ts_to_mp4(ts_list,filename)
print(f"=====SUCCESS DOWNLOAD [{filename}.mp4]=====")
