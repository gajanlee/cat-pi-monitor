import bottle

app = application = bottle.default_app()

if __name__ == "__main__":
    bottle.run(server="gunicorn", host="0.0.0.0", port=8080)