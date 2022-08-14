# Автопостинг комиксов [XKCD](https://xkcd.com/) в [группу VK](https://vk.com/autocomics_xkcd)

Проект xkcd_vk_autopost позволяет автоматизировать публикацию рандомного комикса XKCD в вашу 
группу ВКонтакте.


### Как работает

Скрипт vk_poster.py является главным. При работе он взаимодействует со следующими файлами:
- downloader.py - скрипт используется для загрузки комикса по ссылке и сохраняет его в указанную директорию
под оригинальным именем.


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
1) [Создали Standalone-приложение VK](https://vk.com/dev)
2) [Получить Token VK](https://vk.com/dev/implicit_flow_user)
3) Создали группу VK и [получили её id](https://regvk.com/id/)
4) Создайте файл .env в папке со скриптом и внесите в него данные:
```
VK_CLIENT_ID='ID Standalone-приложение'
VK_GROUP_ID='ID группы'
VK_TOKEN='Token VK'
VK_V_API='5.131, но может быть выше - смотри версию при получении Token VK' 
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
