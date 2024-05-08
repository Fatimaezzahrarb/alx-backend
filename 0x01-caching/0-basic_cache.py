#!/usr/bin/env python3

'''Task zero: Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and is the caching system
    '''

    def put(self, key, item):
        '''assign to dictionary `self.cache_data` the
           `item` value for key `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return value in `self.cache_data` linked to `key`
        '''

        return self.cache_data.get(key, None)