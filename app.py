
from fpdf import FPDF
from os import system

try:
    projeto = str(input("Digite a descrição do projeto:\n >>> "))
    horas_previstas = int(input("Digite o total de horas estimadas:\n >>> "))
    valor_hora = float(input("Digite o valor por hora trabalhada:\n >>> "))
    prazo = str(input("Digite o prazo estimado para conclusão:\n >>> "))

except ValueError:
    system("cls")
    print("Não foi possível registrar informação.\nTente novamente:\n")

    while True:
        try:
            projeto = str(input("Digite a descrição do projeto:\n >>> "))
            horas_previstas = int(input("Digite o total de horas estimadas:\n >>> "))
            valor_hora = float(input("Digite o valor por hora trabalhada:\n >>> "))
            prazo = str(input("Digite o prazo estimado para conclusão:\n >>> "))
            break
        
        except ValueError:
            system("cls")
            print("Não foi possível registrar informação.\nTente novamente:\n")

valor_total = horas_previstas * valor_hora

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", 0, 0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, str(horas_previstas))
pdf.text(115, 175, "{:.2f}".format(valor_hora))
pdf.text(115, 190, str(prazo))
pdf.text(115, 205, "{:.2f}".format(valor_total))

pdf.output("Orçamento.pdf")
print("\nOrçamento criado com sucesso!")
