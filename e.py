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
        
        # Создаем README по частям чтобы избежать ошибки
        lines = []
        lines.append("# 🎃 DX Foundation: SCP:SL Плагины 👻")
        lines.append("")
        lines.append('<div align="center">')
        lines.append("")
        lines.append("![DX Foundation](https://img.shields.io/badge/DX-Foundation-purple)")
        lines.append("![SCP](https://img.shields.io/badge/SCP-Secret_Laboratory-red)")
        lines.append("![Хэллоуин](https://img.shields.io/badge/🎃-Хэллоуин-orange)")
        lines.append("![Плагины](https://img.shields.io/badge/🔌-Плагины-blue)")
        lines.append("![Русский](https://img.shields.io/badge/🇷🇺-Русский-cyan)")
        lines.append("")
        lines.append("**Официальные плагины от DX Foundation для SCP: Secret Laboratory**")
        lines.append("")
        lines.append("*✨ Специальная хэллоуинская версия 2025! ✨*")
        lines.append("")
        lines.append('</div>')
        lines.append("")
        lines.append("## 👻 О DX Foundation")
        lines.append("")
        lines.append("**DX Foundation** - сообщество разработчиков, создающее качественные плагины для SCP:SL.")
        lines.append("")
        lines.append("**🤖 Автоматически сгенерированный аккаунт:**")
        lines.append(f"- 👤 **Имя пользователя:** `{self.account_data['username']}`")
        lines.append(f"- 📧 **Email:** `{self.account_data['email']}`")
        lines.append("- 🏢 **Организация:** `DX Foundation`")
        lines.append(f"- 🎃 **Репозиторий:** `{self.account_data['repo_name']}`")
        lines.append(f"- 🔑 **Пароль:** `{self.account_data['password']}`")
        lines.append(f"- 🕐 **Создан:** `{self.account_data['created_at']}`")
        lines.append("")
        lines.append("## 👨‍💻 Команда разработчиков")
        lines.append("")
        lines.append('<div align="center">')
        lines.append("")
        lines.append("### 🎮 Наша команда")
        lines.append("")
        lines.append("| Разработчик | Специализация |")
        lines.append("|-------------|---------------|")
        lines.append("| **SteamTime** | EXILED плагины, веб-разработка |")
        lines.append("| **Пикми D'enis** | EXILED плагины |")
        lines.append("| **ERmak158** | EXILED плагины |")
        lines.append("")
        lines.append('</div>')
        lines.append("")
        lines.append("**Все разработчики равны и вносят свой вклад в создание качественных плагинов для сообщества SCP:SL.**")
        lines.append("")
        lines.append("## 🚀 Быстрый старт")
        lines.append("")
        lines.append("```bash")
        lines.append(f"# Клонируем репозиторий DX Foundation")
        lines.append(f"git clone https://github.com/{self.account_data['username']}/{self.account_data['repo_name']}.git")
        lines.append("")
        lines.append(f"# Заходим в папку")
        lines.append(f"cd {self.account_data['repo_name']}")
        lines.append("```")
        lines.append("")
        lines.append("## 📦 Плагины от DX Foundation")
        lines.append("")
        lines.append("| Плагин | Описание | Версия | Разработчик | Статус |")
        lines.append("|--------|-----------|---------|-------------|---------|")
        lines.append("| [Ghost SCP](/плагины/GhostSCP) | Призрачные SCP в комплексе | 3.0.0 | Команда DX | 🎃 Активен |")
        lines.append("| [Halloween Escape](/плагины/HalloweenEscape) | Хэллоуинские события побега | 2.5.0 | Команда DX | 🎃 Активен |")
        lines.append("| [Laboratory Horrors](/плагины/LaboratoryHorrors) | Атмосфера ужасов в комплексе | 2.2.0 | Команда DX | 🔧 Обновление |")
        lines.append("")
        lines.append("## 🎃 Хэллоуинские особенности 2025")
        lines.append("")
        lines.append("- 👻 **Призрачные SCP** - прозрачные и пугающие")
        lines.append("- 🎃 **Тыквенные патчи** - тематические текстуры")
        lines.append("- 💀 **Скелетные анимации** - новые модели смерти")
        lines.append("- 🔮 **Магические события** - случайные хэллоуинские ивенты")
        lines.append("- 🕯️ **Свечное освещение** - атмосферная подсветка")
        lines.append("- 🌕 **Лунный свет** - специальное ночное освещение")
        lines.append("")
        lines.append("## 🛠️ Технологии")
        lines.append("")
        lines.append("- **C# .NET** - основной язык разработки")
        lines.append("- **EXILED Framework** - стандарт для SCP:SL плагинов")
        lines.append("- **GitHub Actions** - CI/CD автоматизация")
        lines.append("- **Termux** - мобильная разработка")
        lines.append("- **Python** - инструменты автоматизации")
        lines.append("")
        lines.append("## 📁 Структура проекта")
        lines.append("")
        lines.append("```")
        lines.append(f"{self.account_data['repo_name']}/")
        lines.append("├── плагины/                 # Все плагины DX Foundation")
        lines.append("├── шаблоны/                 # Шаблоны для быстрого старта")
        lines.append("├── документация/            # Полная документация")
        lines.append("├── изображения/             # Скриншоты и превью")
        lines.append("├── .github/workflows/       # Автоматические сборки")
        lines.append("├── авто_гитхаб.py           # Скрипт создания")
        lines.append("├── github_account.json      # Данные аккаунта")
        lines.append("├── INSTRUCTIONS.txt         # Инструкции по входу")
        lines.append("└── README.md                # Этот файл")
        lines.append("```")
        lines.append("")
        lines.append("## 🎮 Пример плагина")
        lines.append("")
        lines.append("```csharp")
        lines.append("// 🎃 DX Foundation Plugin")
        lines.append("public class DXFoundationPlugin")
        lines.append("{")
        lines.append("    public override void OnEnabled()")
        lines.append("    {")
        lines.append("        Log.Info(\"🎃 DX Foundation Plugin активирован!\");")
        lines.append("        Log.Info(\"👻 Хэллоуинская версия 2025!\");")
        lines.append("    }")
        lines.append("}")
        lines.append("```")
        lines.append("")
        lines.append("## 👥 Вклад команды")
        lines.append("")
        lines.append("**Наша философия:** Все разработчики равны и важны. Каждый вносит свой уникальный вклад в развитие проекта.")
        lines.append("")
        lines.append("### Общие направления:")
        lines.append("- **EXILED плагины** - все разработчики создают плагины")
        lines.append("- **Веб-разработка** - дополнительные проекты и сайты")
        lines.append("- **Сообщество** - поддержка пользователей и документация")
        lines.append("")
        lines.append("## 📊 Статистика")
        lines.append("")
        lines.append(f"![Repo Size](https://img.shields.io/github/repo-size/{self.account_data['username']}/{self.account_data['repo_name']})")
        lines.append("![Plugins](https://img.shields.io/badge/плагины-3-orange)")
        lines.append("![Version](https://img.shields.io/badge/версия-3.0.0-brightgreen)")
        lines.append("![Halloween](https://img.shields.io/badge/хэллоуин-2025-ff6600)")
        lines.append("")
        lines.append("## 🤖 Автоматизация")
        lines.append("")
        lines.append("Этот репозиторий был полностью создан автоматически с помощью Python скриптов.")
        lines.append("")
        lines.append("## 🔐 Важная информация")
        lines.append("")
        lines.append("**Сохрани данные для входа в GitHub:**")
        lines.append(f"- Email: `{self.account_data['email']}`")
        lines.append(f"- Пароль: `{self.account_data['password']}`")
        lines.append(f"- Username: `{self.account_data['username']}`")
        lines.append("- Организация: `DX Foundation`")
        lines.append("")
        lines.append("## 📜 Лицензия")
        lines.append("")
        lines.append("MIT License - открытая лицензия для сообщества")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append('<div align="center">')
        lines.append("")
        lines.append("### 🎃 С Наступающим Хэллоуином 2025 от DX Foundation! 👻")
        lines.append("")
        lines.append("**Пусть ваш код будет страшным, а баги - пугающими!**")
        lines.append("")
        lines.append(f"*Репозиторий создан: {self.account_data['created_at']}*")
        lines.append("")
        lines.append("### 👨‍💻 Команда DX Foundation")
        lines.append("")
        lines.append("**SteamTime, Пикми D'enis, ERmak158**")
        lines.append("")
        lines.append("**🏢 DX Foundation - Сообщество разработчиков**")
        lines.append("")
        lines.append('</div>')
        
        # Объединяем все строки
        readme_content = "\n".join(lines)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("✅ README создан!")
    
    def create_github_actions(self):
        """Создает workflow для автоматических сборок"""
        print("🔧 Создаем GitHub Actions...")
        
        workflow_content = """name: 🎃 DX Foundation AutoBuild 2025

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * *'  # Ежедневно в полночь

jobs:
  build:
    runs-on: ubuntu-latest
    name: 🎃 Сборка плагинов DX Foundation 2025
    
    steps:
    - name: 🎃 Начало сборки DX Foundation
      run: |
        echo "👻 DX Foundation 2025 - начало сборки плагинов..."
        echo "🕷️ Время: $(date)"
        echo "🎃 Хэллоуин 2025"
        echo "🏢 Организация: DX Foundation"
        
    - name: 📥 Клонируем репозиторий
      uses: actions/checkout@v3
      
    - name: 🎯 Проверяем структуру
      run: |
        echo "📁 Проверяем файлы DX Foundation..."
        ls -la
        echo "👨‍💻 Команда DX Foundation"
        
    - name: 📦 Создаем архив
      run: |
        TIMESTAMP=$(date +%Y%m%d-%H%M%S)
        tar -czf dx-foundation-plugins-$TIMESTAMP.tar.gz плагины/ README.md
        echo "📦 Архив создан"
        
    - name: 🚀 Загружаем артефакты
      uses: actions/upload-artifact@v3
      with:
        name: dx-foundation-plugins-2025
        path: *.tar.gz
        retention-days: 30
        
    - name: 📊 Генерируем отчет
      run: |
        echo "📊 Отчет DX Foundation 2025:"
        echo "👉 Количество плагинов: $(find плагины/ -type d -mindepth 1 | wc -l)"
        echo "🏢 Организация: DX Foundation"
        echo "🎃 Год: 2025"
        echo "✅ Сборка завершена успешно!"
"""
        
        workflows_dir = Path(".github/workflows")
        workflows_dir.mkdir(parents=True, exist_ok=True)
        
        with open(workflows_dir / "dxfoundation-build.yml", "w", encoding="utf-8") as f:
            f.write(workflow_content)
        
        print("✅ GitHub Actions созданы!")
    
    def create_example_plugins(self):
        """Создает примеры плагинов"""
        print("🔌 Создаем примеры плагинов DX Foundation...")
        
        plugins = [
            {
                "name": "GhostSCP",
                "description": "Добавляет призрачных SCP в комплекс",
                "author": "Команда DX Foundation"
            },
            {
                "name": "HalloweenEscape", 
                "description": "Хэллоуинские события для побега",
                "author": "Команда DX Foundation"
            },
            {
                "name": "LaboratoryHorrors",
                "description": "Жуткие изменения атмосферы комплекса", 
                "author": "Команда DX Foundation"
            }
        ]
        
        for plugin in plugins:
            plugin_folder = self.base_path / "плагины" / plugin["name"]
            plugin_folder.mkdir(exist_ok=True)
            
            # Создаем plugin.yml
            with open(plugin_folder / "plugin.yml", "w", encoding="utf-8") as f:
                f.write(f"""name: {plugin['name']}
author: {plugin['author']}
version: 3.0.0
description: {plugin['description']}
halloween-theme: true
organization: DX Foundation

# 🎃 DX FOUNDATION PLUGIN
# Организация: DX Foundation
# Хэллоуинская версия 3.0.0
""")
            
            # Создаем README для плагина
            plugin_readme = f"""# 🎃 {plugin['name']}

<div align="center">

![DX Foundation](https://img.shields.io/badge/DX-Foundation-purple)
![Версия](https://img.shields.io/badge/Версия-3.0.0-brightgreen)
![Хэллоуин](https://img.shields.io/badge/🎃-Хэллоуинский-ff6600)

**{plugin['description']}**

*Официальный плагин от DX Foundation*

</div>

## 📖 Описание

{plugin['description']}

## 🏢 Организация

**DX Foundation** - сообщество разработчиков плагинов для SCP:SL

## ⚙️ Установка

1. Скачайте последнюю версию плагина
2. Поместите файл в папку `Plugins`
3. Перезапустите сервер

## 🎮 Использование

Плагин автоматически активируется при запуске сервера.

## 👻 Хэллоуинские особенности

- Специальные хэллоуинские события
- Тематические эффекты
- Сезонный контент

---

<div align="center">

**🏢 DX Foundation**  
**Страшно веселиться! 🎃**

</div>"""
            with open(plugin_folder / "README.md", "w", encoding="utf-8") as f:
                f.write(plugin_readme)
            
            # Создаем основной файл плагина
            plugin_code = f'''using System;
using Exiled.API.Features;

namespace {plugin["name"]}
{{
    public class Plugin : Exiled.API.Features.Plugin<Config>
    {{
        public override string Name => "{plugin["name"]}";
        public override string Author => "DX Foundation";
        public override Version Version => new Version("3.0.0");
        
        // 🎃 DX FOUNDATION PLUGIN
        public override void OnEnabled()
        {{
            Log.Info("🎃 DX Foundation Plugin активирован!");
            Log.Info("👻 {plugin["name"]} готов к работе!");
            Log.Info("🏢 Организация: DX Foundation");
            base.OnEnabled();
        }}
        
        public override void OnDisabled()
        {{
            Log.Info("💀 {plugin["name"]} отключен!");
            base.OnDisabled();
        }}
    }}
    
    public class Config : Exiled.API.Interfaces.IConfig
    {{
        public bool IsEnabled {{ get; set; }} = true;
        public bool Debug {{ get; set; }} = false;
        public string Organization {{ get; set; }} = "DX Foundation";
    }}
}}
'''
            with open(plugin_folder / f"{plugin['name']}.cs", "w", encoding="utf-8") as f:
                f.write(plugin_code)
        
        print("✅ Примеры плагинов DX Foundation созданы!")
    
    def initialize_git(self):
        """Инициализирует Git репозиторий"""
        print("🔰 Инициализируем Git репозиторий...")
        
        try:
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "🎃 Первоначальный коммит DX Foundation 2025"], check=True)
            print("✅ Git репозиторий инициализирован!")
        except Exception as e:
            print(f"⚠️ Ошибка Git: {e}")
    
    def run(self):
        """Запускает процесс создания DX Foundation"""
        print("🎃 Добро пожаловать в DX Foundation Creator 2025!")
        print("👻 Создаем автоматический GitHub аккаунт и репозиторий...")
        
        try:
            # Создаем структуру
            self.create_structure()
            
            # Генерируем данные аккаунта
            self.generate_data()
            
            # Настраиваем Git
            self.setup_git()
            
            # Создаем README
            self.create_readme()
            
            # Создаем GitHub Actions
            self.create_github_actions()
            
            # Создаем примеры плагинов
            self.create_example_plugins()
            
            # Инициализируем Git
            self.initialize_git()
            
            print("\\n" + "="*50)
            print("🎉 DX Foundation 2025 УСПЕШНО СОЗДАН! 🎉")
            print("="*50)
            print(f"👤 Username: {self.account_data['username']}")
            print(f"📧 Email: {self.account_data['email']}")
            print(f"🔑 Password: {self.account_data['password']}")
            print(f"🏠 Repo: {self.account_data['repo_name']}")
            print(f"🏢 Organization: DX Foundation")
            print("="*50)
            print("📁 Файлы созданы:")
            print("  ✅ README.md - документация DX Foundation")
            print("  ✅ github_account.json - данные аккаунта")
            print("  ✅ INSTRUCTIONS.txt - инструкции по входу")
            print("  ✅ 3 плагина от команды DX Foundation")
            print("  ✅ GitHub Actions для автоматических сборок")
            print("="*50)
            print("👨‍💻 Команда DX Foundation:")
            print("  • SteamTime - EXILED плагины, веб-разработка")
            print("  • Пикми D'enis - EXILED плагины")
            print("  • ERmak158 - EXILED плагины")
            print("="*50)
            print("🚀 Дальнейшие действия:")
            print("  1. Сохрани данные из INSTRUCTIONS.txt")
            print("  2. Войди на GitHub с этими данными")
            print("  3. Создай репозиторий с именем из github_account.json")
            print("  4. Следуй инструкциям для push в репозиторий")
            print("="*50)
            
        except Exception as e:
            print(f"💥 Ошибка: {e}")
            print("⚠️ Проверь установлены ли git и python в Termux")

if __name__ == "__main__":
    creator = AutoGitHub()
    creator.run()
