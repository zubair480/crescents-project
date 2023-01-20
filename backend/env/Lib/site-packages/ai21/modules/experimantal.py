from ai21 import Completion
from ai21.modules.resources.nlp_task import NLPTask
from ai21.modules.rewrite import Rewrite
from ai21.modules.summarize import Summarize


class Experimental(NLPTask):

    @classmethod
    def _execute(cls, module: str, **params):
        url = f'{cls.get_base_url(**params)}/experimental/{module}'
        return super().execute(task_url=url, **params)

    @classmethod
    def rewrite(cls, **params):
        return Rewrite.execute(experimental_mode=True, **params)

    @classmethod
    def summarize(cls, **params):
        return Summarize.execute(experimental_mode=True, **params)

    @classmethod
    def j1_grande_instruct(cls, **params):
        params["model"] = "j1-grande-instruct"
        return Completion.execute(experimental_mode=True, **params)
