import json, pika

# Connect to RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')  # default credentials
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials)
)
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='books_queue')

# Send book to the queue
def sendBook(book):
    book_title = book['title']
    channel.basic_publish(
        exchange='', 
        routing_key='books_queue', 
        body=json.dumps(book)
    )
    return book_title


with open('books.json') as json_file:
    data = json.load(json_file)
    for book in data:
        book_title = sendBook(book)
        print('Id: ' + book['id'] + ' | Book : ' + book['title'] + ' ✅')

# Close the connection
connection.close()