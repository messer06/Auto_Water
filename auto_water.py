from app import water, create_app

app = create_app()

if __name__ == "__main__":
    server=app.run(host='0.0.0.0', port=5000, debug=True)
    water.auto_water()

