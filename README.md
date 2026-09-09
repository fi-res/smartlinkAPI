# SmartLinkAPI

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue)](www.python.org) ![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green) [![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

Прокси на UserSide API 3.21+ со своей системой авторизации.
Часть функционала работает не через API, так как там реализованы не все фичи что есть на сайте (как бы они есть, но там надо делать несколько запросов, из-за чего запрос выполняется гораздо дольше). Скрипт авторизовывается на сайте, парсит готовый html и преобразует его в JSON.

## Фичи
 - REST API для UserSide ERP
 - Кэширование имен персонала и названий бригад для ускоренной работы
 - Перезапуск ONT и переключение CATV через SSH
 - Получение информации по ONT через SNMP

## Лицензия
Лицензировано под [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)
