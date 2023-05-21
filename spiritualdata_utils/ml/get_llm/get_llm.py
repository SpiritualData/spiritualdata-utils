from langchain.llms import OpenAI

def get_llm(model_name="gpt-4"):
    """
    Make sure to set the environment variable OPENAI_API_KEY
    
    Args:
        - model_name

    Returns:
        - llm (LangChain LLM instantiation)
    """
    llm = OpenAI(model_name=model_name, n=2, best_of=2)
    return llm
    