import os

stick_man_art =(" o ",
                "/|\\",
                "/ \\")

def show_message(message, max_width=25):
    words_of_the_message = message.split()
    lines = []
    current_line = ""

    for word in words_of_the_message:
        if len(word) > max_width:
            if current_line:
                lines.append(current_line)

            while len(word) > max_width:
                lines.append(word[:max_width])
                word = word[max_width:]

            current_line = word

        else:
            test = current_line + " " + word if current_line else word

            if len(test) <= max_width:
                current_line = test
            else:
                lines.append(current_line)
                current_line = word

    if current_line:
        lines.append(current_line)

    width = max(len(l) for l in lines)
    border = "-" * (width + 4)

    print(border)
    for l in lines:
        print("| " + l.ljust(width) + " |")
    print(border)
    print(" v")


def show_stick_man():
    for line in stick_man_art:
        print(line)
    print()


def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    is_running = True
    default_message = "Hi, Write something, so i can say it outloud !!"

    show_message(default_message)
    show_stick_man()

    while is_running:
        message = input("type something (0 to leave): ")
        clean_terminal()

        show_message(message)
        show_stick_man()


        if message == "0":
            clean_terminal()
            is_running = False
       

    print("Bye!!!")    

        

if __name__ == "__main__":
    main()




