from langchain.llms import OpenAI

def get_llm(model_name="gpt-4"):
    """

    Args:
        - 

    Returns:
        - llm (LangChain LLM instantiation)
    """
    llm = OpenAI(model_name=model_name, n=2, best_of=2)
    return llm
    