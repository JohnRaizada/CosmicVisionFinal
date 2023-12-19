import asyncio
import time
from .aimodel import AIModel


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AIInterface(metaclass=Singleton):
    def __init__(self):
        # Initialize any necessary variables or resources here
        self.consumer = None

    def set_consumer(self, consumer):
        self.consumer = consumer

    def image_generated(self, data):
        # image_generated is called when the image is generated
        # call the consumer's image_generated method
        print("Method called")
        print(self.consumer)
        if self.consumer:
            asyncio.run_coroutine_threadsafe(
                self.consumer.image_generated(data), self.consumer.loop
            )
    def process_data(self, coordinates, zoomLevel, coordinates_hash, starttime, endtime):
        AIModel.generate_images(self, coordinates, zoomLevel, coordinates_hash, starttime, endtime)
