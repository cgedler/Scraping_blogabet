# Created on : Feb 5, 2024, 7:19:48 PM
# Author     : Christopher Gedler


# This is a class for store GRADED PICKS information.


class Pick:
    
    def __init__(self, param1, param2, param3):
        self.pick_line = param1  
        self.feed_odd = param2
        self.data_original_title = param3
            
    def __str__(self):
        elements = 'pick-line {}, feed_odd {}, {} ruedas, {}cc'
        return elements.format(self.pick_line, self.feed_odd, self.data_original_title)