# Packets Visualizer

## Описание

Packets Visualizer — это инструмент командной строки, который позволяет визуализировать граф зависимостей пакетов Python. Он анализирует указанный пакет и его транзитивные зависимости, генерируя код в формате PlantUML, который можно использовать для создания графических представлений зависимостей.

## Особенности

- Анализирует зависимости пакетов Python без использования сторонних библиотек.
- Генерирует код PlantUML для визуализации зависимостей.
- Поддерживает транзитивные зависимости.
- Включает тесты для проверки функциональности.

## Установка

Для работы с проектом вам потребуется Python 3.6 или выше. Убедитесь, что у вас установлен `pip`.

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/dependency-visualizer.git
   cd dependency-visualizer
   ```

Установите необходимые зависимости (если есть):

```bash
pip install -r requirements.txt
```

# Пример Использование

Для запуска инструмента используйте следующую команду:

```bash
python dependency_visualizer.py <output_path> <package_name>
<output_path>: Путь к файлу, в который будет записан сгенерированный код PlantUML.
<package_name>: Имя пакета, для которого вы хотите визуализировать зависимости.

# Пример

python dependency_visualizer.py output.puml requests

# Этот пример создаст файл output.puml, содержащий граф зависимостей для пакета requests.
```

## Результат
<img width="349" alt="image" src="https://github.com/user-attachments/assets/8b0b7b8e-cff2-4ff7-8d75-b642cdc420b2" />

## Генерация графа

Сгенерированный файл PlantUML можно визуализировать с помощью любого инструмента, поддерживающего PlantUML, например, PlantUML Online Server.

## Тестирование

### Пример Использования

```python
    def test_get_dependencies(self, mock_stdout):
        dependencies = get_dependencies('requests')
        self.assertIn('urllib3', dependencies)

    def test_generate_plantuml(self):
        dependencies = {'urllib3', 'chardet'}
        plantuml_code = generate_plantuml('requests', dependencies)
        self.assertIn('package "requests"', plantuml_code)
        self.assertIn('[ urllib3 ]', plantuml_code)
        self.assertIn('[ requests ] --> [ urllib3 ]', plantuml_code)
```

### Результат Тестов

<img width="435" alt="image" src="https://github.com/user-attachments/assets/9e41328b-3019-4788-ad05-4affcc3ff0cd">


Проект включает тесты для проверки функциональности. Для запуска тестов используйте следующую команду:

```bash
python -m unittest test_dependency_visualizer.py
```

### Структура проекта

packets-visualizer/
│
├── packets_visualizer.py  # Основной код визуализатора
├── tests.py  # Тесты для визуализатора
├── requirements.txt  # Зависимости проекта (если есть)
└── README.md  # Этот файл
