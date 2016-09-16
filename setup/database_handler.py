from models.basic_info_model import BasicInfo
from models.contact_model import Contact
from models.winter_wheel_model import WinterWheel
from models.summer_wheel_model import SummerWheel
from models.warehouse_model import Warehouse
from setup.open_files import OpenFiles


class Upload:
    FILE = OpenFiles.open_file('store/good_warehouse.csv')

    @classmethod
    def basic_info_upload(cls):
        for car in cls.FILE:
            BasicInfo.create(rendsz=car[0], ready=car[1], protekcio=car[2], contact=None, winter=None, summer=None, warehouse=None)

    @classmethod
    def contact_upload(cls):
        for contact in cls.FILE:
            Contact.create(name=contact[3], phone=contact[4], email=contact[5], address=contact[6], others=contact[7])

    @classmethod
    def summer_wheel_upload(cls):
        for summer in cls.FILE:
            SummerWheel.create(brand=summer[8], size=summer[9], season=summer[10])

    @classmethod
    def winter_wheel_upload(cls):
        for winter in cls.FILE:
            WinterWheel.create(brand=winter[11], size=winter[12], season=winter[13])

    @classmethod
    def warehouse_upload(cls):
        for ware in cls.FILE:
            Warehouse.create(position=ware[14], felni=ware[15])

    @classmethod
    def get_contact_id(cls):
        BasicInfo.get_contact()

    @classmethod
    def get_summer_id(cls):
        BasicInfo.get_summer()

    @classmethod
    def get_winter_id(cls):
        BasicInfo.get_winter()

    @classmethod
    def get_warehouse_id(cls):
        BasicInfo.get_warehouse()


    @classmethod
    def get_without_email(cls):
        without_dict = {}
        query = Contact.select()
        print(query)
        for i in query:
            if i.email == 'None':
                without_dict[i.id] = i.name
        return without_dict
