"""
IxLoad package tests that can run in offline mode.

@author yoram@ignissoft.com
"""

from os import path

from ixload.test.test_base import IxlTestBase


class IxlTestOffline(IxlTestBase):

    def testLoadConfig(self):
        """ Test configuration load. """
        self.logger.info(IxlTestOffline.testLoadConfig.__doc__)

        self._load_config(path.join(path.dirname(__file__), 'configs/test_config.rxf'))
        print(self.ixl.repository.get_elements())

        self._save_config()

    def testGetSet(self):
        """ Test get/set operations. """
        self.logger.info(IxlTestOffline.testLoadConfig.__doc__)

        self._load_config(path.join(path.dirname(__file__), 'configs/test_config.rxf'))
        print '+++'
        print self.ixl.api.get_children(self.ixl.api.session_url)
        ixload_url = self.ixl.api.get_children(self.ixl.api.session_url, 'ixload')[0]
        print self.ixl.api.get_children(ixload_url)
        test_url = self.ixl.api.get_children(ixload_url, 'test')[0]
        print self.ixl.api.get_children(test_url)
        activeTest_url = self.ixl.api.get_children(test_url, 'activeTest')[0]
        print self.ixl.api.get_children(activeTest_url)
        timelineList_url = self.ixl.api.get_children(activeTest_url, 'timelineList')[0]
        print self.ixl.api.get_children(timelineList_url)
        docs_url = self.ixl.api.get_children(timelineList_url, 'docs')[0]
        print self.ixl.api.get_children(docs_url)
        print self.ixl.api.cget(timelineList_url)
        print self.ixl.api.cget(timelineList_url, 'iterations')
        self.ixl.api.config(timelineList_url, iterations=2)
        print self.ixl.api.cget(timelineList_url, 'iterations')
        print '+++'
