import json

from google.cloud.bigquery import schema


def parse_schema(schema_dict=None, text=None, path=None):
    """ Parse a schema at the given path.
    Caller may pass a path to the schema using the path argument,
    the text of a schema using the text argument, or the parsed
    schema in the form of a dict to the schema_dict argument.

    :param dict schema_dict: Parsed schema, like from json.loads('...')
    :param str text: Schema as a json string
    :param str path: Path to a json schema
    :return: a list of SchemaFields
    :rtype: generator of SchemaFields
    """
    if path:
        with open(path) as schema_file:
            text = schema_file.read()
    if text:
        schema_dict = json.loads(text)
    for field in schema_dict:
        yield schema.SchemaField.from_api_repr(field)
