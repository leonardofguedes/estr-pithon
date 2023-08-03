from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import Swagger, swag_from
from data.empresas import empresas_fake
from operator import itemgetter

app = Flask(__name__)
api = Api(app)
template = {
    "swagger": "2.0",
    "info": {
        "title": "API 03082023",
        "description": "API ESTR",
        "version": "0.0.1"
    },
    "consumes": [
        "application/json",
    ],
    "produces": [
        "application/json",
    ],
}
app.config['SWAGGER'] = {
    'uiversion': 3,
    'swagger_version': '2.0',
    'specs_route': '/apidocs/',
    'templates': template
}
swagger = Swagger(app)

class HomeResource(Resource):
    @swag_from('docs/home.yml')
    def get(self):
        return "API-EST"

class EmpresaResource(Resource):
    @swag_from('docs/empresa_get.yml')
    def get(self, cnpj):
        for empresa in empresas_fake:
            if empresa['cnpj'] == cnpj:
                return empresa
        return {'error': 'Empresa não encontrada'}, 404

    @swag_from('docs/empresa_put.yml')
    def put(self, cnpj):
        """Edita uma empresa pelo CNPJ"""
        for empresa in empresas_fake:
            if empresa['cnpj'] == cnpj:
                for field in request.json:
                    if field not in ['nome_fantasia', 'cnae']:
                        return {'error': f'Atributo {field} não pode ser alterado'}, 400

                if 'nome_fantasia' in request.json:
                    empresa['nome_fantasia'] = request.json['nome_fantasia']
                if 'cnae' in request.json:
                    empresa['cnae'] = request.json['cnae']
                return empresa

        return {'error': 'Empresa não encontrada'}, 404


    
    @swag_from('docs/empresa_delete.yml')
    def delete(self, cnpj):
        """Remove uma empresa pelo CNPJ"""
        global empresas_fake
        empresas_fake = [empresa for empresa in empresas_fake if empresa['cnpj'] != cnpj]
        return {'success': 'Empresa removida'}

class EmpresasResource(Resource):
    @swag_from('docs/empresas.yml')
    def get(self):
        """Retorna a lista de todas as empresas"""
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        limit = int(request.args.get('limit', len(empresas_fake)))
        sort = request.args.get('sort', 'nome_razao')

        sorted_empresas = sorted(empresas_fake, key=itemgetter(sort))

        start = (page - 1) * per_page
        end = start + per_page
        empresas = sorted_empresas[start:end][:limit]

        return empresas

    @swag_from('docs/empresa_post.yml')
    def post(self):
        """Cria uma nova empresa"""
        nova_empresa = request.json
        empresas_fake.append(nova_empresa)
        return nova_empresa, 201

api.add_resource(EmpresaResource, '/empresa/<string:cnpj>')
api.add_resource(EmpresasResource, '/empresas')
api.add_resource(HomeResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
