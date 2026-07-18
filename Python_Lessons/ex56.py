sal = float(input("Digite o salário: "))

if sal <= 1621.00:
    desc0 = (7.5*sal)/100  #inss
    desc1 = sal - desc0    #inss
elif 1621.00 < sal <= 2902.84:
    desc0 = (9*sal)/100   #inss
    desc1 = sal - desc0   #inss
elif 2902.84 < sal <= 4354.27:
    desc0 = (12*sal)/100   #inss
    desc1 = sal - desc0    #inss
else:
    desc0 = (14*sal)/100   #inss
    desc1 = sal - desc0    #inss

base_ir = sal - desc0

if base_ir <= 2112:
    ir = 0
elif base_ir <= 2826:
    ir = (base_ir *0.075) - 158.40
elif base_ir <= 3751:
    ir = (base_ir * 0.15) - 370.40
elif base_ir <= 4664:
    ir = (base_ir * 0.225) - 651.73
else:
    ir = (base_ir * 0.275) - 884.96

total = sal - desc0 - ir

print ("Seu salário é: {:.2f}".format(sal))
print ("Seu INSS é: {:.2f}".format(desc0))
print ("Seu IR é: {:.2f}".format(ir))
print ("Seu salário com todos os desconto é de {}".format(total))