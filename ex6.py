
def AT():
    sum = 0
    if alg('test1.txt') == 'Yes':
        sum += 1
    if alg('test2.txt') == 'Now':
        sum += 1
    if alg('test3.txt') == 'Now':
        sum += 1

    if sum == 3:
        print('Autotest passed!\n')
        return
    else:
        print('Autotest failled!\n')
        return








def alg(filename):
    a = 0
    b = 0
    n = 0
    n_plus_1 = 0
    q1 = 0
    q2 = 0
    flag = 0
    sgn = 1
    try:
        with open(filename, 'r') as file:
            it = file.read(1)
            if it == '-':
                sgn = -1
                it = file.read(1)
            if it != '-':    
                a = a * 10 + sgn*int(it)
                sng = 1
            
            while it:
                it = file.read(1)
                if it == ' ' or it == '\n' or it == '':
                    n = n_plus_1
                    n_plus_1 = a
                    if n != 0:
                        if n*n_plus_1 > 0:
                            return 'Now'
                    else:
                        if flag != 0:
                            file.close() 
                            return 'Now'
                        flag = 1                
                    
                    a = 0
                    sgn = 1
                if it != ' ' and it != '\n' and it != '':
                    if it == '-':
                        sgn = -1
                    if it != '-':                     

                       a = a * 10 + sgn*int(it)
    except IOError:
       print("File not accessible")
                       
    file.close()               
    return 'Yes'



AT()
name = input('Enter name of file\n')

print(alg(name))
