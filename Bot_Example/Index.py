import sys
sys.path.insert(1, '../Common_Assets')
import Base

Bot = Base.Bot("YOURUSERNAME", "YOURPASSWORD")

Bot.log()
Bot.DIY_txt_to_list("Assets/Follow_File.txt")
Bot.DIY_follow_from_list_with_selenium() # You can also use: Bot.DIY_follow_from_list()
