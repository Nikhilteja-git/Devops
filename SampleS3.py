import boto3

def upload_to_s3(file_name, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"✅ {file_name} uploaded to s3://{bucket_name}/")

# Example
upload_to_s3("sample.txt", "your-bucket-name")
