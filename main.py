from time import sleep
import pytchat #pychatをインポート
import time
chat = pytchat.create(video_id="") #対象動画のurlを指定
while chat.is_alive(): #動画が続いていれば
    for c in chat.get().items: #チャットを取得
        print(c.datetime, c.message)
    time.sleep(5) #sleepを入れないと空のデータが作成される可能性
