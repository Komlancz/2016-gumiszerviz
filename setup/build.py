from setup.gumi_data_manager import *
from models.basic_info_model import BasicInfo
from models.contact_model import Contact
from models.winter_wheel_model import WinterWheel
from models.summer_wheel_model import SummerWheel
from models.warehouse_model import Warehouse


class Create:
    @classmethod
    def building(cls):
        db.connect()
        print("Connected...")
        try:
            db.create_tables([BasicInfo, Contact, WinterWheel, SummerWheel, Warehouse], safe=True)
            print("Tables are created...")
        except OperationalError:
            print("Tables already exists!")