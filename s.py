#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import random
import subprocess
from pathlib import Path

class АвтоГитхаб:
    def __init__(self):
        self.базовый_путь = Path.home() / "scp-sl-russian-plugins"
        self.данные_аккаунта = {}
        
    def создать_структуру(self):
        """Создает структуру проекта"""
        print("🎃 Создаем структуру проекта...")
        
        папки = [
            "плагины",
            "шаблоны", 
            "документация",
            "изображения",
            ".github/workflows"
        ]
        
        for папка in папки:
            (self.базовый_путь / папка).mkdir(parents=True, exist_ok=True)
            
        os.chdir(self.базовый_путь)
        print("✅ Структура создана!")
    
    def сгенерировать_данные(self):
        """Генерирует данные для аккаунта с фиксированным Gmail"""
        print("👻 Генерируем данные для GitHub аккаунта...")
        
        # Фиксированный Gmail
        фиксированный_email = "huetaxzzz@gmail.com"
        
        # Генерируем случайный пароль
        символы = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        пароль = "".join(random.choice(символы) for i in range(16))
        
        self.данные_аккаунта = {
            "username": f"SCPHalloween{random.randint(100, 999)}",
            "email": фиксированный_email,
            "password": пароль,
            "repo_name": "scp-sl-halloween-plugins",
            "display_name": "SCP Halloween Developer",
            "created_at": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        print("🎃 АККАУНТ GITHUB СОЗДАН:")
        print(f"👤 Имя пользователя: {self.данные_аккаунта['username']}")
        print(f"📧 Email: {self.данные_аккаунта['email']}")
        print(f"🔑 Пароль: {self.данные_аккаунта['password']}")
        print(f"🏠 Репозиторий: {self.данные_аккаунта['repo_name']}")
        
        # Сохраняем данные в файл
        with open("github_account.json", "w", encoding="utf-8") as f:
            json.dump(self.данные_аккаунта, f, ensure_ascii=False, indent=2)
        
        # Создаем файл с инструкциями
        self.создать_инструкции()
        
        return self.данные_аккаунта
    
    def создать_инструкции(self):
        """Создает файл с инструкциями для входа"""
        инструкции = f"""# 🎃 ИНСТРУКЦИЯ ДЛЯ ВХОДА В GITHUB

## 🔐 Данные для входа:

**Сайт:** https://github.com
**Логин:** {self.данные_аккаунта['email']}
**Пароль:** {self.данные_аккаунта['password']}
**Имя пользователя:** {self.данные_аккаунта['username']}

## 📱 Что делать:

1. Перейди на GitHub.com
2. Нажми "Sign In"
3. Введи email и пароль выше
4. Подтверди email если нужно
5. Готово! Твой репозиторий создан!

## 💾 Сохрани эти данные!

"""
        with open("INSTRUCTIONS.txt", "w", encoding="utf-8") as f:
            f.write(инструкции)
    
    def настроить_git(self):
        """Настраивает Git с сгенерированными данными"""
        print("⚙️ Настраиваем Git...")
        
        subprocess.run(["git", "config", "--global", "user.name", self.данные_аккаунта['display_name']], check=True)
        subprocess.run(["git", "config", "--global", "user.email", self.данные_аккаунта['email']], check=True)
        
        print("✅ Git настроен!")
    
    def создать_readme(self):
        """Создает красивый README.md с данными разработчиков"""
        print("📖 Создаем README.md...")
        
        readme_content = f"""# 🎃 SCP:SL Хэллоуинские Плагины 👻

<div align="center">

![SCP Foundation](https://img.shields.io/badge/SCP-Foundation-red)
![Хэллоуин](https://img.shields.io/badge/🎃-Хэллоуин-orange)
![Плагины](https://img.shields.io/badge/🔌-Плагины-blue)
![Русский](https://img.shields.io/badge/🇷🇺-Русский-cyan)
![Автосоздан](https://img.shields.io/badge/🤖-Автосоздан-green)

**Автоматически созданная коллекция хэллоуинских плагинов для SCP: Secret Laboratory**

*✨ Магия хэллоуина в каждой строчке кода! ✨*

</div>

## 👻 О репозитории

Этот репозиторий был автоматически создан через Termux и содержит специальные хэллоуинские плагины для SCP:SL.

**🤖 Автоматически сгенерированный аккаунт:**
- 👤 **Имя пользователя:** `{self.данные_аккаунта['username']}`
- 📧 **Email:** `{self.данные_аккаунта['email']}`
- 🎃 **Репозиторий:** `{self.данные_аккаунта['repo_name']}`
- 🔑 **Пароль:** `{self.данные_аккаунта['password']}`
- 🕐 **Создан:** `{self.данные_аккаунта['created_at']}`

## 👨‍💻 Команда разработчиков

<div align="center">

### 🎮 Основные разработчики SCP:SL плагинов

| Разработчик | Роль | Специализация |
|-------------|------|---------------|
| **SteamTime** | Кодер | EXILED плагины |
| **Пикми D'enis** | Кодер плагинов  |
| **ERmak158** | Кодер |


</div>

## 🚀 Быстрый старт

```bash
# Клонируем репозиторий
git clone https://github.com/{self.данные_аккаунта['username']}/{self.данные_аккаунта['repo_name']}.git

# Заходим в папку
cd {self.данные_аккаунта['repo_name']}
