from setup.build import Create
from setup.drop_tables import DropTables
from setup.database_handler import Upload


class MainMenu:
    @classmethod
    def running(cls):
        run = True
        print('''HI! Choose one of them:
            1. Build tables
            2. Delete tables
            3. Upload Basic Info Model
            4. Get id and name who has not email address yet
            5. Quit''')

        while run != False:
            choose = int(input())
            if choose == 1:
                Create.building()
            elif choose == 2:
                DropTables.delete()
            elif choose == 3:
                Upload.basic_info_upload()
                Upload.contact_upload()
                Upload.summer_wheel_upload()
                Upload.winter_wheel_upload()
                Upload.warehouse_upload()
                Upload.get_contact_id()
                Upload.get_summer_id()
                Upload.get_winter_id()
                Upload.get_warehouse_id()
            elif choose == 4:
                print(Upload.get_without_email())
            elif choose == 5:
                print("Good Bye!")
                run = False

MainMenu.running()