# How to use packages
#
# 1. Activate your virtual environment.
#       source env/bin/activate
#
# 2. Install package:
#       pip install [package-name]
#       pip install requests
#
# 3. Use the package.

import requests

r = requests.get('http://google.com')
print(r.content)

# 4. Get or display the packages info from the virtual env
#       pip freeze

# 5. Create a requirements .txt file with the required packages in the project for sharing.
#       pip freeze > requirements.txt
