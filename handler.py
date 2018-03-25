import json
from pykafka import KafkaClient, SslConfig
#import Queue

def hello(event, context):

    # init with Certs n' stuff
    config = SslConfig(cafile='certs/ca.pem',
                        certfile='certs/cert.pem',  # optional
                        keyfile='certs/key.pem')  # optional
                        #password='unlock my client key please')  # optional
    client = KafkaClient(hosts="steamer-01.srvs.cloudkafka.com:9093,steamer-03.srvs.cloudkafka.com:9093,steamer-02.srvs.cloudkafka.com:9093",ssl_config=config)

    topic = client.topics[b"47x9-default"]
    message=''

    with topic.get_sync_producer() as producer:
      for i in range(100):
        message='test message ' + str(i)

        producer.produce(message.encode(),b'data')

    # with topic.get_producer(delivery_reports=True) as producer:
    #   count = 0
    #   while True:
    #       count += 1
    #       producer.produce('test msg', partition_key='{}'.format(count))
    #       if count % 10 ** 5 == 0:  # adjust this or bring lots of RAM ;)
    #           while True:
    #               try:
    #                   msg, exc = producer.get_delivery_report(block=False)
    #                   if exc is not None:
    #                       print('Failed to deliver msg {}: {}'.format(msg.partition_key, repr(exc)))
    #                   else:
    #                       print('Successfully delivered msg {}'.format(msg.partition_key))
    #               except: # Queue.Empty:
    #                   break
    
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
