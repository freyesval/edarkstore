from fpdf import FPDF


class PDF(FPDF):
    pass
    def logo(self, name, x, y, w,h):
        self.image(name,x,y,w,h)

    def texts(self, texto):
        #with open(name,'rb') as txt:
        #    text = txt.read().decode('latin-1')
        #text = 'Esto es un texto de prueba para ver si funciona la creacion del PDF. Lorem Ipsum...'
        self.set_xy(10.0,80.0)
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial','',12)
        self.multi_cell(0, 10, texto)

    def titles(self, title):
        self.set_xy(0.0, 40.0)
        self.set_font('Arial','B',16)
        self.set_text_color(220.0, 50.0, 50.0)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)


