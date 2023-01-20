from typing import Dict
import logging
import ai21
from ai21.ai21_object import construct_ai21_object
from ai21.errors import MissingInputException, WrongInputTypeException, UnsupportedInputException

logger = logging.getLogger("ai21")


def log_info(message):
    if ai21.log_level == "debug":
        print(message)
        logger.debug(message)
    elif ai21.log_level == "info":
        logger.info(message)


def log_error(message):
    logger.error(message)


def convert_to_ai21_object(obj: Dict):
    if isinstance(obj, list):
        return [construct_ai21_object(i) for i in obj]

    return construct_ai21_object(obj)


def validate_mandatory_field(key: str, call_name: str, params: Dict, validate_type: bool = False, expected_type: type = None):
    value = params.get(key, None)
    if value is None:
        raise MissingInputException(field_name=key, call_name=call_name)
    if not validate_type:
        pass
    if not isinstance(value, expected_type):
        raise WrongInputTypeException(key=key, expected_type=expected_type, given_type=type(value))


def validate_mandatory_fields(key_to_type: Dict, params: Dict, call_name: str):
    [validate_mandatory_field(key=key, call_name=call_name, params=params, validate_type=True, expected_type=key_type)
     for key, key_type in key_to_type]


def validate_unsupported_field(key: str, call_name: str, params: Dict):
    if key in params:
        raise UnsupportedInputException(field_name=key, call_name=call_name)


def get_global_configs():
    from ai21 import api_key, organization, application, api_version, api_host, timeout_sec, num_retries
    return {
        'api_key': api_key,
        'organization': organization,
        'application': application,
        'api_version': api_version,
        'api_host': api_host,
        'timeout_sec': timeout_sec,
        'num_retries': num_retries
    }
