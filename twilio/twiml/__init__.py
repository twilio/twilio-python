import xml.etree.ElementTree as ET


def lower_camel(string):
    result = "".join([x.title() for x in string.split('_')])
    if not result:
        return result

    return result[0].lower() + result[1:]


class TwiMLException(Exception):
    pass


class TwiML(object):
    """
    Twilio basic verb object.
    """
    MAP = {
        'from_': 'from'
    }

    def __init__(self, **kwargs):
        self.name = self.__class__.__name__
        self.value = None
        self.verbs = []
        self.attrs = {}

        for k, v in kwargs.items():
            if v is not None:
                self.attrs[lower_camel(self.MAP.get(k, k))] = v

    def __str__(self):
        return self.to_xml()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def to_xml(self, xml_declaration=True):
        """
        Return the contents of this verb as an XML string

        :param bool xml_declaration: Include the XML declaration. Defaults to
                                     True
        """
        xml = ET.tostring(self.xml()).decode('utf-8')

        if xml_declaration:
            return '<?xml version="1.0" encoding="UTF-8"?>' + xml
        else:
            return xml

    def append(self, verb):
        """
        Add a TwiML doc
        :param verb: TwiML Document
        :return:
        """
        if not isinstance(verb, TwiML):
            raise TwiMLException('Only appending of TwiML is allowed')

        self.verbs.append(verb)
        return self

    def xml(self):
        """
        Convert to XML
        :return: Generated TwiML
        """
        el = ET.Element(self.name)

        keys = self.attrs.keys()
        keys = sorted(keys)
        for a in keys:
            value = self.attrs[a]

            if isinstance(value, bool):
                el.set(a, str(value).lower())
            else:
                el.set(a, str(value))

        if self.value:
            el.text = self.value

        for verb in self.verbs:
            el.append(verb.xml())

        return el
