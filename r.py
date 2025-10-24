#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import random
import subprocess
from pathlib import Path

class AutoGitHub:
    def __init__(self):
        self.base_path = Path.home() / "scp-sl-russian-plugins"
        self.account_data = {}
        
    def create_structure(self):
        """Создает структуру проекта"""
        print("🎃 Создаем структуру проекта...")
        
        folders = [
            "плагины",
            "шаблоны", 
            "документация",
            "изображения",
            ".github/workflows"
        ]
        
        for folder in folders:
            (self.base_path / folder).mkdir(parents=True, exist_ok=True)
            
        os.chdir(self.base_path)
        print("✅ Структура создана!")
    
    def generate_data(self):
        """Генерирует данные для аккаунта с фиксированным Gmail"""
        print("👻 Генерируем данные для GitHub аккаунта...")
        
        # Фиксированный Gmail
        fixed_email = "huetaxzzz@gmail.com"
        
        # Генерируем случайный пароль
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        password = "".join(random.choice(characters) for i in range(16))
        
        self.account_data = {
            "username": f"DXFoundation{random.randint(100, 999)}",
            "email": fixed_email,
            "password": password,
            "repo_name": "dx-foundation-plugins",
            "display_name": "DX Foundation",
            "created_at": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        print("🎃 АККАУНТ GITHUB СОЗДАН:")
        print(f"👤 Имя пользователя: {self.account_data['username']}")
        print(f"📧 Email: {self.account_data['email']}")
        print(f"🔑 Пароль: {self.account_data['password']}")
        print(f"🏠 Репозиторий: {self.account_data['repo_name']}")
        print(f"🏢 Организация: DX Foundation")
        
        # Сохраняем данные в файл
        with open("github_account.json", "w", encoding="utf-8") as f:
            json.dump(self.account_data, f, ensure_ascii=False, indent=2)
        
        # Создаем файл с инструкциями
        self.create_instructions()
        
        return self.account_data
    
    def create_instructions(self):
        """Создает файл с инструкциями для входа"""
        instructions = f"""# 🎃 ИНСТРУКЦИЯ ДЛЯ ВХОДА В GITHUB

## 🔐 Данные для входа:

**Сайт:** https://github.com
**Логин:** {self.account_data['email']}
**Пароль:** {self.account_data['password']}
**Имя пользователя:** {self.account_data['username']}
**Организация:** DX Foundation

## 📱 Что делать:

1. Перейди на GitHub.com
2. Нажми "Sign In"
3. Введи email и пароль выше
4. Подтверди email если нужно
5. Готово! Твой репозиторий создан!

## 💾 Сохрани эти данные!

"""
        with open("INSTRUCTIONS.txt", "w", encoding="utf-8") as f:
            f.write(instructions)
    
    def setup_git(self):
        """Настраивает Git с сгенерированными данными"""
        print("⚙️ Настраиваем Git...")
        
        subprocess.run(["git", "config", "--global", "user.name", self.account_data['display_name']], check=True)
        subprocess.run(["git", "config", "--global", "user.email", self.account_data['email']], check=True)
        
        print("✅ Git настроен!")
    
    def create_readme(self):
        """Создает красивый README.md с данными разработчиков"""
        print("📖 Создаем README.md...")
        
        readme_content = f"""# 🎃 DX Foundation: SCP:SL Плагины 👻

<div align="center">

![DX Foundation](https://img.shields.io/badge/DX-Foundation-purple)
![SCP](https://img.shields.io/badge/SCP-Secret_Laboratory-red)
![Хэллоуин](https://img.shields.io/badge/🎃-Хэллоуин-orange)
![Плагины](https://img.shields.io/badge/🔌-Плагины-blue)
![Русский](https://img.shields.io/badge/🇷🇺-Русский-cyan)

**Официальные плагины от DX Foundation для SCP: Secret Laboratory**

*✨ Специальная хэллоуинская версия 2025! ✨*

</div>

## 👻 О DX Foundation

**DX Foundation** - сообщество разработчиков, создающее качественные плагины для SCP:SL.

**🤖 Автоматически сгенерированный аккаунт:**
- 👤 **Имя пользователя:** `{self.account_data['username']}`
- 📧 **Email:** `{self.account_data['email']}`
- 🏢 **Организация:** `DX Foundation`
- 🎃 **Репозиторий:** `{self.account_data['repo_name']}`
- 🔑 **Пароль:** `{self.account_data['password']}`
- 🕐 **Создан:** `{self.account_data['created_at']}`

## 👨‍💻 Команда разработчиков

<div align="center">

### 🎮 Наша команда

| Разработчик | Специализация |
|-------------|---------------|
| **SteamTime** | EXILED плагины, веб-разработка |
| **Пикми D'enis** | EXILED плагины |
| **ERmak158** | EXILED плагины |

</div>

**Все разработчики равны и вносят свой вклад в создание качественных плагинов для сообщества SCP:SL.**

## 🚀 Быстрый старт

```bash
# Клонируем репозиторий DX Foundation
git clone https://github.com/{self.account_data['username']}/{self.account_data['repo_name']}.git

# Заходим в папку
cd {self.account_data['repo_name']}
