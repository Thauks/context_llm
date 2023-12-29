from src.file_handling import FileHandler
from src.llm_interface import ChatGPTInterface
from dotenv import load_dotenv
import os

def main():
    processor = FileHandler()
    inputs = processor.read_input_files()
    print(inputs)
    
    gptif = ChatGPTInterface(os.getenv("OPENAI_API_KEY"))
    res = gptif.generate_response(inputs)
    print(res)

if __name__ == "__main__":
    load_dotenv()
    main()