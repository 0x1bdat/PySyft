# stdlib
import functools
from typing import Any as TypeAny
from typing import List as TypeList
from typing import Tuple as TypeTuple

# third party
import fhir2dataset

# syft relative
from . import query  # noqa: 401
from ...ast import add_classes
from ...ast import add_methods
from ...ast import add_modules
from ...ast.globals import Globals
from ..util import generic_update_ast

LIB_NAME = "fhir2dataset"
PACKAGE_SUPPORT = {"lib": LIB_NAME}


def create_ast(client: TypeAny = None) -> Globals:
    ast = Globals(client)

    modules: TypeList[TypeTuple[str, TypeAny]] = [("fhir2dataset", fhir2dataset)]

    classes: TypeList[TypeTuple[str, str, TypeAny]] = [
        ("fhir2dataset.Query", "fhir2dataset.Query", fhir2dataset.Query),
    ]

    methods: TypeList[TypeTuple[str, str]] = [
        ("fhir2dataset.Query.from_sql", "pandas.DataFrame"),
    ]

    add_modules(ast, modules)
    add_classes(ast, classes)
    add_methods(ast, methods)

    for klass in ast.classes:
        klass.create_pointer_class()
        klass.create_send_method()
        klass.create_storable_object_attr_convenience_methods()

    return ast


update_ast = functools.partial(generic_update_ast, LIB_NAME, create_ast)
