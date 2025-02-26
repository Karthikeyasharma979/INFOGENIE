from smolagents import Tool
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
load_dotenv()
class summarize(Tool):
    name = "summarize_text"
    description = """
    This tool takes a long text input and generates a concise summary.
    It helps users get a quick overview of the content.
    """
    inputs = {
        "text": {
            "type": "string",
            "description": "The input text that needs to be summarized.",
        },
    }
    output_type = "string"

    def __init__(self,):
        super().__init__()
        self.client =InferenceClient(
            provider="hf-inference",
            api_key=load_dotenv("HF_API_KEY"),
        )
    
    def forward(self, text: str):
        summary = self.client.summarization(  
            model="facebook/bart-large-cnn",
            text=text,  
        )
        return summary.summary_text







