from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["Hadisch versie 2b.pdf", "Hadisch.pdf"]:
    merger.append(pdf)

merger.write("Hadisch Uitleg.pdf")
merger.close()