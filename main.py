from travel import create_app

# runs the application when executed allowing for the web app to be accessed via a local address
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)