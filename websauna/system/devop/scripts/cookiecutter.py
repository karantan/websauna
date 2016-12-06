"""ws-create script."""

import argparse
import os
import binascii
from cookiecutter.main import cookiecutter


def main():
    parser = argparse.ArgumentParser(description='Websauna project generator.')
    parser.add_argument(
        '--app',
        dest='scaffold',
        default='websauna_app',
        help='Project scaffold to use for this project (default: websauna_app)',
    )
    parser.add_argument(
        '--no-input',
        dest='no_input',
        default=False,
    )
    args = parser.parse_args()

    print("Starting to generate new project with cookiecutter ...")

    authentication_random = binascii.hexlify(os.urandom(20)).decode("utf-8")
    authomatic_random = binascii.hexlify(os.urandom(20)).decode("utf-8")
    session_random = binascii.hexlify(os.urandom(20)).decode("utf-8")

    scaffolds = {
        'websauna_app': 'https://github.com/karantan/websauna-cookiecutter',
        'websauna_addon': 'https://github.com/karantan/websauna-cookiecutter-addon',
    }

    if scaffolds.get(args.scaffold):
        cookiecutter(
            scaffolds[args.scaffold],
            no_input=args.no_input,
            extra_context={
                'authentication_random': authentication_random,
                'authomatic_random': authomatic_random,
                'session_random': session_random,
            },
        )
    else:
        print("[*] Scaffold {} not found.".format(args.scaffold))
