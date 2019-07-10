Создание проекта + Github:

1. Создание репозитория на github.com
2. Клонирование репозитория в папку (/PycharmProjects/...) через GitHub Desktop
3. Создание PyCharm проекта в папке (/PycharmProjects/...)
4. Создание виртуального окружения
5. Добавление .gitignore
6. Git Push из под PyCharm

Создание Django:

1. django-admin.py startproject djangoshop - Разворачивание папки проекта (вводить в виртуальном окружении)
2. python manage.py runserver - Запустить проект Django (можно настроить запуск по кнопке PyCharm)
3. python manage.py migrate - Решить ошибку об миграциях (Добавить миграции)
4. python manage.py createsuperuser - Создать суперпользователя
5. Создание приложения "app" в среде Django:
    - python manage.py startapp app (Пишем в консоли)
    - Добавляем "app" в "setting.py" в раздел "INSTALLED_APPS"
6. python manage.py collectstatic - для подключения bootstrap в Django