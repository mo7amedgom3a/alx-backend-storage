#!/usr/bin/env python3
""" 8-main """
from connection import *
list_all = __import__('8-all').list_all



if __name__ == "__main__":

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))