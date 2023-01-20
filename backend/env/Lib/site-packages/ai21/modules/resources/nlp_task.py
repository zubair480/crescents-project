from ai21.ai21_studio_client import AI21StudioClient
from ai21.modules.resources.ai21_module import AI21Module


class NLPTask(AI21Module):

    @classmethod
    def execute(cls, task_url, **params):
        client = AI21StudioClient(**params)
        return client.execute_http_request(method='POST', url=task_url, params=params)

