from time import sleep

class Foo(object):
    def __init__(self):
        pass


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        sleep(0.05)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        sleep(0.1)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
