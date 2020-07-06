import json

from wikitables.util import TableJSONEncoder


class Field(object):
    """
    Field within a table row
    attributes:
     - raw(mwparserfromhell.nodes.Node) - Unparsed field Wikicode
     - value(str) - Parsed field value as string
    """
    def __init__(self, node, value, attrs={}):
        self.raw = node
        self.value = value
        self.attrs = attrs

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __json__(self):
        return self.value


class Row(dict):
    """
    Single WikiTable row, mapping a field name(str) to wikitables.Field obj
    """
    def __init__(self, name, node):
        self.name = name
        self.raw = node

    def json(self):
        return json.dumps(self, cls=TableJSONEncoder)

    @property
    def is_null(self):
        for k,f in self.items():
            if f.value != '':
                return False
        return True
