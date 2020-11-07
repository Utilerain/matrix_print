from matrix_print import *
from matrix_print import ColorPrint as col
from time import sleep
printc("test1 ", 0.1)
sleep(0.5)
printc("pass ", 0.2)
sleep(0.5)
printc("test2 ", 0.1)
sleep(0.5)
printu("test msg ", 0.2, "user")
printc("pass ", 0.1)
sleep(0.5)
printc("test input ", 0.2)
matrix_input("please, input this: ", 0.2, "")
printc("pass ", 0.2)
printc("TEST1 PASSED ", 0.3)
sleep(1)

col.red("test_red ", 0.2)
col.green("test_green ", 0.2)
col.yellow("test_yellow ", 0.2)
col.blue("test_blue", 0.2)
col.green("TEST2 PASSED ", 0.4)
try:
    col.bg_red("test_bg_red", 0.1)
    col.bg_yellow("test_bg_yellow", 0.1)
    col.bg_green("test_bg_green", 0.1)
    col.bg_blue("test_bg_blue", 0.1)
    col.bg_white("test_bg_white", 0.2)
    col.bg_green("TEST3 PASSED", 0.3)
except:
    printc("error", 0.3)

print("test completed")
sleep(1)