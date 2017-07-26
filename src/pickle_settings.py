__author__ = 'CGT'
import pickle
import logging

logger = logging.getLogger(__name__)


def load_settings(key='Default'):
    try:
        with open('settings.pk', 'rb') as f:
            data = pickle.load(f)
        if key in data.keys():
            settings = data[key]
        else:
            logger.warning('Settings with key %s not found in file. Opening Default settings', type)
            settings = data['Default']
        return settings
    except IOError:
        logger.error('Cannot find settings.pk')