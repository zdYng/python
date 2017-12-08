import unittest2
import beiceshi_model
class mytest(unittest2.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testsum(self):
        self.assertEqual(beiceshi_model.sum(1,2),3)

if __name__ =='__main__':
    unittest2.main()
