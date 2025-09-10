from functools import singledispatch
from typing import Any, Iterator, NamedTuple


class BaseQueryParams(NamedTuple):
    objects: list
    quantities: list
    attributes: list


class SpecialQueryParams(NamedTuple):
    format: str
    item: str = None
    sortby: str = None


class QueryFilters(NamedTuple):
    filters: list


class BoolQueryParams(NamedTuple):
    first: bool
    closest: bool
    complete: bool


def namedtuple_items(nt: NamedTuple) -> Iterator[tuple[Any]]:
    yield from zip(nt._fields, nt)


@singledispatch
def format_query_params(params: BaseQueryParams) -> str:
    formatted = []
    for _, value in namedtuple_items(params):
        formatted.append("+".join(value_part for value_part in value))
    return "/".join(value for value in formatted)


@format_query_params.register
def _(params: SpecialQueryParams) -> str:
    return "&".join(
        f"{field}={value}" for field, value in namedtuple_items(params)
    )


@format_query_params.register
def _(params: QueryFilters) -> str:
    return "&".join(filter_ for filter_ in namedtuple_items(params))


@format_query_params.register
def _(params: BoolQueryParams) -> str:
    return "&".join(field_name for field_name, _ in namedtuple_items(params))
