import mysql.connector
from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

conector = mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database='cadastrobilheteunico',
)

#Create---------------------------------------------------
@app.route('/usuario/criar',methods=['POST'])
def CriarUsuario():
	cursor = conector.cursor()
    
	novoUsuario = request.json
	comando=f'INSERT INTO usuarios (Nome, CPF, RG, DataNascimento, Telefone , Email, EndereçoResidencial, CEP, Polo, TipoBilhete, SaldoBilhete, ValidadeBilhete, CarteiraTrabalho, ComprovanteEscolar) VALUES("{novoUsuario['Nome']}", {novoUsuario["CPF"]}, {novoUsuario["RG"]}, "{novoUsuario["DataNascimento"]}", {novoUsuario["Telefone"]}, "{novoUsuario["Email"]}", "{novoUsuario["EndereçoResidencial"]}", {novoUsuario["CEP"]}, "{novoUsuario["Polo"]}", "{novoUsuario["TipoBilhete"]}", {novoUsuario["SaldoBilhete"]}, "{novoUsuario["ValidadeBilhete"]}", {novoUsuario["CarteiraTrabalho"]}, "{novoUsuario["ComprovanteEscolar"]}")'

	cursor.execute(comando)
	conector.commit()
	cursor.close()

	return make_response(
    	jsonify(
        	mensagem='Cadastro realizado com sucesso!',
        	aluno=novoUsuario
    	)
	)


#ReadTodos------------------------------------------------
@app.route('/usuario/ler',methods=['GET'])
def ConsultaUsuario():
	cursor = conector.cursor()
	comando='SELECT * FROM usuarios WHERE 1'

	cursor.execute(comando)
	Consulta = cursor.fetchall()
	cursor.close()

	Retorno = list()
	for dadoUsuario in Consulta:
		Retorno.append(
        	{
            	'Codigo': dadoUsuario[0],
            	'Nome': dadoUsuario[1],
            	'CPF': dadoUsuario[2],
				'RG':  dadoUsuario[3],
				'DataNascimento': dadoUsuario[4],
				'Telefone': dadoUsuario[5],
				'Email': dadoUsuario[6],
				'EndereçoResidencial': dadoUsuario[7],
				'CEP': dadoUsuario[8],
				'Polo': dadoUsuario[9],
				'TipoBilhete': dadoUsuario[10],
				'SaldoBilhete': dadoUsuario[11],
				'ValidadeBilhete': dadoUsuario[12],
				'CarteiraTrabalho': dadoUsuario[13],
				'ComprovanteEscolar': dadoUsuario[14]
        	}
    	)

	return make_response(
    	jsonify(Retorno)
	)
	

#Read------------------------------------------------------
@app.route('/usuario/lerid/<int:id>',methods=['GET'])
def ConsultaUsuarioPorId(id):
	cursor = conector.cursor()
	comando=f'SELECT * FROM usuarios WHERE codigo = "{id}"'

	cursor.execute(comando)
	Consulta = cursor.fetchall()
	cursor.close()

	Retorno = list()
	for dadoUsuario in Consulta:
		Retorno.append(
        	{
            	'Codigo': dadoUsuario[0],
            	'Nome': dadoUsuario[1],
            	'CPF': dadoUsuario[2],
				'RG':  dadoUsuario[3],
				'DataNascimento': dadoUsuario[4],
				'Telefone': dadoUsuario[5],
				'Email': dadoUsuario[6],
				'EndereçoResidencial': dadoUsuario[7],
				'CEP': dadoUsuario[8],
				'Polo': dadoUsuario[9],
				'TipoBilhete': dadoUsuario[10],
				'SaldoBilhete': dadoUsuario[11],
				'ValidadeBilhete': dadoUsuario[12],
				'CarteiraTrabalho': dadoUsuario[13],
				'ComprovanteEscolar': dadoUsuario[14]
        	}
    	)

	return make_response(
    	jsonify(Retorno)
		)


#Update-----------------------------------------------------
@app.route('/usuario/atualizar/<int:id>',methods=['PUT'])
def AtualizarUsuarioPorId(id):
	cursor = conector.cursor()
	atualizado = request.json

	comando=f'UPDATE usuarios SET Nome= "{atualizado["Nome"]}", CPF= {atualizado["CPF"]}, RG= {atualizado["RG"]}, DataNascimento= "{atualizado["DataNascimento"]}", Telefone= {atualizado["Telefone"]}, Email= "{atualizado["Email"]}", EndereçoResidencial= "{atualizado["EndereçoResidencial"]}", CEP= {atualizado["CEP"]}, Polo= "{atualizado["Polo"]}", TipoBilhete= "{atualizado["TipoBilhete"]}", SaldoBilhete= {atualizado["SaldoBilhete"]}, ValidadeBilhete= "{atualizado["ValidadeBilhete"]}", CarteiraTrabalho= {atualizado["CarteiraTrabalho"]}, ComprovanteEscolar= "{atualizado["ComprovanteEscolar"]}" WHERE codigo = {id}'

	cursor.execute(comando)
	conector.commit()
	cursor.close()

	return make_response(
    	jsonify(
        	mensagem='Registro atualizado com sucesso!',
        	user=atualizado
    	)
	)


#Delete------------------------------------------------------
@app.route('/usuario/deletar/<int:id>',methods=['DELETE'])
def DeletarUsuarioPorId(id):
	cursor = conector.cursor()

	comando=f'DELETE FROM usuarios WHERE codigo = {id}'

	cursor.execute(comando)
	conector.commit()
	cursor.close()

	return make_response(
    	jsonify(
        	mensagem='Registro deletado com sucesso!',
    	)
	)

app.run()

# Baixar Python na máquina
# Baixar extensão Python
# pip install Flask
# pip install mysql-connector-python