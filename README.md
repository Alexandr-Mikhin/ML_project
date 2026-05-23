# Реклама vs Честный отзыв

Детектор рекламных отзывов на основе модели RuBERT.  
Определяет, является ли отзыв рекламой или честным мнением.  
**Точность модели: 99.7%**

---

## Готовый сайт

Модель развёрнута на Hugging Face Spaces:

**[https://huggingface.co/spaces/AlexandrMikhin/fake-review-detector](https://huggingface.co/spaces/AlexandrMikhin/fake-review-detector)**

---

## Исходные данные

Датасет с отзывами взят с Kaggle:

**[Yandex Geo Reviews Dataset 2023](https://www.kaggle.com/datasets/kyakovlev/yandex-geo-reviews-dataset-2023)**

---

##Как развернуть проект с нуля

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Alexandr-Mikhin/ML_project.git
cd ML_project
```
### 2. Создать виртуальное окружение
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Mac / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Установить зависимости
```bash
pip install -r requirements.txt
```
### 4. Подготовить данные
Золотой стандарт (размеченные отзывы) лежит в папке Датасеты.
### 5. Обучить модель
```bash
jupyter notebook Блокноты/ML_project_Итог.ipynb
```
Ноутбук содержит:

- Загрузку данных

- Обучение RuBERT

- Оценку качества модели

После обучения модель сохранится в папку fake_detector_model

### 6. Запустить веб-сервис локально
```bash
python app.py
```

---
## Результаты модели

| Метрика | Значение |
|---------|----------|
| Accuracy | 99.67% |
| F1-score | 99.81% |
| Precision | 99.62% |
| Recall | 100.00% |

---

## Пример работы

**Входной текст:**  
> Супер заведение, супер вкусно! Официант Андрей Андреевич - просто бомба! Были в пятницу вечером.

**Ответ модели:**  
🟢 Вероятнее всего, это честный отзыв. Вероятность рекламы: 8.62%
## 📝 Зависимости
Основные библиотеки:

- gradio — веб-интерфейс

- transformers — RuBERT модель

- torch — глубокое обучение

- pandas — работа с данными

- scikit-learn — метрики

- openpyxl — работа с Excel файлами

Полный список в requirements.txt

