import json, pika

# Connect to RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')  # default credentials
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials)
)
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='book_queue')

# Send book to the queue
def sendBook(book):
    book_id = book['id']
    channel.basic_publish(
        exchange='', 
        routing_key='book_queue', 
        body=json.dumps(book)
    )
    return book_id


with open('books.json') as json_file:
    data = json.load(json_file)
    for book in data:
        print('Name: ' + book['title'])
        book_id = sendbook(book)
        print('Book ID: ' + book_id)

# Close the connection
connection.close()