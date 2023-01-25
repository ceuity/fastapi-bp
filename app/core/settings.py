from pydantic import BaseSettings, Field


class MongoSettings(BaseSettings):
    scheme: str = Field(default="mongodb", env="MONGO_SCHEME")
    host: str = Field(default="localhost", env="MONGO_HOST")
    username: str = Field(None, env="MONGO_USERNAME")
    password: str = Field(None, env="MONGO_PASSWORD")
    db_name: str = Field(default="sample", env="MONGO_DBNAME")


class S3Settings(BaseSettings):
    bucket: str = Field(None, env="AWS_S3_BUCKET")


class AwsSettings(BaseSettings):
    profile: str = Field(default="default", env="AWS_PROFILE")
    region: str = Field(default="us-east-1", env="AWS_DEFAULT_REGION")
    s3: S3Settings = S3Settings()


class ApplicationSettings(BaseSettings):
    env: str = "dev"
    mongo: MongoSettings = MongoSettings()
    aws: AwsSettings = AwsSettings()


settings: ApplicationSettings = ApplicationSettings()
