from flask import Flask,render_template,request

app = Flask (__name__)

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        valor = request.form['valor']
        unidad = request.form['unidad']
        # # aquí puedes implementar la lógica para realizar la conversión
        if valor=="" or unidad==None:
             return render_template("index.html", dolar=0, euro=0, pesos=0, yen=0 , dinar=0, libra=0)
        elif unidad=="dolar":
            valor=int(valor)
            dolar = valor
            euro = round(valor*0.94,2)
            pesos= round(valor*4823.94,2)
            yen= round(valor *132.447,2)
            dinar=round(valor*0.30525,2)
            libra=round(valor*0.82174,2)
            return render_template("index.html", dolar=dolar, euro=euro, pesos=pesos, yen=yen , dinar=dinar, libra=libra)
        elif unidad=="euro":
            valor=int(valor)
            dolar = round(valor*0.94,2)
            euro = valor
            pesos= round(valor*5149.84,2)
            yen= round(valor *142.241,2)
            dinar=round(valor*0.3278,2)
            libra=round(valor*0.8825,2)
            return render_template("index.html", dolar=dolar, euro=euro, pesos=pesos, yen=yen , dinar=dinar, libra=libra)
        elif unidad=="pesos":
            valor=int(valor)
            dolar = round(valor*0.00021,2)
            euro = round(valor*0.00019,2)
            pesos= valor
            yen= round(valor *0.02754,2)
            dinar=round(valor*0.00006,2)
            libra=round(valor*0.00017,2)
            return render_template("index.html", dolar=dolar, euro=euro, pesos=pesos, yen=yen , dinar=dinar, libra=libra)
        elif unidad=="yen":
            dolar = round(valor *0.00755,2)
            euro = round(valor*0.00703,2)
            pesos= round(valor*36.2022,2)
            yen= valor
            dinar=round(valor*0.0023,2)
            libra=round(valor*0.0062,2)
            return render_template("index.html", dolar=dolar, euro=euro, pesos=pesos, yen=yen , dinar=dinar, libra=libra)
        elif unidad=="dinar":
            dolar = round(valor*3.26023,2)
            euro = round(valor*3.03551,2)
            pesos= round(valor*15634.7,2)
            yen= round(valor *431.808,2)
            dinar=valor
            libra=round(valor*2.67905,2)
            return render_template("index.html", dolar=dolar, euro=euro, pesos=pesos, yen=yen , dinar=dinar, libra=libra)
        elif unidad=="libra":
            dolar = round(valor*1.21671,2)
            euro = round(valor*1.13291,2)
            pesos= round(valor*5834,84,2)
            yen= round(valor *161.158,2)
            dinar=round(valor*0.3714,2)
            libra=valor
            return render_template("index.html", dolar=dolar, euro=euro, pesos=pesos, yen=yen , dinar=dinar, libra=libra)
    return render_template("index.html")


if __name__ =="__main__":
    app.run()