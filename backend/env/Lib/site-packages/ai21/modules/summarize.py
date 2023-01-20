from ai21.modules.resources.nlp_task import NLPTask
from ai21.utils import validate_mandatory_field


class Summarize(NLPTask):
    MODULE_NAME = 'summarize'

    @classmethod
    def execute(cls, experimental_mode=False, **params):
        validate_mandatory_field(key='text', call_name=cls.MODULE_NAME, params=params, validate_type=True, expected_type=str)
        url = cls.get_base_url(**params)
        if experimental_mode:
            url = f'{url}/experimental'
        url = f'{url}/{cls.MODULE_NAME}'
        return super().execute(task_url=url, **params)
