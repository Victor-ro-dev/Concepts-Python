from abc import ABC, abstractmethod

# Interface esperada pelo sistema
class LLMClient(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass

# Implementação concreta para um provedor (exemplo: OpenAI)
class OpenAIClient:
    def create_completion(self, prompt):
        return f"OpenAI response to: {prompt}"

# Adapter para OpenAIClient
class OpenAIAdapter(LLMClient):
    def __init__(self, openai_client):
        self.openai_client = openai_client

    def generate_text(self, prompt: str) -> str:
        return self.openai_client.create_completion(prompt)

# Implementação concreta para outro provedor (exemplo: HuggingFace)
class HuggingFaceClient:
    def query_model(self, prompt):
        return f"HuggingFace response to: {prompt}"

# Adapter para HuggingFaceClient
class HuggingFaceAdapter(LLMClient):
    def __init__(self, hf_client):
        self.hf_client = hf_client

    def generate_text(self, prompt: str) -> str:
        return self.hf_client.query_model(prompt)

# Uso do Adapter
if __name__ == "__main__":
    openai = OpenAIClient()
    hf = HuggingFaceClient()

    llm1 = OpenAIAdapter(openai)
    llm2 = HuggingFaceAdapter(hf)

    prompt = "Explique o padrão Adapter em poucas palavras."
    print(llm1.generate_text(prompt))
    print(llm2.generate_text(prompt))