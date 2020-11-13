import time as t
class ColoramaIsNotInstalledError(Exception):
    def __init__(self, text):
        self.txt = text 
try:
    from colorama import Fore, Back, Style
    from colorama import init    


    def printc(text, time): #classic matrix print
        my_string = text
        for string in my_string:
            t.sleep(time)
            print(string, end = "", flush = True)
        print(flush = False)

    def printu(text, time, name_of_user): #matrix print but msg from user or machine
        my_string = text
        print(name_of_user)
        for string in my_string:
            t.sleep(time)
            print(string, end = "", flush = True)
        print(flush = False)

    def matrix_input(text, time, your_name=""): #print text from user

        my_string = input(text)
        if your_name == "":
            your_name = "you:" #default 
        print(your_name)
        for string in my_string:
            t.sleep(time)

            print(string, end = "", flush = True)
        print(flush = False)

    def print_edit(text, time, second_text, mnoj=0):
        my_string = text
        text = "\b"
        text2 = second_text
        for string in my_string:
            print(string, end="", flush=True)
            t.sleep(time)
        for delet in text:
            print(delet * mnoj, end="", flush=True)
            t.sleep(time)
        for text1 in text2:
            print(text1, end="", flush=True)
            t.sleep(time)
        print(flush=False)


    class ColorPrint:
        
        '''
        colorprint.green(text, time) - text with green color
        colorprint.red(text, time) - text with red color
        colorprint.blue(text, time) - text with blue color
        colorprint.purple(text, time) - text with purple color
        colorprint.yellow(text, time) - text with yellow color
        colorprint.bg_red(text, time) - text with background red color
        '''

        init(autoreset = True) 
        
        def green(text, time): #matrix print with green color
            color = Fore.GREEN
            my_string = text
            for string in my_string:
                t.sleep(time)
                print(color + string, end = "", flush = True)
            print(flush = False)
        def red(text, time): #matrix print with red color
            color = Fore.RED
            my_string = text
            for string in my_string:
                t.sleep(time)
                print(color + string, end = "", flush = True)
            print(flush = False)
        def blue(text, time): #matrix print with blue color
            color = Fore.BLUE
            my_string = text
            for string in my_string:
                t.sleep(time)
                print(color + string, end = "", flush = True)
            print(flush = False)
        def yellow(text, time): #matrix print with yellow color
            color = Fore.YELLOW
            my_string = text
            for string in my_string: 
                t.sleep(time)
                print(color + string, end = "", flush = True)
            print(flush = False)
        def bg_red(text, time): #matrix print with bg
            color = Back.RED
            my_string = text
            for string in my_string: 
                t.sleep(time)
                print(color + string, end = "", flush = True)
            print(flush = False)
        def bg_green(text, time):
            bgcolor = Back.GREEN
            color = Fore.BLACK
            my_string = text
            for string in my_string: 
                t.sleep(time)
                print(color + bgcolor + string, end = "", flush = True)
            print(flush = False)
        def bg_blue(text, time):
            bgcolor = Back.BLUE
            color = Fore.BLACK
            my_string = text
            for string in my_string: 
                t.sleep(time)
                print(color + bgcolor + string, end = "", flush = True)
            print(flush = False)
        def bg_yellow(text, time):
            bgcolor = Back.YELLOW
            color = Fore.BLACK
            my_string = text
            for string in my_string: 
                t.sleep(time)
                print(color + bgcolor + string, end = "", flush = True)
            print(flush = False)
        def bg_white(text, time):
            bgcolor = Back.WHITE
            color = Fore.BLACK
            my_string = text
            for string in my_string: 
                t.sleep(time)
                print(color + bgcolor + string, end = "", flush = True)
            print(flush = False)
except ModuleNotFoundError:
        raise ColoramaIsNotInstalledError("module colorama is not installed")

