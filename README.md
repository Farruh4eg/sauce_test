# Saucedemo Autotests

Проект автоматизированного тестирования формы логина сайта saucedemo.com

## Реализованные сценарии
1. Успешная авторизация (`` `standard_user` ``).
2. Попытка входа заблокированного пользователя (`` `locked_out_user` ``).
3. Вход с неверным паролем.
4. Валидация пустых полей (логин/пароль).
5. Тестирование пользователя с задержкой загрузки (`` `performance_glitch_user` ``).

## Стек
- Python 3.12
- Selenium
- Pytest
- Allure
- Docker

## Локальный запуск

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Запустите тесты:

``` bash
pytest --alluredir=allure-results
```

3. Просмотр отчета:

```bash
allure serve allure-results
```

---

## Запуск в Docker

1. Соберите образ:

```bash
DOCKER_BUILDKIT=1 docker build -t sauce_test .
```

> Если при сборке вылетает ошибка buildx component is missing, установите его:
- Arch Linux:

```bash
sudo pacman -S docker-buildx
```

2. Запустите контейнер:
- Linux / MacOS / PowerShell:

```bash
docker run --rm -v $(pwd)/allure-results:/app/allure-results sauce_test
```

- Windows CMD:

```bash
docker run --rm -v %cd%/allure-results:/app/allure-results sauce_test
```

3. Просмотр отчета:
После выполнения тестов папка `` `allure-results` `` появится в корне проекта

```bash
allure serve allure-results
```
