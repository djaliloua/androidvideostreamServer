import asyncio
import concurrent.futures
import time
from kivy.clock import Clock
from kivy.core.camera import Camera
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from CommonLibrary.utility import Server, LOCALHOST, PORT, Data, get_ip

loop = asyncio.get_event_loop()
q = asyncio.Queue()
data = Data()
local_server = None
futur = None


def run_server():
    while True:
        print("start server")
        data.server = Server(LOCALHOST, PORT)
        while not data.server.is_error:
            if data.data is not None:
                data.server.send_bytes(data.data)
                if data.server.close_server:
                    data.server.close_connection()
                    data.server.close_socket()
                    print("close server")
                    break


async def main():
    global result
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, run_server)


def close():
    print("want to cancel the task")
    if result:
        result.cancel()
        if futur is not None:
            print("cancelling task")
            futur.cancel()


class CamBox(MDBoxLayout):
    # app_obj = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.connect_camera(enable_analyze_pixels=True, analyze_pixels_resolution=680)
        Clock.schedule_interval(self._update, 0)
        asyncio.run_coroutine_threadsafe(main(), loop)
        self.app_obj = MDApp.get_running_app()
        
        # print(self.app_obj)
        # self.app_obj.bind(on_stop=close)

    def _update(self, dt):
        """
        Function to capture the images and give them the names
        according to their captured time and date.
        """
        camera = self.ids['camera']
        # print(camera.resolution)
        image = camera.texture
        if image is not None:
            # self.send_bytes(image.pixels)
            data.data = image.pixels

    def on_app_obj(self, *args):
        self.app_obj.bind(on_stop=close)
