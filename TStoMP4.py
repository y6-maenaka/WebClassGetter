import ffmpeg

def ts_to_mp4(ts_list,filename):
    videos = ts_list

    with open("ts_file_list.txt","w") as fp:
        lines = [f"file '{line}'" for line in videos] 
        fp.write("\n".join(lines))

    ffmpeg.input("ts_file_list.txt", f="concat", safe=0).output(filename+".mp4", c="copy").run()
