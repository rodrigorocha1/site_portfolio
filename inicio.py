from paginas.pagina_principal import PaginaPrincipal

pp = PaginaPrincipal()
server = pp.app.server

if __name__ == '__main__':
    pp.rodar_aplicacao()
