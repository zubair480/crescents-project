def supported_resources():
    from ai21 import Completion, Dataset, CustomModel, Rewrite, Tokenization, Summarization

    return {
        'completion': Completion,
        'tokenization': Tokenization,
        'dataset': Dataset,
        'customModel': CustomModel,
        'rewrite': Rewrite,
        'summarization': Summarization
    }
