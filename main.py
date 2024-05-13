# import subprocess
#
#
# def main():
#     games = {
#         '1': 'blackjack.py',
#         '2': 'hangman.py',
#         '3': 'mainframe.py',
#         '4': 'numberguesser.py',
#         '5': 'tetris.py',
#         '6': 'tictactoe.py',
#         '7': 'wordandmeaning.py'
#     }
#
#     # 显示所有游戏选项
#     print("Available games:")
#     for key, value in games.items():
#         print(f"{key}: {value[:-3]}")  # 输出游戏名，去掉.py后缀
#
#     # 获取用户输入
#     choice = input("Which game would you like to play? Enter the number: ")
#
#     # 启动对应的游戏脚本
#     if choice in games:
#         filepath = f"/Users/pusi/PycharmProjects/PYGames1/{games[choice]}"
#         subprocess.run(['python3', filepath])
#     else:
#         print("Invalid choice, please select a valid game number.")
#
#
# if __name__ == '__main__':
#     main()
#
import subprocess


def main():
    games = {
        '1': 'blackjack.py',
        '2': 'hangman.py',
        '3': 'mainframe.py',
        '4': 'numberguesser.py',
        '5': 'tetris.py',
        '6': 'tictactoe.py',
        '7': 'wordandmeaning.py'
    }

    # 显示所有游戏选项
    print("Available games:")
    for key, value in games.items():
        print(f"{key}: {value[:-3]}")  # 输出游戏名，去掉.py后缀

    # 获取用户输入
    choice = input("Which game would you like to play? Enter the number: ")

    # 启动对应的游戏脚本
    if choice in games:
        filepath = f"/Users/pusi/PycharmProjects/PYGames1/Games/{games[choice]}"
        subprocess.run(['python3', filepath])
    else:
        print("Invalid choice, please select a valid game number.")


if __name__ == '__main__':
    main()
