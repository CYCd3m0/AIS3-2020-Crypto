import requests, string
from padding_oracle import *

PHPSESSID = 'f4cf346c027a189a3af9d6b730052821'
CSRF_TOKEN = '1vgADumihlx+6eWyEdI6pIRP4zXaXhl9DxSDJNXJ32LNdTJbM4gwB4THhpS1hwjgKZOd8ATDPY6c661TDVn8+OOhy33aQb6wd01rauFSD3bGFvgpZ1WQQ10s+fOjlrGP'

sess = requests.Session()
sess.cookies.set('PHPSESSID', PHPSESSID)

def test_if_it_is_decrypted_successfully(c):
    res = sess.post('https://turtowl.ais3.org/?action=login', data={'csrf_token': base64_encode(c)})
    return 'token decryption failed' not in res.text

padding_oracle(base64_decode(CSRF_TOKEN), block_size=16, oracle=test_if_it_is_decrypted_successfully, num_threads=8, chars=string.printable)

# flag = AIS3{5l0w_4nd_5734dy_w1n5_7h3_r4c3.}
# ref : https://github.com/djosix/AIS3-2020-Pre-Exam#turtle-crypto