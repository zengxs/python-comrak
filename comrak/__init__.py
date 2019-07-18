from comrak._comrak import py_markdown_to_html, PyComrakOption

COMRAK_UNSAFE_HTML = 'unsafe'
COMRAK_EXT_AUTOLINK = 'ext_autolink'
COMRAK_EXT_GFM_TABLE = 'ext_gfm_table'

COMRAK_EXT_TABLE = COMRAK_EXT_GFM_TABLE


def markdown_to_html(md, *extensions):
    """
    Convert markdown to html
    :param str md: Markdown text
    :param list[str] extensions: Enable extensions
    :returns: str
    """
    o = PyComrakOption()
    for ext in extensions:
        o.enable(ext)
    return py_markdown_to_html(md, o)
