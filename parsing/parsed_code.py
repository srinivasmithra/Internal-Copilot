import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR = os.path.join(ROOT_DIR, 'mock_data/code_repos')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'processed_data/parsed_code')
os.makedirs(OUTPUT_DIR, exist_ok=True)

for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.endswith(('.cpp', '.h', '.c', '.py')):
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    code = f.read()

                # For now, very simple chunking (1 chunk = 200 lines max)
                lines = code.split('\n')
                chunks = [lines[i:i+200] for i in range(0, len(lines), 200)]

                for idx, chunk in enumerate(chunks):
                    chunk_path = os.path.join(
                        OUTPUT_DIR, f"{file}_{idx}.txt")
                    with open(chunk_path, 'w') as out_f:
                        out_f.write('\n'.join(chunk))
            except Exception as e:
                print(f"Error while processing {file}: {str(e)}")
