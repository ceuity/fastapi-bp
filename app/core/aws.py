from aiobotocore.session import AioSession
from aiobotocore.config import AioConfig
from types_aiobotocore_s3.client import S3Client


from app.core.log import logger

AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"


async def get_aws_session(
    profile: str = "default",
) -> AioSession:
    """AWS Session 생성"""

    session: AioSession = AioSession(profile=profile)

    logger.info("AWS Session Started")
    yield session
    logger.info("AWS Session Closed")


async def get_s3_client(
    session: AioSession,
    region: str = "us-east-1",
) -> S3Client:
    """AWS S3 Client 생성"""

    async with session.create_client("s3", region_name=region, config=AioConfig(signature_version="s3v4")) as s3_client:

        logger.info("AWS S3 Client Started")
        yield s3_client
        logger.info("AWS S3 Client Closed")
