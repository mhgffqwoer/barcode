from tkinter import Tk, Canvas

WHITE_CODE = "00000000000"
CODE_B = "11010010000"
STOP_CODE = "11000111010"

BAR_CODE_HEIGHT = 200

WHITE_COLOR = "#ffffff"
BLACK_COLOR = "#000000"

UPPER_BAR_CODE_BORDER_Y = 190
BOTTOM_BAR_CODE_BORDER_Y = 10
SHIFT_X = 7


def codes(i: int, j: int):  # функция создания и вывода кодов
    codes = [
        [0, " ", "11011001100"],
        [1, "!", "11001101100"],
        [2, '"', "11001100110"],
        [3, "#", "10010011000"],
        [4, "$", "10010001100"],
        [5, "%", "10001001100"],
        [6, "&", "10011001000"],
        [7, "'", "10011000100"],
        [8, "(", "10001100100"],
        [9, ")", "11001001000"],
        [10, "*", "11001000100"],
        [11, "+", "11000100100"],
        [12, ",", "10110011100"],
        [13, "-", "10011011100"],
        [14, ".", "10011001110"],
        [15, "/", "10111001100"],
        [16, "0", "10011101100"],
        [17, "1", "10011100110"],
        [18, "2", "11001110010"],
        [19, "3", "11001011100"],
        [20, "4", "11001001110"],
        [21, "5", "11011100100"],
        [22, "6", "11001110100"],
        [23, "7", "11101101110"],
        [24, "8", "11101001100"],
        [25, "9", "11100101100"],
        [26, ":", "11100100110"],
        [27, ";", "11101100100"],
        [28, "<", "11100110100"],
        [29, "=", "11100110010"],
        [30, ">", "11011011000"],
        [31, "?", "11011000110"],
        [32, "@", "11000110110"],
        [33, "A", "10100011000"],
        [34, "B", "10001011000"],
        [35, "C", "10001000110"],
        [36, "D", "10110001000"],
        [37, "E", "10001101000"],
        [38, "F", "10001100010"],
        [39, "G", "11010001000"],
        [40, "H", "11000101000"],
        [41, "I", "11000100010"],
        [42, "J", "10110111000"],
        [43, "K", "10110001110"],
        [44, "L", "10001101110"],
        [45, "M", "10111011000"],
        [46, "N", "10111000110"],
        [47, "O", "10001110110"],
        [48, "P", "11101110110"],
        [49, "Q", "11010001110"],
        [50, "R", "11000101110"],
        [51, "S", "11011101000"],
        [52, "T", "11011100010"],
        [53, "U", "11011101110"],
        [54, "V", "11101011000"],
        [55, "W", "11101000110"],
        [56, "X", "11100010110"],
        [57, "Y", "11101101000"],
        [58, "Z", "11101100010"],
        [59, "[", "11100011010"],
        [60, "\\", "11101111010"],
        [61, "]", "11001000010"],
        [62, "^", "11110001010"],
        [63, "_", "10100110000"],
        [64, "`", "10100001100"],
        [65, "a", "10010110000"],
        [66, "b", "10010000110"],
        [67, "c", "10000101100"],
        [68, "d", "10000100110"],
        [69, "e", "10110010000"],
        [70, "f", "10110000100"],
        [71, "g", "10011010000"],
        [72, "h", "10011000010"],
        [73, "i", "10000110100"],
        [74, "j", "10000110010"],
        [75, "k", "11000010010"],
        [76, "l", "11001010000"],
        [77, "m", "11110111010"],
        [78, "n", "11000010100"],
        [79, "o", "10001111010"],
        [80, "p", "10100111100"],
        [81, "q", "10010111100"],
        [82, "r", "10010011110"],
        [83, "s", "10111100100"],
        [84, "t", "10011110100"],
        [85, "u", "10011110010"],
        [86, "v", "11110100100"],
        [87, "w", "11110010100"],
        [88, "x", "11110010010"],
        [89, "y", "11011011110"],
        [90, "z", "11011110110"],
        [91, "{", "11110110110"],
        [92, "|", "10101111000"],
        [93, "}", "10100011110"],
        [94, "~", "10001011110"],
        [95, "None", "10111101000"],
        [96, "None", "10111100010"],
        [97, "None", "11110101000"],
        [98, "None", "11110100010"],
        [99, "None", "10111011110"],
        [100, "None", "10111101110"],
        [101, "None", "11101011110"],
        [102, "None", "11110101110"],
    ]
    if (i != None) and (j != None):
        return codes[i][j]  # выводит элемент
    else:
        return codes  # выводит весь массив codes


def search_codes(symbol, command: str):  # поиск кодов для символа
    for i in range(len(codes(None, None))):
        if symbol == codes(i, 1):
            if command == "code":
                return codes(i, 2)
            if command == "number":
                return codes(i, 0)
        if (symbol == codes(i, 0)) and (command == "check_sum"):
            return codes(i, 2)


def barcode_bin(
    line: str,
) -> str:  # barcode = white + code_b + (line) + check_sum + stop + white
    barcode = WHITE_CODE + CODE_B
    symbol_number = 1  # номер символа в троке
    check_sum = 104  # начальная контрольная сумма
    for i in line:
        barcode += search_codes(i, "code")
        # контрольная сумма = номер символа * на номер в таблице
        check_sum += search_codes(i, "number") * symbol_number
        symbol_number += 1
    barcode += search_codes(check_sum % 103, "check_sum")
    barcode += STOP_CODE + WHITE_CODE
    return barcode


def print_bar_code(
    canvas: Canvas, bar_code: str, left_edge_x: int = 10, right_edge_x: int = 17
):
    for symb in bar_code:
        current_color = WHITE_COLOR if symb == "0" else BLACK_COLOR
        canvas.create_rectangle(
            left_edge_x,
            BOTTOM_BAR_CODE_BORDER_Y,
            right_edge_x,
            UPPER_BAR_CODE_BORDER_Y,
            outline=current_color,
            fill=current_color,
        )
        left_edge_x += SHIFT_X
        right_edge_x += SHIFT_X


def main():
    seq_to_code = input("Input symbol sequence for generate bar-code: ")
    bar_code = barcode_bin(seq_to_code)

    bar_code_width = len(bar_code) * 7 + 20

    root = Tk()
    root["bg"] = WHITE_COLOR
    root.resizable(width=False, height=False)
    canvas = Canvas(root, height=BAR_CODE_HEIGHT, width=bar_code_width)
    canvas.pack()
    canvas.create_rectangle(
        0, 0, bar_code_width, BAR_CODE_HEIGHT, outline=WHITE_COLOR, fill=WHITE_COLOR
    )

    print_bar_code(canvas, bar_code)

    root.mainloop()


if __name__ == "__main__":
    main()
