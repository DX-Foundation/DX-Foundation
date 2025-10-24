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
        """Генерирует случайные данные для аккаунта"""
        print("👻 Генерируем данные для GitHub аккаунта...")
        
        имена = ["ShadowCoder", "GhostDeveloper", "PumpkinProgrammer", "SpookyCoder", "HalloweenDev"]
        домены = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com"]
        
        self.данные_аккаунта = {
            "username": f"{random.choice(имена)}{random.randint(100, 999)}",
            "email": f"scp.dev{random.randint(1000, 9999)}@{random.choice(домены)}",
            "password": f"ScpSecretLab{random.randint(10000, 99999)}!",
            "repo_name": "scp-sl-halloween-plugins",
            "display_name": "SCP Halloween Developer"
        }
        
        print(f"👤 Имя пользователя: {self.данные_аккаунта['username']}")
        print(f"📧 Email: {self.данные_аккаунта['email']}")
        print(f"🔑 Пароль: {self.данные_аккаунта['password']}")
        
        # Сохраняем данные в файл
        with open("github_account.json", "w", encoding="utf-8") as f:
            json.dump(self.данные_аккаунта, f, ensure_ascii=False, indent=2)
        
        return self.данные_аккаунта
    
    def настроить_git(self):
        """Настраивает Git с сгенерированными данными"""
        print("⚙️ Настраиваем Git...")
        
        subprocess.run(["git", "config", "--global", "user.name", self.данные_аккаунта['display_name']], check=True)
        subprocess.run(["git", "config", "--global", "user.email", self.данные_аккаунта['email']], check=True)
        
        print("✅ Git настроен!")
    
    def создать_readme(self):
        """Создает красивый README.md"""
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

**Автоматически сгенерированный аккаунт:**
- 👤 **Имя пользователя:** `{self.данные_аккаунта['username']}`
- 📧 **Email:** `{self.данные_аккаунта['email']}`
- 🎃 **Репозиторий:** `{self.данные_аккаунта['repo_name']}`

## 🚀 Быстрый старт

```bash
# Клонируем репозиторий
git clone https://github.com/{self.данные_аккаунта['username']}/{self.данные_аккаунта['repo_name']}.git

# Заходим в папку
cd {self.данные_аккаунта['repo_name']}
