from .base_object import BaseButtonElement, BaseElement


class ToolBox(BaseElement):

    def __init__(self, driver):
        super().__init__(driver=driver, selector='[data-id="tools-panel-header"]')
        self.my_powtoon_item = BaseButtonElement(selector='[data-id="image-overlay"]', driver=self.driver)


class WorkSpace:

    def __init__(self, driver, validate=True):
        self.capture_button = BaseButtonElement(selector='[data-id="capture-featured-tile"]', driver=driver)
        self.toolbox = ToolBox(driver=driver)
        self.driver = driver
        if validate:
            assert 'new-dashboard' in driver.current_url
