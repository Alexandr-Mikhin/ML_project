import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Загружаем модель
print("🔄 Загрузка модели...")
model = AutoModelForSequenceClassification.from_pretrained("./fake_detector_model")
tokenizer = AutoTokenizer.from_pretrained("./fake_detector_model")
model.eval()
print("✅ Модель загружена!")

def predict_review(text):
    if not text or text.strip() == "":
        return "⚠️ Пожалуйста, введите текст отзыва"
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        prob_fake = probs[0][1].item()
    
    if prob_fake > 0.5:
        return f"🔴 Вероятнее всего, это рекламный отзыв\n\nВероятность: {prob_fake:.2%}"
    else:
        return f"🟢 Вероятнее всего, это честный отзыв\n\nВероятность рекламы: {prob_fake:.2%}"

# Создаём интерфейс с кнопкой Submit
demo = gr.Interface(
    fn=predict_review,
    inputs=gr.Textbox(lines=5, placeholder="Введите текст отзыва здесь...", label="Текст отзыва"),
    outputs=gr.Textbox(label="Результат проверки"),
    title="Реклама vs Честный отзыв",
    description="Модель RuBERT обучена отличать настоящие отзывы от скрытой рекламы. Точность: 99.7%.",
    submit_btn="Проверить отзыв"
)

demo.launch()
