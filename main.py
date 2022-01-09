import module.my_module as m

def main():
    id = input("取得したい動画のIDを入力してね!:")
    url = 'https://www.youtube.com/watch?v=' + id
    last_time = m.getchat(url)
    t = m.chat_analysis(last_time)
    m.exciting_scene(t, id)
if __name__ == '__main__':
    main()