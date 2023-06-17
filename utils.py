from discord.app_commands import Choice

def format_currency(amount: float):
    return '{:,.2f}'.format(amount)

def get_auto_complete(text: str, list: dict[any]):
    data = []
    for key, value in list.items():
        if key.lower().startswith(text.lower()) or value.lower().startswith(text.lower()):
            data.append(Choice(name=f"{value} ({key})", value=key))
    return data[0:24]

fake_useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"