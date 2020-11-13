<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>matrix_print</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Представляю вам matrix_print!</h1>
    <h2>1.Введение</h2>
    <p>
        Итак, у вас вопрос: что это? <br>
        Это библиотека <strong>python</strong> с эффектом печати текста, чтобы... 
        Не знаю для чего может вам понадобится 
        ¯\_(ツ)_/¯<br>
        Вы можете сделать по типу квеста с чатом или еще чего-то... Всё по вашему желанию! 
    </p>
    <br>
    <h2>2.Команды</h2>
    <p>Первое, что мы должны импортировать это сам <strong>matrix_print</strong><br></p>
    <p class="box"><code>
        1|<strong>import</strong> matrix_print <strong>as</strong> mp
    </code></p>
    <p>Дальше можно приступать к работе!</p>
    <p class="comm"><code>
        1|mp.printc(text, time) #классическая печать <br>
        2|mp.printu(text, time, name_of_user) #по типу отправки сообщения от пользователя<br>
        3|mp.matrix_input(text, time, your_name="") #тот же input, но с эффектом печати<br>  
    </code></p>
    <p>Также существует особый класс - <strong class="gradient-1">ColorPrint</strong><br></p>
    <p>Если вам не нравится писать mp.ColorPrint.x, то можно просто импортировать класс<br></p>
    <p class="box1"><code>
        1|<strong>from</strong> matrix_print <strong>import</strong> ColorPrint <strong>as</strong> col <br>
    </code></p>
    <p>Примечание: если библиотека не обнаружит <strong class="gradient-1">Colorama</strong>, то она выведет ошибку <br></p>
    <p class="comm"><code>
        matrix_print.matrix.ColoramaIsNotInstalledError: module colorama is not installed <br>
    </code></p>
    <p>Но если вы установили этот модуль, то вы молодцы! <br></p>
    <p class="comm"><code>
        1|col.red(text, time) #печать красный текстом <br>
        2|col.bg_red(text, time) #печать текстом с красным фоном <br>
        3|col.yellow(text, time) #печать жёлтым текстом <br>
        4|col.bg_yellow(text, time) #печать текстом с жёлтым фоном <br>
        5|col.blue(text, time) #печать синим текстом <br>
        6|col.bg_blue(text, time) #печать текстом с синим фоном <br>
        7|col.green(text, time) #печать зеленым текстом <br>
        8|col.bg_green(text, time) #печать с синим фоном <br>
        9|col.bg_white(text, time) #печать с белым фоном <br>
    </code></p>
    <h2>3.Пример использования</h2>
    <p class="comm"><code>
        <strong>import</strong> matrix_print <strong>as</strong> mp  <br>
        <strong>from</strong> matrix_print <strong>import</strong> ColorPrint <strong>as</strong> col  <br>
        <strong>import</strong> random <br>
        <strong>import</strong> time  <br>
        <strong>import</strong> sys  <br>
 <br>
        mp.printc("hi, welcome to elOS", 0.1) <br>
        mp.printc("elastic Operating System", 0.1) <br>
        mp.printc("downloading files") <br>
        time.sleep(1) <br>
        wat = random.choice(["ERROR", "ok"]) <br>
        if wat == "ERROR": <br>
        &emsp;&emsp;col.red(wat, 0.1) <br>
        &emsp;&emsp;time.sleep(1) <br>
        &emsp;&emsp;sys.exit() <br>
        else: <br>
        &emsp;&emsp;col.green(wat, 0.1) <br>
    </code></p>
    <h2>4.Релизы</h2>
    <p>0.1 - появился colorprint в отдельном файле <br></p>
    <p>0.2 - появился matrix_input <br></p>
    <p>0.3 - появились задние фоны для colorprint <br></p>
    <p>0.4 - colorprint был перенесен в первый файл и стал классом <strong class="gradient-1">
    ColorPrint</strong> <br></p>
    <p>0.5 - появился <strong>print_edit</strong>
    <h2>5.Планы</h2>
    <p>
        сейчас в планах идет:
        <ul>
            <li>Создание печати с паузой
            <li>Возможность удаления символов при печати 
        </ul>
    </p>
    <a href="https://vk.com/utilerain">
        <img 
        src="https://www.flaticon.com/svg/static/icons/svg/889/889151.svg", 
        width="60px",
        height="40px">
    </a>
</body>
</html>
