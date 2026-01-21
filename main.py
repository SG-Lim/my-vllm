from vllm import LLM, SamplingParams

llm = LLM("./model_weights", gpu_memory_utilization=0.7) 
params = SamplingParams(max_tokens=128, temperature=0.7)

prompt = "What is your opinion about humans and their philosophy. 10000 words essay."
outputs = llm.generate([prompt], params)

print(outputs[0].outputs[0].text.strip())