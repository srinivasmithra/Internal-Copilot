import os
import fitz


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR = os.path.join(ROOT_DIR, 'mock_data/sdk_docs')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'processed_data/parsed_sdk_docs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(SOURCE_DIR):
    if file.endswith('.pdf'):
        try:
            pdf = fitz.open(os.path.join(SOURCE_DIR, file))
            text = ""
            for page in pdf:
                text += page.get_text()

            # Simple chunking by words (1 chunk = 1000 words)
            words = text.split()
            chunks = [' '.join(words[i:i+1000])
                      for i in range(0, len(words), 1000)]

            for idx, chunk in enumerate(chunks):
                chunk_path = os.path.join(
                    OUTPUT_DIR, f"{file}_{idx}.txt")
                with open(chunk_path, 'w') as out_f:
                    out_f.write(chunk)
        except Exception as e:
            print(f"Error while processing {file}: {str(e)}")
