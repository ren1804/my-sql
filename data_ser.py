import pickle
import io
from pprint import pprint
from dataclasses import dataclass
from zipfile import ZipFile
from datetime import datetime

my_data= dict(name="David", real_number=76.54, count=22,
                        pets=['Astrophe', 'Kachina', 'Jackson', 'Rebel'])

pkl = pickle.dumps(my_data)
#pprint(pkl, width=50)

new_data = pickle.loads(pkl)
print(new_data)

with open('data.pkl', 'wb') as fh:
        pickle.dump(my_data, fh)

