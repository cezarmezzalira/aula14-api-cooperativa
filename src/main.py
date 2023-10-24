import json
from fastapi import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()

registros = []


@app.get("/")
def health_check():
    return {"status": "ok"}


# POST /registros
@app.post("/registros")
async def criar_registro(request: Request):
    # Recupera o body
    body = await request.body()
    # Converte para dictionary
    body = dict(json.loads(body))

    # Criamos uma variável de controle
    registro_existe = False
    # Percorremos a lista procurando se existe um registro
    # com a mesma placa
    for registro in registros:
        # Se existir, atualiza a variável de controle e para o loop
        if (registro.get("placa_veiculo") == body.get("placa_veiculo")):
            registro_existe = True
            break
    # Se existir um registro, vai retornar uma mensagem
    if (registro_existe):
        content = json.dumps({"mensagem": "Caminhão já está no pátio"})
        return Response(content=content,
                        status_code=400,
                        media_type="application/json")

    body["data_hora_entrada"] = datetime.now()

    registros.append(body)
    return body


# GET /registros
@app.get("/registros")
def listar():
    return {"registros": registros}

# PATCH /registros/:placa/finalizar


@app.patch("/registros/{placa}/finalizar")
async def finalizar(placa: str, request: Request):
    # Recupera o body
    body = await request.body()
    # Converte para dictionary
    body = dict(json.loads(body))

    # Criamos uma variável de controle
    registro_existe = None

    # Percorremos a lista procurando se existe um registro
    # com a mesma placa
    for registro in registros:
        # Se existir, atualiza a variável de controle e para o loop
        if (registro.get("placa_veiculo") == placa):
            registro_existe = registro
            break

    # Se existir um registro, vai retornar uma mensagem
    if (not registro_existe):
        content = json.dumps({"mensagem": "Caminhão não encontrado"})
        return Response(content=content,
                        status_code=404,
                        media_type="application/json")

    # Obtenho o peso final
    peso_final = body.get("peso_final", 0)

    indice = registros.index(registro_existe)

    registros[indice]["data_hora_final"] = datetime.now()
    registros[indice]["peso_final"] = peso_final
    registros[indice]["peso_carga"] = registros[indice]["peso_bruto"] - peso_final

    return registros[indice]


# DELETE /registros/:placa
@app.delete("/registros/{placa}")
def delete(placa: str):
    # Percorremos a lista procurando se existe um registro
    # com a mesma placa
    for registro in registros:
        # Se existir, atualiza a variável de controle e para o loop
        if (registro.get("placa_veiculo") == placa):
            registro_existe = registro
            break

    # Se existir um registro, vai retornar uma mensagem
    if (not registro_existe):
        content = json.dumps({"mensagem": "Caminhão não encontrado"})
        return Response(content=content,
                        status_code=404,
                        media_type="application/json")

    registros.remove(registro_existe)

    Response(content=None,
             status_code=203,
             media_type="application/json")
