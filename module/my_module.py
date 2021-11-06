import pytchat
import datetime
import youtube_dl
import matplotlib.pyplot as plt
#動画ダウンロード
def download(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

#チャット取得
def getchat(url):
    with open('C:\\Users\\ryota\\Desktop\\youtube\\output\\chat.txt', mode='w') as f:
        f.write("")
    p = True
    chat = pytchat.create(video_id=url) #対象動画のurlを指定
    while chat.is_alive(): #動画が続いていれば
        lines = []
        for c in chat.get().items: #チャットを取得
            tstr = c.elapsedTime
            if "-" in tstr:
                continue
            else:
                if tstr.count(":") == 1:
                    tstr = "0:" + tstr
                tdatetime = datetime.datetime.strptime(tstr, '%H:%M:%S') #datetimeに変換
                if p: #最初のチャットを基準
                    p = False
                    standard_time = tdatetime
                    chat_message = "0" + "　" + c.message + "\n"
                else: #それ以外は差を計算
                    else_time = tdatetime
                    difference_time = else_time - standard_time
                    chat_message =  str(difference_time.seconds) + "　" + c.message + "\n"
                lines.append(chat_message) #一度listに格納
        with open('C:\\Users\\ryota\\Desktop\\youtube\\output\\chat.txt', 'a+', encoding='UTF-8') as f: #write操作は重たい処理なのでなるべく呼び出さない
            f.write("\n".join(lines))
    return difference_time.seconds

def chat_analysis(last_time):
    target_comments = []
    with open('C:\\Users\\ryota\\Desktop\\youtube\\input\\target_comment.txt', 'r') as f:
        target_comments = f.read().split("\n")
    x = []
    y = []
    comment_cnt = 0
    now_time = 0
    interval_time = 30
    plt.xlim(0,(int(last_time)//interval_time) + interval_time)
    with open('C:\\Users\\ryota\\Desktop\\youtube\\output\\chat.txt', 'r') as f:
        for line in f:
            if len(line) == 0 or line == "\n":
                continue
            else:
                c = line.split("　")
                time = c[0]
                comment = c[1]
                if now_time <= int(time) < now_time + interval_time:
                    for tc in target_comments:
                        if tc in comment:
                            comment_cnt += 1
                else:
                    x.append(now_time//interval_time)
                    y.append(comment_cnt)
                    comment_cnt = 0
                    now_time += interval_time
    plt.plot(x, y)
    plt.show()
