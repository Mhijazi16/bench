from langchain_ollama import ChatOllama

def benchmark(model_name: str): 
    llm = ChatOllama(model=model_name, temperature=0)
    tokens = []
    for token in llm.stream("Write a TCP server in C++"): 
        print(f"🍿Tokens Writtern: {len(tokens)}", flush=True, end="\r")
        tokens += token.content


models = ["llama3.1","llama3-groq-tool-use","internlm2","deepseek-coder-v2","gemma2"]
for model in models: 
    print(f"[💺] STARTING BENCHMARK FOR {model}")
    benchmark(model)

