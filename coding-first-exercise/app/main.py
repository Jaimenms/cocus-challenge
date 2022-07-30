import sys
from .cli import Cli, ParserVersion
from .predicate import Predicate
from .criterias.suffix import Suffix
from .folder import Folder


def main():
    args = Cli(parser_version=ParserVersion.v1).parse(sys.argv[1:])
    suffix = Suffix(criteria_value=args.suffix)
    predicate = Predicate(criterias=[suffix, ])
    folder = Folder(path=args.path)
    files = folder.traverse(predicate=predicate)
    print(files)
