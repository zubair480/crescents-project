from ai21.modules.resources.nlp_task import NLPTask
from ai21.utils import validate_mandatory_field


class Tokenization(NLPTask):

    MODULE_NAME = 'tokenize'

    @classmethod
    def execute(cls, **params):
        validate_mandatory_field(key='text', call_name=cls.MODULE_NAME, params=params, validate_type=True, expected_type=str)
        url = f'{cls.get_base_url(**params)}/{cls.MODULE_NAME}'
        return super().execute(task_url=url, **params)





