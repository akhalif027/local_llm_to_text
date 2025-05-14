## Let's be honest here...

We all have burning questions just ready to be inquired but asking someone in real-life would be too embarrasing and googling them would give
underwhelming results. Asking a large language model (llm) is a great method of testing the waters but no one wants their sensitive data to be hosted along
with their full name, phone number, email, and location.

Enter local_llm_to_text: A program that uses any llm of your choice to query confidental questions and save their answers locally on your 
computer. So you won't have to choose between your burning questions and your honour. 

## Getting Started: Downloading Dependacies

First, you will need to download a few items to truly own a secure, private feedback loop. 

1. Ollama: A framework to download and host AI models.
2. Langchain: An AI framework that can host models and add tools to them.

Once you downloaded them, open the terminal and write ollama to activate it. 
There you will type the name of the model you wish to download. I recommend llama3.2 since it's light enough to utilize without a dedicated gpu but still capable.
    - To download it type: ollama pull llama3.2
    - Make sure you have at least 2 GBs of storage to download it. 

Finally, make sure you download the frameworks' libraries to connect the model to the code. 
    - In the terminal enter: pip install ollama, langchain, langchain_ollama

And Voila! You now own a private llm model that saves its responses on a seperate file along with the question asked and its' timestamp.

## Optional Feastures 

 Don't forget you can save your data under a different file name to segment queries into different topics.
 You can also delete the file saving the responses in the program itself by typing: clear. 

 That's everything! Happy researching!  
