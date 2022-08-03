import sys

TypeMessageSize = "auto"
messageSize = 20
styleBorder = ["# ", "#", "#", "."]


# Вспомогательная функция изменения параметров пакета
def edit(NewMessageSize: int = None, NewBorderStyle: list = None, NewTypeMessageSize: list = None):
    global messageSize, styleBorder, TypeMessageSize
    if NewTypeMessageSize is not None:
        if NewTypeMessageSize in ["auto", "set"]:
            TypeMessageSize = NewTypeMessageSize
        else:
            print("\033[91m ConsoleTableText Error: The message length type should be 'set' or 'auto'")
            sys.exit(1)
    if NewMessageSize is not None:
        if NewMessageSize > 0:
            messageSize = NewMessageSize
        else:
            print("\033[91m ConsoleTableText Error: The message length type should be 'set' or 'auto'")
            sys.exit(1)
    if NewBorderStyle is not None:
        if len(NewBorderStyle) == 4:
            if NewBorderStyle[0]:
                if len(NewBorderStyle[1]) <= 1 and len(NewBorderStyle[2]) <= 1 and len(NewBorderStyle[3]) <= 1:
                    styleBorder = NewBorderStyle
                else:
                    print(
                        f"\033[91m ConsoleTableText Error: The arguments of the new frame should consist of 4 parameters:"
                        f" horizontal upper side strip (no restrictions), horizontal upper central strip (1 character),"
                        f" vertical strip (1 character), key-value table separator (1 character)")
                    sys.exit(1)
            else:
                print(
                    f"\033[91m ConsoleTableText Error: The arguments of the new frame should consist of 4 parameters:"
                    f" horizontal upper side strip (no restrictions), horizontal upper central strip (1 character),"
                    f" vertical strip (1 character), key-value table separator (1 character)")
                sys.exit(1)
        else:
            print(
                f"\033[91m ConsoleTableText Error: The arguments of the new frame should consist of 4 parameters:"
                f" horizontal upper side strip (no restrictions), horizontal upper central strip (1 character),"
                f" vertical strip (1 character), key-value table separator (1 character)")
            sys.exit(1)


# Сис. функция генерация длины сообщения
def getTrueLength(string: str):
    codes = ['[95m', '[94m', '[96m', '[92m', '[93m', '[91m']
    codes2 = ['[0m', '[1m', '[4m']
    counter = 0
    t_list = []
    for i in range(len(string)):
        if string[i:i + 4] in codes2:
            counter += 1
            t_list.append(string[i:i + 4])
    for i in range(len(string)):
        if string[i:i + 5] in codes:
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
    return width, newString, string, counter * 2


# Сис. функция генерация длины сообщения
def generateMessageSize(lines=None, margins=None):
    if lines is None:
        lines = [""]
    if margins is None:
        margins = [1, 1]
    global messageSize, TypeMessageSize
    lengths = []
    for i in range(len(lines)):
        width, tmp1, tmp2, tmp3 = getTrueLength(lines[i])
        lengths.append(width)
    tmpMessageSize = max(lengths) + margins[0] * 2 + 2
    if TypeMessageSize == "auto":
        messageSize = tmpMessageSize
    return tmpMessageSize


# Сис. функция вывода рамки до и после сообщения
def writeBorder():
    global messageSize, styleBorder
    lenOfHalfString = messageSize // 2
    isTypeBorderHasPlace = (messageSize - 2 * lenOfHalfString) % 2
    HalfString = ''
    if lenOfHalfString % len(styleBorder[0]) == 0:
        HalfString = styleBorder[0] * (lenOfHalfString // len(styleBorder[0]))
    else:
        while len(HalfString) + len(styleBorder[0]) < lenOfHalfString:
            HalfString += styleBorder[0]
    BackHalfString = ''
    if lenOfHalfString % len(styleBorder[0]) == 0:
        BackHalfString = styleBorder[0] * (lenOfHalfString // len(styleBorder[0]))
    else:
        while len(BackHalfString) + len(styleBorder[0]) < lenOfHalfString:
            BackHalfString += styleBorder[0]
    BackHalfString = BackHalfString[::-1]
    string = HalfString + BackHalfString
    if len(string) == messageSize:
        print(string)
    else:
        print(HalfString + HalfString[-1] * (lenOfHalfString - len(HalfString)), end='')
        if isTypeBorderHasPlace:
            print(styleBorder[1], end='')
        print(HalfString[-1] * (lenOfHalfString - len(HalfString)) + BackHalfString, end='')
        print()


# Основная функция вывода сообщение
def line(lines: list = None, margins: list = None, textAlign=None):
    # Подготовка
    if lines is None:  # Задаем изначальные значения строк
        lines = [""]
    if margins is None:  # Задаем изначальные отступы
        margins = [1, 0]
    if textAlign is None:  # Задаем изначальную центровку текста
        textAlign = ("center " * len(lines)).split()
    if len(textAlign) < len(lines):  # Добавляем тип центровки текст, при его отсутствии
        for i in range(len(lines) - len(textAlign)):
            textAlign.append(textAlign[-1])
    minimumMessageSize = generateMessageSize(lines, margins)
    if messageSize < minimumMessageSize:  # Проверка сообщение на длину
        print(f"\033[91m ConsoleTableText Error: The message length must be at least {minimumMessageSize}")
        sys.exit(1)

    # Задаем центровку текста
    for i in textAlign:
        if i not in ["left", "right", "center"]:  # Проверяем центровку текста
            print(
                f"\033[91m ConsoleTableText Error: Text alignment {textAlign} is not available")
            sys.exit(1)

    # Если все верно выводим строки

    writeBorder()
    # Вывод отступов перед текстом
    for i in range(margins[1]):
        print(styleBorder[2], end="")
        print(" " * (messageSize - len(styleBorder[2]) * 2), end="")
        print(styleBorder[2])
    # Вывод строк кода с центровкой
    for i in range(len(lines)):
        TrueWidth, newString, newArray, countExtSpace = getTrueLength(lines[i])
        if lines[i] == "-border-":
            writeBorder()
        elif lines[i].count("-value-") == 0:
            if textAlign[i] == "left":
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
                print(" " * (messageSize - len(styleBorder[2]) * 2 - TrueWidth - (
                        (messageSize - len(styleBorder[2]) * 2 - TrueWidth) // 2)), end="")
                print(lines[i], end="")
                print(" " * ((messageSize - len(styleBorder[2]) * 2 - TrueWidth) // 2), end="")
                print(styleBorder[2])
        else:
            key_value_line = lines[i].split('-value-')
            subLen = 0
            for k in key_value_line:
                TrueWidth_, newString, newArray, countExtSpace = getTrueLength(k)
                subLen += TrueWidth_
            print(styleBorder[2], end="")
            print(" " * margins[0], end="")
            print(key_value_line[0], end="")
            print(styleBorder[3] * (messageSize - 2 - margins[0] * 2 - subLen), end="")
            print(key_value_line[1], end="")
            print(" " * margins[0], end="")
            print(styleBorder[2])
    # Вывод отступов после текста
    for i in range(margins[1]):
        print(styleBorder[2], end="")
        print(" " * (messageSize - len(styleBorder[2]) * 2), end="")
        print(styleBorder[2])
    writeBorder()
