

from task3 import dublicate_names

import pytest,re

class TestPytest:

    def test_class(self):
       assert type(dublicate_names()) ==  list

    def test_qty(self):
        assert len(dublicate_names()) == 4


    @pytest.mark.parametrize('x',[0,1,2,3])

    def test_regex(self,x):
        res = dublicate_names()[x]
        pattern ="Александр"
        assert bool(re.findall(pattern, res)) == True

