def benchmark(model_name: str): 
    pass

models = ["llama3.1","llama3-groq-tool-use","internlm2","deepseek-coder-v2","gemma2"]
for model in models: 
    print(f"[💺] STARTING BENCHMARK FOR {model}")
    benchmark(model)
