import uvicorn


def start():
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info")


def main():
    start()


if __name__ == "__main__":
    main()
