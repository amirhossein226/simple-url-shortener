from bddrest import response, when, status, given
import hashlib
import re
from tools import url_list

def test_shortener(Given):
    base_url = 'http://localhost:8080/'
    ret_val_patt = r'http://localhost:8080/[a-zA-Z0-9]{8}'
    with Given('/url_shortener/',verb='post', form={'url': 'http://www.google.com/foo/bar/baz'}):
        assert status == 200
        assert re.match(ret_val_patt, response.text)
        assert len(list(url_list.items())) == 2 


        when()
        assert len(list(url_list.items())) == 2 

        when(form=given - 'url')
        assert status == 400
        
        when(form='')
        assert status == 400 
        
        when(verb='')
        assert status == "405 Method Not Allowed"
        
    with Given(f'/{list(url_list.keys())[0]}'):
        assert status == 301
            
        when('/sjfsdljfklj')
        assert status == 404
        
        when('/ssssssss')
        assert status == 404
