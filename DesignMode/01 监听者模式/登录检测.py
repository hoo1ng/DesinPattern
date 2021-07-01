import time
from .framework import *


class Account(Observable):

    def __init__(self):
        super().__init__()
        self.__lastIP = {}
        self.__lastRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.isLongDistance(name, region):
            self.notifesObservers({"name": name, "ip": ip, "region": region, "time": time})

        self.__lastRegion[name] = region
        self.__lastIP[name] = ip

    def __getRegion(self, ip):
        ipRegions = {
            "101.47.18.19": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ipRegions.get(ip);
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        lastestRegion = self.__lastRegion.get(name)
        return lastestRegion is not None and lastestRegion != region


class SmsSender(Observer):
    def update(self, observable, object):
        print("[短信发送] " + object["name"] + "您好！ 检测到您的账户可能登录异常。最近一次登录信息：\n"
                                           "登录地区：" + object["region"] + "登录IP： " + object["ip"] + "登录时间:"
                                                                                                  "" + time.strftime(
            "%Y-%m-%d %H:%M%s", time.gmtime(object["time"])))


class MailSender(Observer):
    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！ 检测到您的账户可能登录异常。最近一次登录信息：\n"
                                           "登录地区：" + object["region"] + "登录IP： " + object["ip"] + "登录时间:"
                                                                                                  "" + time.strftime(
            "%Y-%m-%d %H:%M%s", time.gmtime(object["time"]))
              )


def testLogin():
    account = Account()
    account.addObserver(SmsSender())
    account.addObserver(MailSender())
    account.login("Tony", "101.47.18.9", time.time())
    account.login("Tony", "67.218.147.69", time.time())


if __name__ == '__main__':
    testLogin()
