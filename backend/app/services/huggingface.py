from transformers import pipeline

# Lazy-load models (important for performance)
_sentiment = None
_zero_shot = None

def get_sentiment_pipeline():
    global _sentiment
    if _sentiment is None:
        _sentiment = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    return _sentiment

def get_zero_shot_pipeline():
    global _zero_shot
    if _zero_shot is None:
        _zero_shot = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
    return _zero_shot
