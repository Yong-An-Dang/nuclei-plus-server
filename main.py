import argparse
import logging
import os
import sys
import urllib

import uvicorn

from server.core.config import Config

logging.basicConfig(level=logging.DEBUG)


def start(args):
    uvicorn.run("server:app", host="127.0.0.1", port=8000, log_level="info")


def set_config(args):
    """
    修改配置文件
    """
    Config().generate_config(args.output_path)
    Config().load_config(args.output_path)
    if args.api_url is not None:
        Config().config_dict["chat.api_url"] = args.data_port
    if args.api_key is not None:
        Config().config_dict["chat.api_key"] = args.web_port
    if args.api_model is not None:
        Config().config_dict["chat.api_model"] = args.web_port
    if args.mysql_url is not None:
        try:
            urllib.parse.uses_netloc.append("mysql")
            url = urllib.parse.urlparse(args.mysql_url)
            Config().config_dict["database.host"] = url.hostname if url.hostname is not None else "127.0.0.1"
            Config().config_dict["database.port"] = int(url.port) if url.port is not None else 3306
            Config().config_dict["database.username"] = url.username if url.username is not None else "root"
            Config().config_dict["database.password"] = url.password if url.password is not None else ""
            Config().config_dict["database.db_name"] = url.path[1:]
        except Exception as e:
            print(e)
            print("[!] Can't resolve mysql connection url: {}".format(args.mysql_url))
            sys.exit(1)
    if args.log_level is not None:
        Config().config_dict["log.level"] = args.log_level
    Config().save_config()


def show_version(args):
    print(f"NPS_{open(os.path.join(os.path.dirname(__file__), 'VERSION')).read().strip()}")


def main():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]')

    subparsers = parser.add_subparsers(title="options")

    parser_start = subparsers.add_parser('start', help='start help')
    parser_start.set_defaults(func=start)
    parser_start.add_argument(
        "-c", "--config-path", help="Assign config file path, like /path/to/config.yaml")

    # 显示版本
    parser_config = subparsers.add_parser('version', help='show version')
    parser_config.set_defaults(func=show_version)

    # 修改配置
    parser_config = subparsers.add_parser('config', help='config help')
    parser_config.set_defaults(func=set_config)

    # 输出路径
    parser_config.add_argument(
        "-o", "--output-path",
        help="Assign path config file path to generate, default is /home/username/openrasp-iast/config.yaml",
        type=str, default=None, nargs='?')

    # 大模型配置
    parser_config.add_argument(
        "-u", "--api-url", help="Assign llm api", type=int)
    parser_config.add_argument(
        "-k", "--api-key", help="Assign llm api key", type=int)
    parser_config.add_argument(
        "-m", "--api-model", help="Assign llm api model name", type=bool)

    # MySQL
    parser_config.add_argument(
        "-c", "--mysql-url", help="Assign Mysql connection url", type=str)

    # Logger
    parser_config.add_argument(
        "-l", "--log-level", help="Assign log level", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])

    args = parser.parse_args()

    if len(vars(args)) == 0:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    # sys.argv = ["main.py", "start"]
    # sys.argv = ["main.py", "config"]
    # sys.argv = ["main.py", "version"]
    # sys.argv = ["main.py", "--help"]
    # sys.argv = ["main.py", "start", "--help"]
    main()
