# Трансляция названия играющего трека [Яндекс.Музыка](https://music.yandex.ru/) в поле bio telegram 

### Установка:

1. Для использования необходмо установить библиотеки:

```bash
pip install telethon==1.23.0
pip install yandex_music==1.0.0
```

Подробнее о библиотеках - [Telethon](https://pypi.org/project/Telethon/) и 
[yandex-music](https://pypi.org/project/yandex-music/).

2. Далее - создать файл ```secret_config.py```:
```python
# yandex music:
YA_TOKEN = r'token_from_yandex_music'

# telegram:
TG_API_ID = r'telegram_api_id'
TG_API_HASH = r'telegram_api_id_hash'
```

- Где токен для музыки можно получить по ссылке 
  [ниже](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d) 
  (или из [библиотеки](https://pypi.org/project/yandex-music/#id4));
- А токен и хэш для телеграмма [тут](https://my.telegram.org/) -> перейти на вкладку
  "API development tools".
  
### Запустить файл ```update_status.py``` и радоваться жизни. <sup><sub>(Или ловить ошибки.)</sub></sup>
