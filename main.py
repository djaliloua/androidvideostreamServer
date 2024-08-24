import asyncio
import threading

from CommonLibrary.server import CamStreamingApp
# from CommonLibrary.UserControls.CamControl import Cam

loop = asyncio.get_event_loop_policy().get_event_loop()

if __name__ == "__main__":
    # CamStreamingApp().run()
    # t = threading.Thread(target=runweb, args=())
    # t.start()
    loop.run_until_complete(
        CamStreamingApp().async_run("asyncio")
    )
    loop.close()
