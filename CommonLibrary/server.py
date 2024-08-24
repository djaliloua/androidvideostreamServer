from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy import platform
from CommonLibrary.CamControl import close

if platform == "android":
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android import mActivity

    View = autoclass('android.view.View')


    @run_on_ui_thread
    def hide_landscape_status_bar(instance, width, height):
        # width,height gives false layout events, on pinch/spread
        # so use Window.width and Window.height
        if Window.width > Window.height:
            # Hide status bar
            option = View.SYSTEM_UI_FLAG_FULLSCREEN
        else:
            # Show status bar
            option = View.SYSTEM_UI_FLAG_VISIBLE
        mActivity.getWindow().getDecorView().setSystemUiVisibility(option)


    request_permissions(
        [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.CAMERA, Permission.CAMERA,
         Permission.WAKE_LOCK])


class CamStreamingApp(MDApp):
    server = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.init_service()

    def build(self):
        return Builder.load_file("views/server.kv")

    def on_start(self):
        pass

    def on_server(self, instance, value):
        print("server has changed")

    def on_pause(self):
        argument = ''
        #self.service.start(self.mActivity, argument)
        return True

    def on_resume(self):
        #self.service.stop(self.mActivity)
        return True

    def on_stop(self):
        close()

    def init_service(self):
        # rg.kivy.test
        if platform == 'android':
            from jnius import autoclass
            self.SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
                packagename=u'org.test.testapp',
                servicename=u'Myservice'
            )
            self.service = autoclass(self.SERVICE_NAME)
            self.mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
