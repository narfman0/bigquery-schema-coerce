import unittest

from bigquery_schema_coerce import core


class TestCore(unittest.TestCase):
    def test_parse_schema(self):
        fixture_path = "tests/fixtures/schema.json"
        schema = list(core.parse_schema(path=fixture_path))
        self.assertEqual(3, len(schema))
        self.assertEqual(2, len(schema[2].fields))
