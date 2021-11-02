from time import sleep
import pytchat #pychatをインポート
import time
chat = pytchat.create(video_id="") #対象動画のurlを指定
while chat.is_alive():
    for c in chat.get().items:
        print(c.datetime, c.message)
    time.sleep(5)
