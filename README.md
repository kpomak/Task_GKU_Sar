# Task_GKU_Sar

## Для запуска проекта создайте файл `.env` в папке app/

```bash
cp app/.env.example app/.env
```

## Сохраните в нем свой токен для API openweathermap.com

## Создайте, активируйте виртуальное окружение и установите зависимости

```bash
poetry install
poetry shell
```

## Запустите скрипт

```bash
python script.py
```

## Прогнозы погоды на трое суток сохранятся в папке forecasts/