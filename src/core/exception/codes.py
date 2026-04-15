from enum import Enum


class ErrorCode(str, Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"  # 서버 내부 에러
    UNAUTHORIZED = "UNAUTHORIZED"  # 인증 필요 (로그인 안함)
    DB_ERROR = "DB_ERROR"  # 데이터베이스 오류
    HTTP_ERROR = "HTTP_ERROR"  # HTTP 에러
    VALIDATION_ERROR = "VALIDATION_ERROR"  # Pydantic 모델 검증 실패 에러
