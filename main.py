def main():
    while True:
        print("選択してください：")
        print("1: sato")
        print("2: 選択肢2")
        print("3: 選択肢3")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("satoの自己紹介です")
        elif choice == "2":
            print("選択肢2が選ばれました。")
        elif choice == "3":
            print("選択肢3が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

