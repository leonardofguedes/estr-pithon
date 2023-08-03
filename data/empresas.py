import random
import uuid

def generate_random_cnpj():
    cnpj = [str(random.randint(0, 9)) for _ in range(14)]
    return ''.join(cnpj)

def generate_random_cnae():
    cnae = [str(random.randint(0, 9)) for _ in range(7)]
    formatted_cnae = ''.join(cnae[:4]) + '-' + ''.join(cnae[4:])
    return formatted_cnae

def add_random_cnpj_and_uuid_to_empresas(num_empresas):
    empresas = []
    for _ in range(num_empresas):
        empresa = {
            'nome_razao': f'Empresa {_ + 1}',
            'nome_fantasia': f'Empresa {_ + 1}',
            'address': f'Rua {_ + 1}, 123',
            'city': f'Cidade {_ + 1}',
            'cnae': generate_random_cnae(),
            'cnpj': generate_random_cnpj(),
            'uuid': str(uuid.uuid4())
        }
        empresas.append(empresa)
    return empresas

num_empresas = 100
empresas_fake = add_random_cnpj_and_uuid_to_empresas(num_empresas)

