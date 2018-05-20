"""
┌───────────────────┐
│schema: the Todo List│
└───────────────────┘

Usage:
    schema -h | --help
    schema --version
    schema create
    schema add <what> <due>
    schema ls
    schema modify <id> <mwhat> <mdue> <v>

Options:
    -h --help                       Show this screen
    --version                       Show version

Examples:
    schema create
    schema add Test todo 2018-05-16
    schema ls
    schema modify 1 Test schema 2018-05-16 1

Help:
    https://github.com/Verssae/to_do_list_133
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import schema.commands

    options = docopt(__doc__, version=VERSION)

    # 인자 처리하는 부분
    for (k, v) in options.items():
        if hasattr(schema.commands, k) and v:
            module = getattr(schema.commands, k)
            schema.commands = getmembers(module, isclass)
            command = [command[1] for command in schema.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()