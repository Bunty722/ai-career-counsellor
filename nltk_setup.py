import nltk

# This forces download of 'punkt' into your custom nltk_data path
nltk.download('punkt', download_dir=r"C:\D\E\rasa-bot\ai-career-counsellor\nltk_data")

# Optional sanity check: confirm path
print("Punkt downloaded to:", r"C:\D\E\rasa-bot\ai-career-counsellor\nltk_data")
