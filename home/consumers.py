from channels.generic.websocket import AsyncWebsocketConsumer
from json import dumps
from interface.interface import AIInterface
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import threading
import asyncio
from json import loads
import glob

class TestConsumer(AsyncWebsocketConsumer):
    observer = None
    loop = None
    connections = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if TestConsumer.observer is None:
            TestConsumer.loop = asyncio.get_event_loop()
            TestConsumer.observer = Observer()
            TestConsumer.observer.schedule(
                ImageUpdateHandler(self),  # Pass the WebSocket consumer to the handler
                path=r"D:\CosmicVisionLocal3\dist",
                recursive=False,
            )
            TestConsumer.observer.start()
            print("Observer started")
        self.ai_interface = AIInterface()
        self.ai_interface.set_consumer(self)

    async def connect(self):
        print("Connected")
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        await self.channel_layer.group_add(self.room_name, self.room_group_name)
        await self.accept()
        await self.send(text_data=dumps({"status": "connected"}))
        # Create a new list for each connection
        unique_value = self.scope["client"][0]  # Use the client's IP address as a unique value
        self.connections[unique_value] = []

    async def disconnect(self, close_code):
        print("Disconnected")
        # Get the coordinates for this connection
        unique_value = self.scope['client'][0]  # Use the client's IP address as a unique value
        coordinates = self.connections.get(unique_value, [])

        # Delete the files in the 'dist' folder whose names match the coordinates
        for coord in coordinates:
            for file in glob.glob(f"dist/{coord}*"):
                os.remove(file)

        # Remove this connection from the connections dictionary
        if unique_value in self.connections:
            del self.connections[unique_value]
        print(self.connections)

    async def receive(self, text_data):
        await self.send(text_data)
        print(text_data)
        data = loads(text_data)
        coordinates = data.get("location")
        zoomLevel = data.get("zoomLevel")
        starttime = data.get("startDate")
        endtime = data.get("endDate")
        # Add the coordinates to the list for this connection
        unique_value = self.scope["client"][0]  # Use the client's IP address as a unique value
        coordinates_hash = hash(str(coordinates))
        self.connections[unique_value].append(coordinates_hash)
        self.ai_interface.process_data(coordinates, zoomLevel, coordinates_hash, starttime, endtime)
        print(self.connections)

    async def image_generated(self, data):
        print("Notification sending")
        # use coordinates to find proper image
        await self.send(data)
        print("Notification sent")

class ImageUpdateHandler(FileSystemEventHandler):
    def __init__(self, consumer):
        self.debounce_period = 0.1  # delay in seconds
        self.timer = None
        self.consumer = consumer  # Store the WebSocket consumer

    def dispatch(self, event):
        self.on_modified(event)

    def on_modified(self, event):
        if (
            event.src_path == r"D:\CosmicVisionLocal3\dist\react.svg"
            or event.src_path == r"D:\CosmicVisionLocal3\dist\vite.svg"
        ):
            if self.timer is not None:
                self.timer.cancel()
            self.timer = threading.Timer(self.debounce_period, self.handle_event)
            self.timer.start()

    def handle_event(self):
        return
        ai_interface = AIInterface()
        ai_interface.image_generated()
        print("Image generated")
        asyncio.run_coroutine_threadsafe(
            self.consumer.image_generated(), self.consumer.loop
        )
