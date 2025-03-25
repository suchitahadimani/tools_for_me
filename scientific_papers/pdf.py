import fitz  # PyMuPDF
import re
import nltk
from nltk.tokenize import sent_tokenize

# Ensure NLTK sentence tokenizer is available
nltk.download('punkt_tab')

# Define keywords for different categories
KEYWORDS = {
    "problem": ["problem", "challenge", "issue", "gap", "lack", "address"],
    "implementation": ["method", "approach", "we propose", "technique"],
    "results": ["result", "improvement", "increase", "decrease", "achieve", "%"],
    "conclusion": ["conclusion", "summary", "in summary", "we conclude"],
    "limitations": ["limitation", "shortcoming", "drawback", "constraint"],
    "future_work": ["future work", "extension", "further research", "improve"]
}

def is_important_sentence(sentence):
    sentence_lower = sentence.lower()
    for category, words in KEYWORDS.items():
        if any(word in sentence_lower for word in words):
            return True
    return False

def highlight_important_sentences(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    
    for page in doc:
        text = page.get_text("text")
        sentences = sent_tokenize(text)
        
        for sentence in sentences:
            if is_important_sentence(sentence):
                text_instances = page.search_for(sentence)
                for inst in text_instances:
                    page.add_highlight_annot(inst)
    
    doc.save(output_path)
    print(f"Highlighted PDF saved as {output_path}")

# Example usage

highlight_important_sentences("input.pdf", "output.pdf")

print("hi")