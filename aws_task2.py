import boto3
import base64
import json
import os

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract bucket name, file name, and file content from the event
        bucket_name = os.environ.get('BUCKET_NAME')  # Set this in Lambda environment variables
        file_name = event['file_name']
        file_content_base64 = event['file_content']
        
        # Decode the base64 content
        file_content = base64.b64decode(file_content_base64)
        
        # Upload the file to the S3 bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f"File '{file_name}' successfully uploaded to bucket '{bucket_name}'."
            })
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': "The event must include 'file_name' and 'file_content' keys."
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
