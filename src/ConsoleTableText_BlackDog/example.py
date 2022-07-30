import ConsoleTableText
ConsoleTableText.edit(NewTypeMessageSize="set", NewMessageSize=35, NewBorderStyle=["# ", "!", "-", "."])
ConsoleTableText.line(["Console Table Text Example", "-border-", "\033[1mSome Text\033[0m", "\033[1mKey-value\033[0m -value- \033[94mText Example\033[0m"], mode="table", textAlign=["center", "left"])