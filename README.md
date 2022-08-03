# ConsoleTableText
<h2>RUS:</h2>
<p>ConsoleTableText - это пакет для Python, который поможет вам выводить сообщения в консоль в рамках с адаптивным изменением длины сообщение. Так же длину сообщениня можно установить в ручную.</p>
<h3>В последнем обновлении:</h3>
<ul>
<li>
Исправлены некоторые ошибка работы с библиотекой
</li>
<li>
Оптимизирована работа программы
</li>
</ul>

[Github-репозиторий](https://example.com/)

<h4>Последняя версия: v. 1.0.1</h4>

<br>
<br>
<br>


<h2>ENG:</h2>

<p>Console Table Test is a Python package that will help you output messages to the console in a console with adaptive message length change. The message length can also be set manually.</p>
<h3>In the latest update:</h3>
<ul>
<li>
Fixed some errors with the library
</li>
<li>
Optimized the operation of the program
</li>
</ul>

[Github-repository](https://example.com/)

<h4>Latest version: v. 1.0.1</h4>

<h2>Code Example \ Пример кода:</h2>

<code style="border-radius: 0; margin: 0; padding: 3px">
import ConsoleTableText<br>
ConsoleTableText.edit(NewTypeMessageSize="set", NewMessageSize=35, NewBorderStyle=["# ", "!", "-", "."])<br>
ConsoleTableText.line(["Console Table Text Example", "-border-", "\033[1mSome Text\033[0m", "\033[1mKey-value\033[0m -value- \033[94mText Example\033[0m"], textAlign=["center", "left"])
</code>