import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR = os.path.join(ROOT_DIR, 'mock_data/logs')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'processed_data/parsed_logs')
os.makedirs(OUTPUT_DIR, exist_ok=True)


for file in os.listdir(SOURCE_DIR):
    if file.endswith('.log'):
        try:
            with open(os.path.join(SOURCE_DIR, file), 'r') as f:
                lines = f.readlines()

            chunks = [lines[i:i+30] for i in range(0, len(lines), 30)]

            for idx, chunk in enumerate(chunks):
                chunk_path = os.path.join(
                    OUTPUT_DIR, f"{file}_{idx}.txt")
                with open(chunk_path, 'w') as out_f:
                    out_f.writelines(chunk)
        except Exception as e:
            print(f"Error while processing {file}: {str(e)}")
