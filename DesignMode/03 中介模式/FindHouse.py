class HouseInfo:
    def __init__(self, area, price, has_window, has_bathroom, has_kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__has_window = has_window
        self.__has_bathroom = has_bathroom
        self.__has_kitchen = has_kitchen
        self.__address = address
        self.__owner = owner

    def get_address(self):
        return self.__address

    def get_onwer_name(self):
        return self.__owner.get_name()

    def show_info(self):
        print("面积： " + str(self.__area) + "平方米" +
              "价格： " + str(self.__price) + "元" +
              "窗户： " + ("有" if self.__has_window else "没有") +
              "厨房： " + ("有" if self.__has_kitchen else "没有") +
              "浴室： " + ("有" if self.__has_bathroom else "没有"))


class HousingAgency:
    def __init__(self, name):
        self.__house_infos = []
        self.__name = name

    def get_name(self):
        return self.__name

    def add_houseinfo(self, houseinfo):
        if houseinfo not in self.__house_infos:
            self.__house_infos.append(houseinfo)

    def remove_houseinfo(self, houseinfo):
        for info in self.__house_infos:
            if info == houseinfo:
                self.__house_infos.remove(info)

    def get_search_condition(self, description):
        return description

    def get_match_infos(self, search_condition):
        print(self.get_name(), "为您找到一下最合适的房源：")
        for info in self.__house_infos:
            info.show_info()
        return self.__house_infos

    def sign_contract(self, houseinfo, period):
        print(self.get_name() , "与房东" , houseinfo.get_onwer_name(), "签订", houseinfo.get_address(),"的房子合同，租期为：", period, "年, 租期内", self.get_name(), "有权对其进行使用和转租！")

    def sign_contracts(self, period):
        for info in self.__house_infos:
            self.sign_contract(info, period)


class HouseOwner:
    def __init__(self, name):
        self.__name = name
        self.__houseinfo = None

    def get_name(self):
        return self.__name

    def set_houseinfo(self,  area, price, has_window, has_bathroom, has_kitchen, address, owner):
        self.__houseinfo = HouseInfo(area, price, has_window, has_bathroom, has_kitchen, address, owner)

    def public_houseinfo(self, agency):
        agency.add_houseinfo(self.__houseinfo)
        print(self.get_name(), "在", agency.get_name(), "发布房源出租信息")
        self.__houseinfo.show_info()


class Customer:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def find_house(self, description, agency):
        print("我是" + self.get_name() + "，我想找一个", description , "的房子")
        print()
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, houseinfos):
        size = len(houseinfos)
        return houseinfos[size-1]

    def sign_contract(self, houseinfo, agency, period):
        print(self.get_name(), "与中介", agency.get_name(), "签订", houseinfo.get_address(), "的房子的组人合同，租期", period, "年，合同期内", self.__name , "有权使用！")


if __name__ == '__main__':
    myhome = HousingAgency("我爱你家")
    zhangsan = HouseOwner("张三")
    zhangsan.set_houseinfo(20, 2600, True, False, False, "上地犀利", zhangsan)
    zhangsan.public_houseinfo(myhome)

    lisi = HouseOwner("李四")
    lisi.set_houseinfo(30, 3800, True, True, True, "西二旗的太阳", lisi)
    lisi.public_houseinfo(myhome)

    wangwu = HouseOwner("王五")
    wangwu.set_houseinfo(40, 5200, True, True, True, "东直门的艾利欧", wangwu)
    wangwu.public_houseinfo(myhome)
    print()

    myhome.sign_contracts(3)
    print()

    tony = Customer("Tony")
    houseinfos = tony.find_house("18平方米，要有独立卫生间，要有窗户，最好朝南，有厨房更好！价位200左右", myhome)
    print()

    print("正在看房，寻找最合适的房子")
    print()

    appropriate_house = tony.see_house(houseinfos)
    print()
    tony.sign_contract(appropriate_house, myhome, 1)

