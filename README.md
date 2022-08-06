# ConsoleTableText
<h2>RUS:</h2>
<p>ConsoleTableText - это пакет для Python, который поможет вам выводить сообщения в консоль в рамках с адаптивным изменением длины сообщение. Так же длину сообщениня можно установить в ручную.</p>
<h3>В последнем обновлении:</h3>
<ul>
<li>
Небольшое исправления работы с пользователем
</li>
</ul>

[Github-репозиторий](https://github.com/Blackdog7777/ConsoleTableText)

<h4>Последняя версия: v. 1.0.2</h4>

<br>
<br>
<br>


<h2>ENG:</h2>

<p>Console Table Test is a Python package that will help you output messages to the console in a console with adaptive message length change. The message length can also be set manually.</p>
<h3>In the latest update:</h3>
<ul>
<li>
Small user-usage fixes
</li>
</ul>

[Github-repository](https://github.com/Blackdog7777/ConsoleTableText)

<h4>Latest version: v. 1.0.2</h4>

<h2>Code Example \ Пример кода:</h2>

<code style="border-radius: 0; margin: 0; padding: 3px">
from consoletabletext import edit, line<br>
ConsoleTableText.edit(NewTypeMessageSize="set", NewMessageSize=35, NewBorderStyle=["# ", "!", "-", "."])<br>
ConsoleTableText.line(["Console Table Text Example", "-border-", "\033[1mSome Text\033[0m", "\033[1mKey-value\033[0m -value- \033[94mText Example\033[0m"], textAlign=["center", "left"])
</code>