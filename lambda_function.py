import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    destination_bucket = 'image-resized-bucket-project-9'

    s3.copy_object(
        CopySource={
            'Bucket': source_bucket,
            'Key': key
        },
        Bucket=destination_bucket,
        Key='copied-' + key
    )

    return {
        'statusCode': 200
    }
