from transformers import pipeline
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get the model name from the environment variable
model_name = os.getenv("MODEL_NAME", "facebook/bart-large-cnn")
summarizer = pipeline("summarization", model=model_name)


# Ensure the model is downloaded and cached
if not os.path.exists("facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn") # This line ensures the model is downloaded and cached
# Function to summarize text                

def summarize_text(text: str) -> str:
    if len(text.split()) < 30:
        return "Text too short to summarize."
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']