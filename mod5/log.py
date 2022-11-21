# Log e Logging
import logging
# tipos de log utilizaveis ''logging.xxx''
'''
debug - Só estformando infomrações para desenvolvedores
info - Só quero informar algo que está acontecendo no programa, mas que não e um erro.
warning - Quero alertar sobre algo que está acontecendo, possívelmente fora do esperado, porém ainda não é um erro, mas pode gerar um futuramente.
error - Um erro ocorreu na aplicação.
critical - Um erro com consequências ges acaba de ocorrrer na aplicação.
'''
logging.basicConfig(level=logging.DEBUG,filename='log.log',filemode='a',format='%(levelname)s - %(message)s')
# comando usado pra escolher o nivel mininmo do logging a ser exibido, para criar um arquivo que possa ser acessado posteriormente.
logging.debug('Logging nível debug')
logging.info('Logging nível info')
logging.warning('Logging nível warning')
logging.error('Logging nível error')
logging.critical('Logging nível critical')
