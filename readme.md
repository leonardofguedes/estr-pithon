API-ESTR

Passo 1:
- baixar bibliotecas do requirements.txt

Porta:
localhost/5000




Paginação na rota get /empresas:
Para usar a rota com paginação, limite de itens e ordenação, você precisará adicionar parâmetros à URL da seguinte maneira:

Paginação: Para controlar a paginação, você pode usar os parâmetros page e per_page. Por exemplo, se você quiser a segunda página de resultados e quiser 5 resultados por página, você usaria a seguinte URL:

/empresas?page=2&per_page=5

Isto irá retornar as empresas de 6 a 10, se estiverem disponíveis.

Limite de itens: Se você quiser limitar o número total de resultados retornados, você pode usar o parâmetro limit. Por exemplo, se você quiser um máximo de 10 resultados, independente da paginação, você usaria a seguinte URL:

/empresas?limit=10

Isto irá retornar até 10 empresas, mesmo que a paginação normalmente retornasse mais.

Ordenação: Para controlar a ordenação dos resultados, você pode usar o parâmetro sort. Por exemplo, se você quiser ordenar as empresas pelo nome_fantasia, você usaria a seguinte URL:

/empresas?sort=nome_fantasia

Isto irá retornar todas as empresas, ordenadas por nome_fantasia.

Você pode combinar esses parâmetros da maneira que quiser. Por exemplo, se você quiser a segunda página de resultados, com 5 resultados por página, um máximo de 10 resultados no total, e ordenado por nome_fantasia, você usaria a seguinte URL: