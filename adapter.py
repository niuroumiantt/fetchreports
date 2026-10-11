"""LBNL native publication metadata/method; does not pretend to read the PDF."""
import re
from helpers import html, candidate, date


def extract(data, source, original, sampled_at):
    p = html(data)
    sentence = re.search(r'This report, designed.*?historical shipment data\.', p.text)
    published = re.search(r'Date Published (\d{2})/(\d{2})/(\d{4})', p.text)
    if not sentence or not published or '10.71468/P1WC7Q' not in p.text:
        raise ValueError('report metadata/method not found')
    return [candidate('study', source['title'], {'DOI': '10.71468/P1WC7Q', 'publisher': 'LBNL', 'edition': '2024'},
        'study.method', sentence[0], None,
        'US national historical datacenter electricity consumption method, publication abstract only; no per-campus allocation or quantitative PDF extraction',
        'reported', 'publication page / Abstract; method sentence', sentence[0], sentence[0],
        published=date(f'{published[3]}-{published[1]}-{published[2]}', 'day', 'Date Published on native publication page'))]
