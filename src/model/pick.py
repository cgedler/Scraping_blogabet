# Created on : Feb 5, 2024, 7:19:48 PM
# Author     : Christopher Gedler


# This is a class for store PICKS information.


class Pick:
    
    def __init__(self, url, picks, profit, yields, followers):
        self._url = url
        self._picks = picks  
        self._profit = profit
        self._yields = yields
        self._followers = followers
            
    def __str__(self):
        elements = 'URL: {}, Picks: {}, Profit: {},  Yields: {}, Followers: {}'
        return elements.format(self._url, self._picks, self._profit, self._yields, self._followers)