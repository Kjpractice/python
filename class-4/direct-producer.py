import time
from server import channel
logs_files = open("assets\web-server-nginx.log","r")
QUEUES = [ 
    {
        "name": "queue-data-lake",
        "routing_key": "logs"
    }, 
    { 
        "name": "queue-data-clean", 
        "routing_key": "logs" 
    }
]
EXCHANGE_NAME = "topic-exchange-logs"
# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')
# create queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['routing_key'])

# publish event
for line in logs_files:
    #channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=QUEUE_LOGS, body=line)
    #time.sleep(5)
    time.sleep(0.05)
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key="logs", body=line)


    print(f"[x] published event `{line}` in topic `{queue['routing_key']}`")

#import time

#from server import channel

#QUEUE_HELLO_WORLD = "hello-world"
#EXCHANGE_NAME = "direct-exchange-hello-world"

# create exchange
#channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='direct')

# create a queue
#channel.queue_declare(queue=QUEUE_HELLO_WORLD)
#channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_HELLO_WORLD)

# publish event
#events = ["event 1", "event 2", "event 3", "event 4", "event 5"]

#for event in events:
    #channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=QUEUE_HELLO_WORLD, body=event)
    #time.sleep(2)
    #print(f"[x] published {event}")
