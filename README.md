# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

Скачайте репозиторий.

Установите виртуальное окружение и запустите его:
```
python3 -m virtualenv virtualenv_name
source virtualenv_name/bin/activate
```

Установите пакеты из файла requirements.txt:
```
python -m pip install -r requirements.txt
```

В корень проекта положите файл с названием `wine.xlsx`. Пример содержимого файла:

| Категория| Название | Сорт | Цена | Картинка | Акция |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение |
| Напитки | Коньяк классический | | 350 | konyak_klassicheskyi.png | |
| Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png | |
| Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png | |
| Красные вина | Хванчкара | Александраули | 550 | hvanchkara.png | |
| Белые вина | Кокур | Кокур | 450 | kokur.png | |
| Красные вина | Киндзмараули | Саперави | 550 | kindzmarauli.png | |
| Напитки | Чача | | 299 | chacha.png | Выгодное предложение |
| Напитки | Коньяк кизиловый | | 350 | konyak_kizilovyi.png | |




Запустите сайт командой:
```
python main.py
```

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000). Если вы увидите страничку, значит всё работает корректно.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
