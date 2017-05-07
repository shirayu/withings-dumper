#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dump withings data
"""

import argparse
import json
import sys
import codecs
from withings import WithingsAuth, WithingsApi, WithingsCredentials


def init(cfg):
    '''
    Get values to be set
    '''
    auth = WithingsAuth(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
    authorize_url = auth.get_authorize_url()
    print("Go to %s allow the app and copy your oauth_verifier" % authorize_url)

    oauth_verifier = input('Please enter your oauth_verifier: ')
    creds = auth.get_credentials(oauth_verifier)

    print("OAUTH_TOKEN\t%s" % creds.access_token)
    print("OAUTH_VERIFIER\t%s" % creds.access_token_secret)
    print("CONSUMER_KEY\t%s" % creds.consumer_key)
    print("CONSUMER_SECRET\t%s" % creds.consumer_secret)
    print("USER_ID\t%s" % creds.user_id)


def get_data(cfg, startdate, enddate):
    '''
    Get data and print
    '''
    creds = WithingsCredentials(
        cfg['OAUTH_TOKEN'],
        cfg['OAUTH_VERIFIER'],
        cfg['CONSUMER_KEY'],
        cfg['CONSUMER_SECRET'],
        cfg['USER_ID'])
    client = WithingsApi(creds)
#     measures = client.get_measures(limit=1)

    measures = None
    if (startdate is not None) and (enddate is not None):
        measures = client.get_measures(startdate=startdate, enddate=enddate)
    else:
        measures = client.get_measures()

    outs = []
    for measure in measures:
        data = {}
        data["raw"] = measure.data
        data["weight"] = measure.weight
        data["fat_free_mass"] = measure.fat_free_mass
        data["fat_ratio"] = measure.fat_ratio
        data["fat_mass_weight"] = measure.fat_mass_weight
        outs.append(data)
    return outs


def main():
    '''
    main
    '''

    oparser = argparse.ArgumentParser()
    oparser.add_argument("--init", dest="init", default=False, action="store_true")
    oparser.add_argument("--startdate", dest="startdate", default=None)
    oparser.add_argument("--enddate", dest="enddate", default=None)
    oparser.add_argument("-c", "--config", dest="config", default=None, required=True)
    oparser.add_argument("-o", "--output", dest="output", default="-")
    opts = oparser.parse_args()

    cfg = None
    with open(opts.config) as fhdl:
        cfg = json.loads(fhdl.read())

    if opts.init:
        init(cfg)
        return

    outs = get_data(cfg, opts.startdate, opts.enddate)
    if outs:  # When not empty, write
        outf = None
        if opts.output == "-":
            outf = sys.stdout
        else:
            outf = codecs.open(opts.output, "w", "utf8")

        for data in outs:
            json.dump(data, outf, ensure_ascii=False)
            outf.write("\n")

if __name__ == '__main__':
    main()
