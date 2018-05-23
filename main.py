import argparse

from executor import CommandsExecutor


def parse_args():
    parser = argparse.ArgumentParser()

    commands_source = parser.add_mutually_exclusive_group()
    commands_source.add_argument('-p', '--path', help="Path to the file with commands",
                                 type=str)
    commands_source.add_argument("-c", "--command", help="Command to execute",
                                 type=str)

    execution_mode = parser.add_mutually_exclusive_group()
    execution_mode.add_argument('-q', '--quiet', help="Don't output all recognized tokens",
                                action="store_true")
    execution_mode.add_argument('-t', '--tranquil', help="Don't execute commands",
                                action="store_true")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    command_executor = CommandsExecutor(**vars(args))
    try:
        command_executor.run()
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
