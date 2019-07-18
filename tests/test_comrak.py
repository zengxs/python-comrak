import json
import urllib.request
from os.path import abspath, dirname, join

from comrak import *


def _get_file(name, suffix):
    base_dir = join(dirname(__file__), 'data')
    with open(join(base_dir, f'{name}.{suffix}')) as file:
        return file.read()


def _get_markdown(name):
    return _get_file(name, 'md')


def _get_html(name):
    return _get_file(name, 'html')


def test_commonmark_spec():
    spec_url = 'https://spec.commonmark.org/0.29/spec.json'
    req = urllib.request.Request(url=spec_url, method='GET')
    res = urllib.request.urlopen(req)
    text = res.read().decode('utf-8')
    testcases = json.loads(text)
    for testcase in [x for x in testcases if x['section'] != 'Autolinks']:
        markdown = testcase['markdown']
        html = testcase['html']
        assert markdown_to_html(markdown, COMRAK_UNSAFE_HTML) == html


def test_gfm_table():
    name = 'gfm-table'
    md = _get_markdown(name)
    excepted = _get_html(name)
    assert markdown_to_html(md, COMRAK_EXT_TABLE) == excepted
