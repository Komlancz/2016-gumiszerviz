from setup.gumi_data_manager import *


class SummerWheel(BaseModel):
    brand = CharField()
    size = CharField()
    season = IntegerField()