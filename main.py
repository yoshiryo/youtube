import module.my_module as m

def main():
    id = input("取得したい動画のIDを入力してね！:")
    url = 'https://www.youtube.com/watch?v=' + id
    last_time = m.getchat(url)
    m.chat_analysis(last_time)
if __name__ == '__main__':
    main()