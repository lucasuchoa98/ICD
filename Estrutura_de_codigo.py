def ler_dados(dado: np.):
    """
    Transforma os dados para o formato xarray

    Essa função lê os dados disponiveis no link:
    https://utexas.app.box.com/v/Xavier-etal-IJOC-DATA
    A função recebe dados (no formato .nc, .npc, etc) e retorna um xarray dele

    Lucas e Mateus
    """
    return dado_da_grade

def faz_mapa(dado_da_grade: xr.DataArray):
    """
    Essa função faz um mapa com o recorte do brasil

    A função recebe os dados da grade e retorna um mapa

    Mateus
    """
    return mapa

def faz_regiao_hidrografica(dados_shp: str):
    """
    Essa função faz o poligono das regiões hidrograficas

    Essa função recebe os dados da região hidrográfica do estado de alagoas e
    retorna o poligono selecionado

    Lucas
    """
    return poligono

def intersecta_dado(dados_da_grade: xr.DataArray, poligono: gpd.GeoDataFrame):
    """
    Essa função produz o poligono de recorte dos `dados_da_grade` através do `poligono`

    A função recebe os dados da grade e o poligono da região hidrográfica e
    retorna a interseção de ambos em xr.DataArray

    Micaellen e Lucas
    """
    return interseccao

def faz_grafico(interseccao: xr.DataArray):
    """
    Essa função produz gráficos estatisticos

    A função recebe dados da grade e retorna um gráfico

    Micaellen e Mateus
    """
    return grafico
