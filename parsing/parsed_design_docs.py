import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR = os.path.join(ROOT_DIR, 'mock_data/internal_docs/design_docs')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'processed_data/parsed_design_docs')
os.makedirs(OUTPUT_DIR, exist_ok=True)


for file in os.listdir(SOURCE_DIR):
    if file.endswith('.md'):
        try:
            with open(os.path.join(SOURCE_DIR, file), 'r') as f:
                text = f.read()

            lines = text.split('\n')
            chunks = [lines[i:i+50] for i in range(0, len(lines), 50)]

            for idx, chunk in enumerate(chunks):
                chunk_path = os.path.join(
                    OUTPUT_DIR, f"{file}_{idx}.txt")
                with open(chunk_path, 'w') as out_f:
                    out_f.write('\n'.join(chunk))
        except Exception as e:
            print(f"Error while processing {file}: {str(e)}")
