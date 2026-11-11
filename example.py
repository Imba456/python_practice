from dotenv import load_dotenv
import os #navigating files

load_dotenv()

nolongerasecret = os.getenv('secret')

print(nolongerasecret)