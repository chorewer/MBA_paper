from http import HTTPStatus
from typing import Any,List,Mapping,Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

from dotenv import load_dotenv, find_dotenv
import dashscope
from dashscope import Generation
import os

from model_config import QWEN_MODEL,QWEN_SEED,QWEN_MAX_TOKENS,QWEN_TOP_P,QWEN_TEMPERATURE,QWEN_REPETITION_PENALTY

class QwenLLM(LLM):
    n:int
    
    def init(self):
        load_dotenv(verbose=True)
        api_key = os.getenv("DASHSCOPE_API_KEY")
        dashscope.api_key = api_key
    
    @property
    def _llm_type(self) -> str:
        return "Qwen-turbo"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None
    ):
        response = Generation.call(
            model= QWEN_MODEL,
            messages=[{"role":"user","content":prompt}],
            seed= QWEN_SEED,
            result_format="message",
            max_tokens= QWEN_MAX_TOKENS,
            top_p = QWEN_TOP_P,
            temperature= QWEN_TEMPERATURE,
            repetition_penalty= QWEN_REPETITION_PENALTY
        )
        if response.status_code == HTTPStatus.OK:
            return response.output.choices[0]['message']['content']
        else:
            print(response.message)
        # return prompt
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"n":self.n}
    
    
if __name__=="__main__":
    llm = QwenLLM(n=10)
    llm.init()
    print(llm._call("where do you from?"))