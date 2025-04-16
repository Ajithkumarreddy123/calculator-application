import json

def lambda_handler(event, context):
    body = event.get('body')

    # First level: convert string to dict
    if isinstance(body, str):
        body = json.loads(body)

    # Second level: check if body has a nested 'body' string again
    if isinstance(body, dict) and 'body' in body and isinstance(body['body'], str):
        body = json.loads(body['body'])

    # Extract base and exponent
    base = body.get('base')
    exponent = body.get('exponent')

    if base is None or exponent is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing base or exponent'})
        }

    result = base ** exponent

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
{
  "body": $input.body
}
