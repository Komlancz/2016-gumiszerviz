from setup.gumi_data_manager import *
from models.basic_info_model import BasicInfo
from models.contact_model import Contact
from models.winter_wheel_model import WinterWheel
from models.summer_wheel_model import SummerWheel
from models.warehouse_model import Warehouse



class DropTables:
    @classmethod
    def delete(cls):
        try:
            db.drop_tables([BasicInfo, Contact, WinterWheel, SummerWheel, Warehouse], safe=True)
            print("Tables are deleted!")
        except OperationalError:
            print("There are not any tables")