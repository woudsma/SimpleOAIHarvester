#! /usr/bin/env python

import argparse, sys
from urllib2 import HTTPError
from oai import *

parser = argparse.ArgumentParser(description='OAI Identify verb.')
parser.add_argument('baseUrl', help='The baseUrl of the OAI repository.')

args = parser.parse_args()


if __name__ == "__main__":
    print parser.description
    try:
        xml = identify(args.baseUrl)
    except (OAIException, HTTPError) as err:
        print err
        sys.exit(1)

    parsedUrl = parseUrl(args.baseUrl)
    save(xml, filename=parsedUrl.netloc + "-identify")
