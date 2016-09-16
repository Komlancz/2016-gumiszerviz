from setup.gumi_data_manager import *
from models.contact_model import Contact
from models.winter_wheel_model import WinterWheel
from models.summer_wheel_model import SummerWheel
from models.warehouse_model import Warehouse


class BasicInfo(BaseModel):
    rendsz = CharField()
    ready = CharField()
    protekcio = IntegerField()
    contact = ForeignKeyField(Contact, related_name='contact_key', null=True)
    winter = ForeignKeyField(WinterWheel, related_name='winter_key', null=True)
    summer = ForeignKeyField(SummerWheel, related_name='summer_key', null=True)
    warehouse = ForeignKeyField(Warehouse, related_name='raktar_key', null=True)

    @classmethod
    def get_contact(cls):
        query = Contact.select(Contact.id).where(cls.id == Contact.id)
        for cont in cls.select():
            cont.contact = query
            cont.save()

    @classmethod
    def get_winter(cls):
        query = WinterWheel.select(WinterWheel.id).where(cls.id == WinterWheel.id)
        for wint in cls.select():
            wint.winter = query
            wint.save()

    @classmethod
    def get_summer(cls):
        query = SummerWheel.select(SummerWheel.id).where(cls.id == SummerWheel.id)
        for summ in cls.select():
            summ.summer = query
            summ.save()

    @classmethod
    def get_warehouse(cls):
        query = Warehouse.select(Warehouse.id).where(cls.id == Warehouse.id)
        for ware in cls.select():
            ware.warehouse = query
            ware.save()