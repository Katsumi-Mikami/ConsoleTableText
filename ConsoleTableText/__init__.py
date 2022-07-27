import sys

TypeMessageSize = "auto"
messageSize = 20
styleBorder = ["# ", "#", "#"]


def edit(NewMessageSize: int = None, NewBorderStyle: list = None, NewTypeMessageSize: list = None):
    global messageSize, styleBorder, TypeMessageSize
    if NewTypeMessageSize is not None:
        if NewMessageSize in ["auto", "set"]:
            TypeMessageSize = NewTypeMessageSize
        else:
            print("\033[91m ConsoleTableText Error: The message length type should be set or auto")
            sys.exit(1)
    if NewMessageSize is not None:
        messageSize = NewMessageSize
    if NewBorderStyle is not None:
        if len(NewBorderStyle) == 3:
            if NewBorderStyle[0]:
                if len(NewBorderStyle[1]) <= 1 and len(NewBorderStyle[2]) <= 1:
                    styleBorder = NewBorderStyle
                else:
                    print(
                        f"\033[91m ConsoleTableText Error: The arguments of the new frame should consist of 3 parameters:"
                        f" horizontal upper side strip (no restrictions), horizontal upper central strip (1 character),"
                        f" vertical strip (1 character)")
                    sys.exit(1)
            else:
                print(
                    f"\033[91m ConsoleTableText Error: The arguments of the new frame should consist of 3 parameters:"
                    f" horizontal upper side strip (no restrictions), horizontal upper central strip (1 character),"
                    f" vertical strip (1 character)")
                sys.exit(1)
        else:
            print(
                f"\033[91m ConsoleTableText Error: The arguments of the new frame should consist of 3 parameters:"
                f" horizontal upper side strip (no restrictions), horizontal upper central strip (1 character),"
                f" vertical strip (1 character)")
            sys.exit(1)


def getTrueLength(string: str):
    codes = ['[95m', '[94m', '[96m', '[92m', '[93m', '[91m']
    codes2 = ['[0m', '[1m', '[4m']
    counter = 0
    t_list = []
    for i in range(len(string)):
        if string[i:i+4] in codes2:
            counter += 1
            t_list.append(string[i:i+4])
    for i in range(len(string)):
        if string[i:i+5] in codes:
            counter += 1
            t_list.append(string[i:i + 5])
    newString = ''
    for i in string:
        newString += i
        newString += " "
    newString = newString[:-1]
    width = len(string)
    for i in t_list:
        width -= len(i)
    return width, newString, string, counter*2


def generateMessageSize(lines=None, margins=None):
    if lines is None:
        lines = [""]
    if margins is None:
        margins = [1, 1]
    global messageSize, TypeMessageSize
    lengths = []
    if TypeMessageSize == "auto":
        for i in range(len(lines)):
            width, tmp1, tmp2, tmp3 = getTrueLength(lines[i])
            lengths.append(width)
        messageSize = max(lengths)+margins[0]*2 + 2
        return messageSize


def writeBorder():
    global messageSize, styleBorder
    halfLength = messageSize // 2
    isTypeBorderHasPlace = (messageSize - 2 * halfLength) % 2
    string = ''
    HalfString = ''
    tmp = ''
    counter = 0
    if halfLength % len(styleBorder[0]) == 0:
        HalfString = styleBorder[0] * (halfLength // len(styleBorder[0]))
    else:
        while len(HalfString) + len(styleBorder[0]) < halfLength:
            HalfString += styleBorder[0]
    BackHalfString = ''
    if halfLength % len(styleBorder[0]) == 0:
        BackHalfString = styleBorder[0] * (halfLength // len(styleBorder[0]))
    else:
        while len(BackHalfString) + len(styleBorder[0]) < halfLength:
            BackHalfString += styleBorder[0]
    BackHalfString = BackHalfString[::-1]
    BackHalfString = BackHalfString.replace("/", "BackSlashDev")
    BackHalfString = BackHalfString.replace('//', "/")
    BackHalfString = BackHalfString.replace("BackSlashDev", "//")
    string = HalfString + BackHalfString
    if len(string) == messageSize:
        print(string)
    else:
        print(HalfString + HalfString[-1] * (halfLength - len(HalfString)), end='')
        if isTypeBorderHasPlace:
            print(styleBorder[1], end='')
        print(HalfString[-1] * (halfLength - len(HalfString)) + BackHalfString, end='')
        print()


def line(lines: list = None, margins: list = None, textAlign=None):
    if lines is None:  # Задаем изначальные значения строк
        lines = [""]
    generateMessageSize(lines, margins)
    if margins is None:
        margins = [1, 0]
    if textAlign is None:
        textAlign = ("center " * len(lines)).split()
    if len(textAlign) < len(lines):
        for i in range(len(lines) - len(textAlign)):
            textAlign.append(textAlign[-1])
    if messageSize < len(styleBorder[0]) * 2:
        print(f"\033[91m ConsoleTableText Error: The message length must be at least {len(styleBorder[0]) * 2}")
        sys.exit(1)
    countLines = len(lines)
    lineWidth = 0
    for i in range(len(lines)):  # Проверка строк на превышение длины
        width, newString, newArray, temp = getTrueLength(lines[i])
        maxNewArray = max(newArray)
        lenOfNewMaxArray = len(maxNewArray)
        if lenOfNewMaxArray + margins[1] * 2 > messageSize:
            print(
                f"\033[91m ConsoleTableText Error: This line '{maxNewArray}' cannot be printed because its size {len(maxNewArray)} and the"
                f" horizontal margins {margins[1]} exceeds the minimum size {messageSize}.")
            sys.exit(1)

    for i in textAlign:
        if i not in ["left", "right", "center"]:
            print(
                f"\033[91m ConsoleTableText Error: Text alignment {textAlign} is not available")
            sys.exit(1)

    # Если все верно выводим строки

    writeBorder()
    for i in range(margins[1]):
        print(styleBorder[2], end="")
        print(" " * (messageSize - len(styleBorder[2]) * 2), end="")
        print(styleBorder[2])
    for i in range(len(lines)):
        TrueWidth, newString, newArray, countExtSpace = getTrueLength(lines[i])
        if textAlign[i] == "left":
            codes = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[0m', '\033[1m',
                     '\033[4m']
            print(styleBorder[2], end="")
            print(" " * (margins[0]), end="")
            print(lines[i], end="")
            print(" " * (messageSize - len(styleBorder[2]) * 2 - margins[0] - TrueWidth), end="")
            print(styleBorder[2])
        if textAlign[i] == "right":
            print(styleBorder[2], end="")
            print(" " * (messageSize - len(styleBorder[2]) * 2 - margins[0] - TrueWidth), end="")
            print(lines[i], end="")
            print(" " * margins[0], end="")
            print(styleBorder[2])
        if textAlign[i] == "center":
            print(styleBorder[2], end="")
            print(" " * (messageSize - len(styleBorder[2]) * 2 - TrueWidth - ((messageSize - len(styleBorder[2]) * 2 - TrueWidth) // 2)), end="")
            print(lines[i], end="")
            print(" " * ((messageSize - len(styleBorder[2]) * 2 - TrueWidth) // 2), end="")
            print(styleBorder[2])
    for i in range(margins[1]):
        print(styleBorder[2], end="")
        print(" " * (messageSize - len(styleBorder[2]) * 2), end="")
        print(styleBorder[2])
    writeBorder()
