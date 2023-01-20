from ai21.constants import STUDIO_HOST, DEFAULT_API_VERSION
from ai21.modules.completion import Completion
from ai21.modules.dataset import Dataset
from ai21.modules.tokenization import Tokenization
from ai21.modules.custom_model import CustomModel
from ai21.modules.experimantal import Experimental

api_key = None
organization = None
application = None
api_version = DEFAULT_API_VERSION
api_host = STUDIO_HOST
timeout_sec = None
num_retries = None
log_level = 'error'


