import unittest2
import beiceshi_model
class mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testsum(self):
        self.assertEqual(beiceshi_model.sum(1,2),2,'test sum fail')
    def testsub(self):
        self.assertEqual(beiceshi_model.sub(2,1),1,'test sub fail')
if __name__ =='__main__':
    unittest.main()