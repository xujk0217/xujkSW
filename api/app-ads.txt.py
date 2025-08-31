def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': 'google.com, pub-4105005748617921, DIRECT, f08c47fec0942fa0\n'
    } 