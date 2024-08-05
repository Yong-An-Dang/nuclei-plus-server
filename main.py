import logging

import uvicorn

logging.basicConfig(level=logging.DEBUG)


def start():
    uvicorn.run("server:app", host="127.0.0.1", port=8000, log_level="info")


def main():
    start()


if __name__ == "__main__":
    main()
