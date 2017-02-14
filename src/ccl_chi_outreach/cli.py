"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mccl_chi_outreach` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``ccl_chi_outreach.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``ccl_chi_outreach.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import atexit
import json
import logging
import logging.config
import os
import pprint

import click
import tablib
import time
import yaml
from googleplaces import GooglePlaces, GooglePlacesSearchResult

# # TODO get rid of this dependency sometime after I'm done with high-churn experimenting
# # probably get rid of the whole memoization subclass too...
# # I don't really want to leave Pickle in here as a dependency.
# import percache
# cache = percache.Cache('/tmp/ccl_chi_outreach')
# atexit.register(cache.close)
#
#
# class GooglePlacesWithMemoization(GooglePlaces):
#
#     @cache
#     def nearby_search(self, *args, **kwargs):
#         return super(GooglePlacesWithMemoization, self).nearby_search(*args, **kwargs)
#
#     @cache
#     def text_search(self, *args, **kwargs):
#         return super(GooglePlacesWithMemoization, self).text_search(*args, **kwargs)


@click.command()
@click.option(
    '--configpath', default='./ccl_chi_outreach.yaml', help='Path to configuration file including API Key etc.')
def main(configpath):
    # TODO today I'm just throwing this together for the CCL team... one big dumb function ... TODO refactor a lot

    with open(configpath, 'r') as f:
        config = yaml.load(f)
    logging.config.dictConfig(config['logging'])
    logger = logging.getLogger() # TODO should this be (__name__) or just (), I always forget

    # TODO refactor a fn to do "get-and-redact then assert all nodes of api_keys config are redacted"
    api_key_google_places = config['api_keys']['google_places']
    config['api_keys']['google_places'] = "<REDACTED>"
    api_key_boundaries = config['api_keys']['boundaries_chicago']
    config['api_keys']['boundaries_chicago'] = "<REDACTED>"

    for key, value in config['data_static'].items():
        config['data_static'][key] = os.path.expanduser(os.path.expandvars(value))

    logger.debug("config - evaluated, but API keys hidden: \n%s", json.dumps(config, indent=2))

    # google_places = GooglePlacesWithMemoization(api_key_google_places)
    google_places = GooglePlaces(api_key_google_places)

    start = time.time()
    result = google_places.nearby_search(location="12th Ward, Chicago, IL", radius=10)
    end = time.time()
    duration = end - start
    logger.info("Got %s and it took this much time: %s", result, duration)

    # cache.close()
