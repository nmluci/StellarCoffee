import sys
from app import stellar_app

if "--debug" in sys.argv:
   app = stellar_app(debug=True)
else:
   app = stellar_app()
if __name__ == '__main__':
   app.run(debug=True)