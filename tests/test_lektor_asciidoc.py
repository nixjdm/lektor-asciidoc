import os


def test_basic(pad, builder):
    failures = builder.build_all()
    assert not failures
    page_path = os.path.join(builder.destination_path, 'index.html')
    html = open(page_path).read()
    assert '<h2 id="_header_1">Header 1</h2>' in html
    assert '<pre>code here</pre>' in html
