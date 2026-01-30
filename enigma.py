from actor import A, B
from bletchley import Chat, Channel
from game import Game


print('Loading model for Actor A...')
actor_a = A()
print('Loaded model for Actor A')
print('Loading model for Actor B...')
actor_b = B()
print('Loaded model for Actor B')
chat = Chat()

def callback(ch, method, properties, body):
    id = body.decode()
    print(f"Received message: {id}")
    game: Game = chat.retrieve(Game, id)
    game.turn(actor_a, actor_b)
    chat.update(game)
    print("Processing completed")

if __name__ == '__main__':
    channel = Channel().get_channel('turns')
    channel.basic_consume(queue='turns', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
