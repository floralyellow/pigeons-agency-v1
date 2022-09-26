from typing import Any, List

from ..exceptions.custom_exceptions import WrongInputException


class InputValidator:
    """Helper class to validate data coming from POST requests"""

    def get_key(request: Any, key: str) -> Any:
        if key not in request.POST:
            raise WrongInputException(f"Error: missing key: {key}")
        return request.POST.get(key)

    def validate_is_int(value: Any):
        if not value.isdigit() or not int(value):
            raise WrongInputException("Error: incorrect input type")

    def validate_is_int_in_range(value: Any, min_value: int, max_value: int):
        if not value.isdigit() or not int(value) in range(min_value, max_value):
            raise WrongInputException("Error: incorrect input value")

    def validate_is_in_values(value: Any, keys: List[str]):
        if not value in keys:
            raise WrongInputException("Error: incorrect input value")
