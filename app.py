import gradio as gr
from transformers import pipeline
import json

pipe = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

with open("rubric.json", "r") as f:
    rubric = json.load(f)

def analyze(text):
    pred = pipe(text)[0]
    tone = pred['label'].lower()
    score = round(pred['score'], 2)
    feedback = rubric.get(tone, "General tone – OK")
    return f"Tone: {tone} ({score})\nFeedback: {feedback}"

gr.Interface(fn=analyze, inputs="text", outputs="text", title="ToneAdapt: AI Tone Evaluator").launch()
