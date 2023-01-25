from types_aiobotocore_s3.client import S3Client


class S3Util:
    """Base S3 구현체"""

    def __init__(self, s3_client: S3Client, bucket_name: str, region: str):
        """Base S3 initialize"""

        self.s3_client: S3Client = s3_client
        self.bucket_name: str = bucket_name
        self.region: str = region

    async def get_bucket_list(self):
        return await self.s3_client.list_buckets()

    async def get_object(self, key):
        """S3 Get object"""

        try:
            result = await self.s3_client.get_object(Bucket=self.bucket_name, Key=key)

        except Exception:
            result = None

        return result
