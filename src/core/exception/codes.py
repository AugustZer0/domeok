from enum import Enum


class ErrorCode(str, Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"  # 서버 내부 에러
    UNAUTHORIZED = "UNAUTHORIZED"  # 인증 필요 (로그인 안함)
    DB_ERROR = "DB_ERROR"  # 데이터베이스 오류
