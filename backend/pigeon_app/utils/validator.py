from typing import Union, List, Any, Optional
from ..exceptions.custom_exceptions import WrongInputException

class InputValidator:

    def validate_keys_exist_in_post_data(request: Any, keys: Union[str, List[str]]):
        if isinstance(keys, list):
            for key in keys:
                if key not in request.POST:
                    raise WrongInputException(f'Error: No {key}')
        elif isinstance(keys, str):
            key = keys
            if key not in request.POST:
                raise WrongInputException(f'Error: No {key}')

    def validate_is_int(value: Any, error: Optional[str]):
        if not value.isdigit() or not int(value):
            raise WrongInputException(f'Error: invalid input {error}')


    def validate_is_int_in_range(value: Any, min_value: int, max_value: int, error: Optional[str]):
        if not value.isdigit() or not int(value) in range(min_value, max_value):
            raise WrongInputException(f'Error: invalid input {error}')
