from setup.gumi_data_manager import *


class WinterWheel(BaseModel):
    brand = CharField()
    size = CharField()
    season = IntegerField()