from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    def __init__(self, id, name, type, isDefault=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
        return "type: " + str(self.__type) + "id: " + str(self.__id) + "name: " + str(
            self.__name) + "isDefault: " + str(self.__isDefault)

    def getId(self):
        return self.__id

    def getNmae(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class DeviceList:
    def __init__(self):
        self.__devices = []

    def add(self, deviceItem):
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if item.getId() == id:
                return item
        return None


class DeviceMgr(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        pass

    @abstractmethod
    def active(self, deviceId):
        pass

    @abstractmethod
    def getCurDeviceId(self):
        pass


class SpeakerMgr(DeviceMgr):
    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        devices = DeviceList()
        devices.add(
            DeviceItem("37dd1024-843b-83a1-934c-81ac9230111", "Realtek HighDefinition Audio", DeviceType.TypeSpeaker,
                       True))
        devices.add(
            DeviceItem("215a41c60-1313-24aa-1241-324ac3f445", "NVIDIA HighDefinition Audio", DeviceType.TypeSpeaker,
                       True))
        return devices

    def active(self, deviceId):
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        return self.__curDeviceId


class DeviceUtil:
    def __init__(self):
        self.__mgrs = {DeviceType.TypeSpeaker: SpeakerMgr()}
        # self.__microphoneMgr =

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()


if __name__ == '__main__':
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("麦克风设备列表：")
    if deviceList.getCount() > 0:
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())

    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
        print("当前使用的设备：" + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getNmae())
