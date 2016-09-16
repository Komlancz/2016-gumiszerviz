from setup.gumi_data_manager import *


class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    email =  CharField()
    address = CharField()
    others = CharField()