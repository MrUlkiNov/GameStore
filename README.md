# 🎮 GameStore — Интернет-магазин видеоигр на Django

[![Django](https://img.shields.io/badge/Django-5.1.7-44B78B?logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

**Онлайн-платформа для продажи цифровых игр с корзиной, списком желаний и аутентификацией пользователей.**

---

## ✨ Основные функции
- 🕹️ Каталог игр с фильтрацией и поиском
- 🛒 Сессионная корзина покупок
- ❤️ Список желаний (Wishlist)
- 🔐 Регистрация/авторизация пользователей
- 📦 Панель администратора Django
- 📱 Адаптивный интерфейс (Bootstrap 5)
- 🖼️ Загрузка изображений через админку

---

## 🛠 Технологии
| Категория       | Стек                          |
|-----------------|-------------------------------|
| **Backend**     | Django 5.1.7                  |
| **Frontend**    | Bootstrap 5, Crispy Forms     |
| **База данных** | SQLite (dev), PostgreSQL (prod) |
| **Дополнительно**| Pillow, python-dotenv       |

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/ваш-логин/game_store.git
cd game_store
###2. Настройка виртуального окружения
bash
python -m venv venv

# Активация:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
3. Установка зависимостей
bash
pip install -r requirements.txt
4. Создание .env файла
Создайте .env в корне проекта:

ini
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
5. Применение миграций
bash
python manage.py migrate
6. Создание суперпользователя
bash
python manage.py createsuperuser
7. Запуск сервера
bash
python manage.py runserver
Перейдите по адресу: http://localhost:8000

📂 Структура проекта
game_store/
├── store/               # Основное приложение
│   ├── migrations/      # Миграции БД
│   ├── templates/       # HTML-шаблоны
│   └── context_processors.py # Контекст-процессоры
├── game_store/          # Настройки проекта
├── static/              # CSS, JS, изображения
├── media/               # Загруженные файлы
├── .env.example         # Шаблон настроек
└── requirements.txt     # Зависимости
⚙️ Конфигурация
Настройки Crispy Forms
python
# settings.py
CRISPY_TEMPLATE_PACK = 'bootstrap5'
Работа с медиафайлами
python
# urls.py (добавить в конец)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
📸 Скриншоты
Главная страница	Админ-панель
<img src="screenshots/main.png" width="400">	<img src="screenshots/admin.png" width="400">
🔧 Частые проблемы
Ошибка активации venv в PowerShell
bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
ModuleNotFoundError: No module named 'crispy_forms'
bash
pip install django-crispy-forms==2.4
Нет доступа к медиафайлам
Убедитесь, что в urls.py добавлена строка:

python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
📄 Лицензия
Проект распространяется под лицензией MIT.

Разработано: [Ваше Имя]
📧 Контакты: [ваш.email@example.com]
💻 GitHub: github.com/ваш-логин
