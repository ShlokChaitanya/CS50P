from fpdf import FPDF

class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.generate()

    @classmethod
    def get(cls):
        return cls(input("Name: ").strip())

    def generate(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font("Helvetica", "B", size=50)
        pdf.cell(0, 50, txt="CS50 Shirtificate", align="C", ln=True)

        pdf.image("shirtificate.png", x=5, y=80, w=200)

        pdf.set_font("Helvetica", "B", size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 180, align="C", txt=f"{self.name} took CS50")

        pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    Shirtificate.get()
