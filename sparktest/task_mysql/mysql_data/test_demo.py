# import helper
import settings
# helper.load_settings()
# from mysql import db
import test
db.connect()
db.updata([{'time':129, 'columns2':126}], 'test_update')
print(db.find('test_update', 0,1000))
db.disconnect()