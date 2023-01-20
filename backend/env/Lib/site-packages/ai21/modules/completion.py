import json

from ai21.modules.resources.nlp_task import NLPTask
from ai21.utils import validate_mandatory_field, validate_unsupported_field


class Completion(NLPTask):
    MODULE_NAME = 'complete'

    @classmethod
    def execute(cls, experimental_mode=False, **params):
        validate_mandatory_field(key='prompt', call_name=cls.MODULE_NAME, params=params, validate_type=True, expected_type=str)
        if params.get('stopSequences', None) is None:
            params['stopSequences'] = []

        use_sm_endpoint = 'sm_endpoint' in params
        if use_sm_endpoint:
            return cls.execute_sm_endpoint(**params)
        return cls.execute_studio_api(experimental_mode, **params)

    @classmethod
    def execute_studio_api(cls, experimental_mode: False, **params):
        validate_mandatory_field(key='model', call_name=cls.MODULE_NAME, params=params, validate_type=True, expected_type=str)
        model = params.get('model', None)
        custom_model = params.get('custom_model', None)
        if experimental_mode:
            model = f'experimental/{model}'
        url = f'{cls.get_base_url(**params)}/{model}'
        if custom_model is not None:
            url = f'{url}/{custom_model}'
        url = f'{url}/{cls.MODULE_NAME}'
        return super().execute(task_url=url, **params)

    @classmethod
    def execute_sm_endpoint(cls, **params):
        validate_mandatory_field(key='sm_endpoint', call_name=f"{cls.MODULE_NAME} to SageMaker endpoint", params=params, validate_type=True, expected_type=str)
        validate_unsupported_field(key='model', call_name=f"{cls.MODULE_NAME} to SageMaker endpoint", params=params)
        validate_unsupported_field(key='custom_model', call_name=f"{cls.MODULE_NAME} to SageMaker endpoint", params=params)
        endpoint_name = params.pop('sm_endpoint')
        input_json = json.dumps(params)
        from ai21.SM_utils import invoke_sm_endpoint      # import here because boto3 exists only in SM mode
        return invoke_sm_endpoint(endpoint_name, input_json)
