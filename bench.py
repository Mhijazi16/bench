from langchain_ollama import ChatOllama
import time

def benchmark(model_name: str): 
    llm = ChatOllama(model=model_name, temperature=0)
    start = time.time()
    tokens = []
    for token in llm.stream("Write a TCP server in C++"): 
        print(f"[🍿] Tokens Written: {len(tokens)}", flush=True, end="\r")
        tokens += token.content
    end = time.time()
    print(f"[⛽] Finished Benchmark For: {model_name}")
    print(f"[🪖] Total Toekens: {len(tokens)}")
    print(f"[⏲️] Time Taken: {end-start} seconds")
    print(f"[🎖️] Token/Seconds: {len(tokens)/(end-start)}")


models = ["llama3.1","llama3-groq-tool-use","internlm2","deepseek-coder-v2","gemma2"]
for model in models: 
    print(f"[💺] STARTING BENCHMARK FOR {model}")
    print("==========================================")
    benchmark(model)
