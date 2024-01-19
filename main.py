from src.file_handling import FileHandler
from src.llm_interface import ChatGPTInterface
from dotenv import load_dotenv
import os, json

def main():
    processor = FileHandler()
    inputs = processor.read_input_files()
    print(inputs)
    
    gptif = ChatGPTInterface(os.getenv("OPENAI_API_KEY"))
    res = gptif.generate_response(inputs)
    
    json_obj = json.dumps(res.to_json(), indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_obj)

if __name__ == "__main__":
    load_dotenv()
    main()