import json

from google.cloud.bigquery import schema


def parse_schema(schema_dict=None, text=None, path=None):
    """ Parse a schema at the given path.
    return: a generator of SchemaFields
    """
    if path:
        with open(path) as schema_file:
            text = schema_file.read()
    if text:
        schema_dict = json.loads(text)
    for field in schema_dict:
        yield schema.SchemaField.from_api_repr(field)
