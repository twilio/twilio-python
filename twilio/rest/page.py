import urlparse


class Page(object):
    def __init__(self, domain, pager, instance, instance_kwargs, previous_page_uri, next_page_uri,
                 records):
        self._domain = domain
        self._pager = pager
        self._instance = instance
        self._instance_kwargs = instance_kwargs
        self._previous_page_uri = previous_page_uri
        self._next_page_uri = next_page_uri
        self._records = iter(records)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        return self._instance(self._domain, next(self._records), **self._instance_kwargs)

    def next_page(self):
        if not self._next_page_uri:
            return None

        kwargs = urlparse.parse_qs(urlparse.urlparse(self._next_page_uri).query)
        return self._pager.page(**kwargs)

    def previous_page(self):
        if not self._previous_page_uri:
            return None

        kwargs = urlparse.parse_qs(urlparse.urlparse(self._previous_page_uri).query)
        return self._pager.page(**kwargs)

    def __repr__(self):
        return '<Page {}>'.format(self._instance)


