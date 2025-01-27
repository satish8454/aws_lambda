import json

def lambda_handler(event, context):
    try:
        num1 = event['num1']
        num2 = event['num2']
        
        # Ensure the inputs are numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Inputs must be numbers")
        
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': result
            })
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': "Both 'num1' and 'num2' must be provided in the event."
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
