from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL, COMObject
from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume,
    IAudioEndpointVolumeCallback,
)




class AudioEndpointVolumeCallback(COMObject):
    _com_interfaces_ = [IAudioEndpointVolumeCallback]
    
    
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = (self.devices
                .Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None))
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
        self.volume.RegisterControlChangeNotify(self)


    def OnNotify(self, pNotify):
        if pNotify.contents.bMuted: self.volume.SetMute(0, None)



if __name__ == "__main__":
    avc = AudioEndpointVolumeCallback()
    avc.volume.SetMute(0, None)
    _ = input("Input anything to stop the script.") 
