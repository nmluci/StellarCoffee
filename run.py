from app import stellar_app

app = stellar_app(debug=False)

if __name__ == '__main__':
   app.run(debug=True)