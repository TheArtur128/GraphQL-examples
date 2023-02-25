class AppError:
    pass


class InputError(AppError):
    pass


def status_code_according_to(error: Exception) -> int:
    return 404 if isinstance(error, InputError) else 500