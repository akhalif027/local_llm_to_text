from langchain_ollama.llms import OllamaLLM
from datetime import datetime
import os 
import textwrap 
import re 

model = OllamaLLM(model="llama3.2")
spacing = '-' * 30
custom_filename = input('Enter a name: (press Enter to use default name) ').strip()
filename = custom_filename if custom_filename else 'llm_reponses.txt'


def get_next_index(filename):
    if not os.path.exists(filename):
        return 1 
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    matches = re.findall(r'^\d+\)', content, re.MULTILINE)
    return len(matches) + 1


def saving_response(question: str, response: str, filename: str = filename):
     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     index = get_next_index(filename)
     formatted_text = f'{index}) \n Timestamp: {timestamp} \n Question: {question} \n Response: {response}\n \n'
    
     with open(filename, 'a', encoding='utf-8') as f:
         f.write(formatted_text)
         print('Data successfully recorded!')
    

while True:
    print(spacing)
    question = input("Enter your question: (Press q to quit) ")

    if question.lower() == 'q':
        break

    if question.lower() == 'clear':
        confirm = input("Are you sure you want to delete the file and lose all saved responses? (y/n)")
        if confirm.lower() == 'y' and os.path.exists(filename):
            os.remove(filename)
            print('File deleted.')
        continue
        
    try:
        response = model.invoke(question)
        print(textwrap.fill(response, width=120) + '\n')

        print('Saving responses...')
        saving_response(question=question, response=response)

    except Exception as e:
        print(f'An error has occurred: {e}')


