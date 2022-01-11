import re
import pytchat
import datetime
import youtube_dl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt
import MeCab
import collections
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

#target_commentで指定したコメントが一定時間にどれくらい含まれているかカウント
def chat_count(last_time):
    target_comments = []
    with open('C:\\Users\\ryota\\Desktop\\youtube\\input\\target_comment.txt', 'r') as f:
        target_comments = f.read().split("\n")
    x = []
    y = []
    xy = []
    comment_cnt = 0
    now_time = 0.0
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
                    td = str(datetime.timedelta(seconds=now_time))
                    td = '2012-12-29 ' + td
                    td = dt.strptime(td, '%Y-%m-%d %H:%M:%S')
                    x.append(td)
                    y.append(comment_cnt)
                    xy.append([td, comment_cnt])
                    comment_cnt = 0
                    now_time += interval_time
    fig, ax = plt.subplots()
    ax.plot(x, y)
    xfmt = mdates.DateFormatter("%H/%M/%S")
    xloc = mdates.HourLocator()
    ax.xaxis.set_major_locator(xloc)
    ax.xaxis.set_major_formatter(xfmt)
    # x軸の範囲
    #ax.set_xlim() 
    #ax.grid(True)
    plt.show()
    return xy

#特にコメントが盛り上がった時間の上位5つをurlにして抜き出す
def exciting_scene(xy, id):
    sorted_xy = sorted(xy, key=lambda x:x[1], reverse=True)
    for i in range(5):
        dtime = sorted_xy[i][0]
        hour = dtime.hour
        minute = dtime.minute
        second = dtime.second
        total = hour*60*60 + minute*60 + second
        print(dtime.strftime("%H:%M:%S"))
        print("https://www.youtube.com/watch?v=" + id + "&t=" + str(total))

def chat_analysis():
    m = MeCab.Tagger()
    all_words = []
    with open('C:\\Users\\ryota\\Desktop\\youtube\\output\\chat.txt', 'r') as f:
        for line in f:
            if len(line) == 0 or line == "\n":
                continue
            else:
                c = line.split("　")
                time = c[0]
                comment = c[1]
                node = m.parseToNode(comment)
                while node:
                    hin = node.feature.split(",")
                    if "gg" in hin:
                        print(hin)
                    hinshi = node.feature.split(",")[0]
                    if len(hin) >= 7: #hinshi in ["名詞","動詞","形容詞"]:
                        origin = node.feature.split(",")[7]
                        all_words.append(origin)
                    node = node.next
    c = collections.Counter(all_words)
    print(c["GG"])
