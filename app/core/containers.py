from dependency_injector import containers
from dependency_injector.providers import Factory, Resource, Singleton

from app.core.aws import get_aws_session, get_s3_client
from app.core.database import get_mongo_database
from app.core.settings import settings
from app.repository.sample_repository import MongoSampleRepo
from app.service.sample_service import SampleService
from app.util.s3 import S3Util


class Container(containers.DeclarativeContainer):
    """Dependency injector container class"""

    # Object wiring configuration
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.controller.default",
            "app.controller.sample_controller",
        ]
    )

    # Resource
    aws_session = Resource(get_aws_session)
    s3_client = Resource(get_s3_client, session=aws_session)
    db = Resource(
        get_mongo_database,
        scheme=settings.mongo.scheme,
        host=settings.mongo.host,
        db_name=settings.mongo.db_name,
        username=settings.mongo.username,
        password=settings.mongo.password,
    )

    # Utils
    s3 = Singleton(
        S3Util,
        s3_client=s3_client,
        bucket_name=settings.aws.s3.bucket,
        region=settings.aws.region,
    )

    # Repository
    sample_repository = Singleton(MongoSampleRepo, db=db)

    # Service
    sample_service = Factory(
        SampleService,
        sample_repository=sample_repository,
    )
