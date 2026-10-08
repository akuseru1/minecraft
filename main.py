
from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv()

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

# print(url)
# print(key)


supabase: Client = create_client(url, key)

try:
    response = supabase.table("Minecraft_Command").select("*").execute()
    minecraft_item_get = response.data[0]["Item_ENG"]
    print(f"/give @p {minecraft_item_get}")
    # for i in response.data:
    #     print(i["title"])
except Exception as e:
    print("サーバーからの返事:", e)