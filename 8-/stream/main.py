from create import create_equation
from decoding import decode
from encoding import encode
from addition import addition

if __name__ == '__main__':
    equation1 =  create_equation()
    equation2 = create_equation()
    print(decode(equation1))
    print(decode(equation2))
    print(decode(addition(equation1, equation2)))
    
    
