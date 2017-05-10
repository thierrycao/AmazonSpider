from cowpy import cow


class myCowpy:
    def cow_style(self,msg):
        msg = cow.milk_random_cow(msg)
        return msg

    @property
    def cowpyFactory(self):
        msg = 'hh'
        msg = self.cow_style(msg)
        return msg