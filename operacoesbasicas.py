a=int (input("Digite o primeiro valor: "))
b=int (input("Digite o segundo valor: "))
op=int (input("(1)Soma\n(2)Subtração\n(3)Multiplicação\n(4)Divisão\nEscolha a operação: "))

match op:
    case 1:
        print("Resultado da soma: ",a+b)
    case 2:
        print("Resultado da subtração: ",a-b)
    case 3:
        print("Resultado da multiplicação: ",a*b)
    case 4:
        if b==0:
            print("Impossivel realizar divisão por zero")
        else:
            print("Resultado da divisão: ",a/b)

