'''Utility functions for the project'''
import hashlib


def HashApiKey(apiKey):
    enc = hashlib.sha256()
    enc.update(apiKey.encode('utf-8'))
    return str(enc.digest())
