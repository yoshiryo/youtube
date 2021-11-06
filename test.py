import pytchat
import datetime

def main():
    def getchat(url):
        p = True
        chat = pytchat.create(video_id=url) #対象動画のurlを指定
        while chat.is_alive(): #動画が続いていれば
            for c in chat.get().items: #チャットを取得
                tstr = c.datetime
                tdatetime = datetime.datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S') #datetimeに変換
                if p: #最初のチャットを基準
                    p = False
                    standard_time = tdatetime
                    chat_message = "0" + "　" + c.message + "\n"
                else: #それ以外は差を計算
                    else_time = tdatetime
                    difference_time = else_time - standard_time
                    chat_message =  str(difference_time.seconds) + "　" + c.message + "\n"
                print(chat_message)
    #getchat("https://www.youtube.com/watch?v=5yDQRxUNeIQ")

    tstr1 = "0:28"
    tstr2 = "4:50:04"
    if tstr1.count(":") == 1:
        tstr1 = "0:" + tstr1

    tdatetime1 = datetime.datetime.strptime(tstr1, '%H:%M:%S')
    tdatetime2 = datetime.datetime.strptime(tstr2, '%H:%M:%S')
    difference_time = tdatetime2 - tdatetime1
    print(difference_time.seconds)

if __name__ == '__main__':
    main()