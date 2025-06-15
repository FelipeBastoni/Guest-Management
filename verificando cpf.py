a = input("Cpf:")

b = list(map(int, a))
print(b)

c = ((b[0]*10) + (b[1]*9) + (b[2]*8) + (b[3]*7) + (b[4]*6) + (b[5]*5) + (b[6]*4) + (b[7]*3) + (b[8]*2))%11

d = 11-c


if d >= 10:

    f = 0

    if f == b[9]:

        print("OK")             

        g = ((b[0]*11) + (b[1]*10) + (b[2]*9) + (b[3]*8) + (b[4]*7) + (b[5]*6) + (b[6]*5) + (b[7]*4) + (b[8]*3) + (b[9]*2))%11 
        
        h =  11-(g-1)
        print(g, h)

        if h == b[10]:

            print("Cpf Valido")




    else: 

        print("está errado")


else: 

    print("cpf invalido")



if d<10:

    if d == b[9]:

        i = ((b[0]*11) + (b[1]*10) + (b[2]*9) + (b[3]*8) + (b[4]*7) + (b[5]*6) + (b[6]*5) + (b[7]*4) + (b[8]*3) + (b[9]*2))%11
        j = 11-i
        print(i)


        if j == b[10]:

            print("CPF valido")



        else:

            print("Cpf invalido")


    else: 

        print("Cpf invalido")


