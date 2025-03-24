def main():
    while True:
        print("選択してください：")
        print("1: sato")
        print("2: kaoru")
        print("3: ここを変更")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("satoの自己紹介です")
        elif choice == "2":
            print("kaorudesu")
        elif choice == "3":
            print("ここを変更。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

