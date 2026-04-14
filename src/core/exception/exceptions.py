from core.exception.codes import ErrorCode


class BaseCustomException(Exception):
    def __init__(self, status_code: int, code: str, detail: str):
        self.status_code = status_code
        self.code = code
        self.detail = detail
        super().__init__(detail)


class UnexpectedException(BaseCustomException):
    def __init__(self, detail: str = "서버 내부 오류"):
        super().__init__(status_code=500, code=ErrorCode.INTERNAL_SERVER_ERROR, detail=detail)


class DatabaseException(BaseCustomException):
    def __init__(self, detail: str = "데이터베이스 에러"):
        super().__init__(status_code=500, code=ErrorCode.DB_ERROR, detail=detail)
