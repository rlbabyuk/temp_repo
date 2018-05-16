from driver import Driver


class WebElement(object):
    FIND_ELEMENT = ['name',
                    'tag_name',
                    'id',
                    'xpath',
                    'ccs_selector',
                    'class_name',
                    'link_text',
                    'partial_link_text'
                    ]

    def __init__(self, **kwargs):
        self.driver = Driver().driver
        if kwargs:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    @property
    def element_active_attribute(self):
        for att in self.FIND_ELEMENT:
            try:
                self.__getattribute__(att)
                return att
            except AttributeError:
                # Todo use logger here
                 print("Element doesn't have {} attribute".format(att))

    def element(self):

        action = "find_element_by_{}".format(self.element_active_attribute)
        action_function = self.driver.__getattribute__(action)

        return action_function(self.__getattribute__(self.element_active_attribute))

    def elements(self):
        action = "find_elements_by_{}".format(self.element_active_attribute)
        action_function = self.driver.__getattribute__(action)

        return action_function(self.__getattribute__(self.element_active_attribute))


