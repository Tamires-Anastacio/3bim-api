from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def raizu():
    return {'mensagem': 'Minha primeira API em FastAPI!'}

@app.get('/sobre')
def sobre():
    return {'mensagem': 'PÁGINA SOBRE O SITE!'}