from flask import Flask, render_template,redirect,request
import random

#app name Lol!
app = Flask(__name__)

contador = 0
sum = 1

#route LOL!

@app.route("/")
def dude():
    return render_template("index.html",contador = contador)



@app.route("/totally_real_robux")
#what is show loL!
def casa():

    return '''

Hi there. <br> <br> <br> 

<button onclick="window.location.href = '/virus'"> clickity click me for FREE ROUS :money_mouth_face: </button>

'''

@app.route('/cookie')

def yourmom():
  global contador
  global sum
  contador = contador + sum
  
  
  

  return redirect('/')

@app.route('/cookie_upgrade')

def yourupgrade():
  global sum
  global contador
  if contador > 9:
   sum = sum + 1
   contador = contador - 10
  
  
  return redirect('/')

@app.route('/cookie_superupgrade')

def yoursuperupgrade():
  global sum
  global contador
  if contador > 19:
   sum = sum + 5
   contador = contador - 20
  
  

  return redirect('/')

@app.route('/cookie_ultraupgrade')

def yourultraupgrade():
  global sum
  global contador
  
  if contador > 49:
   sum = sum + 10
   contador = contador - 50
  
  

  return redirect('/')

@app.route('/cookie_cheat')

def cheat():
  global sum
  global contador
  
  
  sum = sum + 9999999999999999
  contador = contador - 0
  
  

  return redirect('/')

@app.route('/cookie_bestupgrade')

def yourBESTupgrade():
  global sum
  global contador
  if contador > 999:
   sum = sum + 99999
   contador = contador - 1000
  if contador < 999:
    print("GETOUT!!")
  

  return redirect('/')


@app.route('/yeah')

def yup():
    return 'yup'







@app.route('/virus')

def jorje():
  for i in range(7):
    with open("SUPER DUPER EVIL virus number " + str(i) + ".txt","w") as archivo:

        #contenido

        archivo.write("hello")
    return '''

   why did you trust me...... now theres a SUPER DUPER EVIL virus in your FOLDER.

    '''



@app.route('/HelloThere',methods=["GET","POST"])  
def hibro():
 
 nombre = request.form.get("pedro")






 return "Welcome to the Ass Gore Fanclub, " + str(nombre) + "!"

@app.route('/bday',methods=["GET","POST"])
def wahwah2():
  birth = request.form.get("birth")
  years = request.form.get("years")
  
  
  texto = "Acuerdo a esto, el año es " + str(birth) + str(years) +"!"

  return texto

@app.route('/69finder')
def wahwah654():
  number = random.randint(-10000,10000)
  text = "Number #" + str(number)
  
  while number != 69:
    number = random.randint(-10000,10000)
    text = text + " Number #" + str(number)
  
  return text

@app.route('/result',methods=["GET","POST"])
def onetwothreeonetwothreeonetwoonetwooneoh():
  number = request.form.get("roblox")
  guess = random.randint(1,11)

  



  if str(guess) == number:
    return "Your number is... " + str(guess) + "!!" 
  if str(guess) <= number:
    return "Your number is... " + str(guess) + "... wait, what do you mean it's not your number?"
  if str(guess) >= number:
    return "Your number is... " + str(guess) + "... wait, what do you mean it's not your number?"

@app.route('/LETSGOGAMBLING',methods=["GET","POST"])
def whatareyouTALKINGabout():
  Guess = request.form.get("Indexer")
  Gamble = random.randint(1,12)
  money = 100
  if str(Guess) == str(Gamble):
    money = money + 10000
    money = money - 20
    return "yay you won the lotery"
  if str(Guess) != str(Gamble):
    money = money - 20
    return "aw dang dude try harder next time"

@app.route('/GamblingALT')
def Gamblin():
  Money = 600
  randNumber = random.randint(1,6)

  if str(randNumber == 6):
    Money = Money + random.randint(200,700)
    Money = Money - 100
    return "yay you won the lottery, you have " + str(Money) + " dollars now!!"
  if str(randNumber != 6):
    Money = Money - 100
    return "aw dang it! you lost the lottery, you have " + str(Money) + " dollars now"



#run the app lOL!

app.run(host)

