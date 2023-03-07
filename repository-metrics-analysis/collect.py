#!/usr/bin/env python3

import traceback
import time
import sys

import requests
import json
from lxml import etree


# Script for collecting metadata from repositories with open-search interface
# and outputting it as newline-delimited JSON. See also instructions in
# https://www.kiwi.fi/pages/viewpage.action?pageId=45782169
# Start page be can given in command line argument, default is 0.
#
# Usage example: ./collect.py https://trepo.tuni.fi/ 2000 > trepo.ndjson 2> trepo.log


url_base = sys.argv[1].strip("/")


def get_from_item(spec):
    elem = item.xpath(spec)
    return elem[0].text if (elem and elem[0].text is not None) else ""


headers = {"User-Agent": "Annif-analysis-collect"}
start = int(sys.argv[2]) if len(sys.argv) == 3 else 0
rpp = 100  # results per page
cnt = 0
while True:
    url_query = (
        # f"/open-search/?query=*&sort_by=3&order=desc&start={start}&rpp={rpp}&format=kkf"
        f"/open-search/?query=*&sort_by=3&order=asc&start={start}&rpp=100&format=kkf"
    )
    url = url_base + url_query
    print(f"Request {cnt}, performing call with url {url}", file=sys.stderr)
    try:
        resp = requests.get(url, headers=headers)
    except Exception as e:
        print(traceback.format_exc(), file=sys.stderr)
        print("Waiting for 10 seconds before retrying...", file=sys.stderr)
        time.sleep(10)
    else:
        try:
            xml_string = resp.text
            root = etree.fromstring(bytes(xml_string, encoding="utf8"))
            if len(root.xpath("//item")) == 0:
                print("No records received, all done.", file=sys.stderr)
                break
            for item in root.xpath("//item"):
                my_dict = {
                "title": get_from_item('metadata[@element="title"]'),
                "id": get_from_item(
                    'metadata[@element="identifier" and @qualifier="uri"]'
                ),
                "lang": get_from_item('metadata[@element="language"]'),
                "type": get_from_item(
                    'metadata[@element="type"]'
                ),
                "type_level": get_from_item(
                    'metadata[@element="type" and @qualifier="ontasot"]'
                ),
                "faculty": get_from_item(
                    'metadata[@element="contributor" and @qualifier="faculty"]'
                ),
                "discipline": get_from_item(
                    'metadata[@element="subject" and @qualifier="discipline"]'
                ),
                "degreeprogram": get_from_item(
                    'metadata[@element="subject" and @qualifier="degreeprogram"]'
                ),
                "date_accessioned": get_from_item(
                    'metadata[@element="date" and @qualifier="accessioned"]'
                ),
                "date_issued": get_from_item(
                    'metadata[@element="date" and @qualifier="issued"]'
                ),
                "suggestions": get_from_item('metadata[@element="suggestions"]').split(
                    "|"
                ),
                "subjects_yso": [
                    s.text
                    for s in item.xpath(
                        'metadata[@element="subject" and @qualifier="yso"]'
                    )
                ],
                "subjects_none": [
                    s.text
                    for s in item.xpath(
                        'metadata[@element="subject" and @qualifier=""]'
                    )
                ],
                "subjects_all": [
                    s.text for s in item.xpath('metadata[@element="subject"]')
                ],
                }
                # print data as json object
                print(json.dumps(my_dict))
        except Exception as e:
            print(traceback.format_exc(), file=sys.stderr)
            print("Failed parsing, continue to next page.", file=sys.stderr)

        start += rpp
    cnt += 1
    time.sleep(5)
    # if cnt >= 0:
    #     break
