from argparse import ArgumentParser

from src import constants, models, api_manager, query_builder

parser = ArgumentParser("oacapi", description="Open Astronomy Catalog CLI")

parser.add_argument(
    "--objects",
    default=[constants.DEFAULT_OBJECT],
    nargs="*",
    metavar="OBJECT NAME",
    help="objects to lookup",
)
parser.add_argument(
    "--quantities",
    default=[],
    nargs="*",
    metavar="QUANTITY",
    help="quantities to lookup",
)
parser.add_argument(
    "--attributes",
    default=[],
    nargs="*",
    metavar="ATTRIBUTE",
    help="attributes to lookup",
)
parser.add_argument(
    "--catalog",
    choices=[value.value for value in constants.Catalog],
    default=constants.Catalog.ASTROCATS.value,
    help=f"search catalog, default: {constants.Catalog.ASTROCATS.value}",
)
parser.add_argument(
    "--format",
    choices=[value.value for value in constants.OutputFormat],
    default=constants.OutputFormat.JSON.value,
    help="return data in the specified format, "
    f"default: {constants.OutputFormat.JSON.value}",
)
parser.add_argument(
    "--item",
    metavar="NUMBER",
    help="return only the nth item of each of the listed quantities",
)
parser.add_argument(
    "--sortby",
    metavar="ATTRIBUTE",
    help="sort the returned array by the specified attribute",
)
parser.add_argument(
    "--filters",
    default=[],
    nargs="*",
    metavar="KEY=VALUE",
    help="filter output by specified quantity values",
)
parser.add_argument(
    "--first",
    action="store_true",
    help="return only the first of each of the listed quantities",
)
parser.add_argument(
    "--closest",
    action="store_true",
    help="""
        return the quantities with the closest value to the specified attributes. 
        If multiple attributes are specified, the closest to each will be returned
    """,
)
parser.add_argument(
    "--complete",
    action="store_true",
    help="return results containing all of the requested attributes",
)


def main() -> None:
    arguments = parser.parse_args()

    query = query_builder.QueryBuilder(
        arguments.catalog,
        models.QueryFilters.from_object(arguments),
        models.BaseQueryParams.from_object(arguments),
        models.BoolQueryParams.from_object(arguments),
        models.SpecialQueryParams.from_object(arguments),
    ).build()

    print(api_manager.make_request(query))


if __name__ == "__main__":
    main()
