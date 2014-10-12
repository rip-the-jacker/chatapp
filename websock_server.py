from omnibus.api import publish

def send_hello_world():
    publish(
        'mychannel',  # the name of the channel
        'hello',  # the `type` of the message/event, clients use this name
                  # to register event handlers
        {'text': 'Hello world'},  # payload of the event, needs to be
                                  # a dict which is JSON dumpable.
        sender='server'  # sender id of the event, can be None.
    )

send_hello_world()