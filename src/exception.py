from types import TracebackType
from typing import Protocol, override


class ErrorDetail(Protocol):
    def exc_info(
        self,
    ) -> tuple[
        type[BaseException] | None,
        BaseException | None,
        TracebackType | None,
    ]:
        ...


def error_message_detail(error: object, error_detail: ErrorDetail) -> str:
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"Error message [{error!s}]"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error in script [{file_name}] "
        f"line [{line_number}] "
        f"message [{error!s}]"
    )


class CustomException(Exception):
    error_message: str

    def __init__(self, error_message: str, error_detail: ErrorDetail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    @override
    def __str__(self) -> str:
        return self.error_message
