"""Clase creada para generar la URL a usar."""

import database, log

class Parametros():

    logger = log.logger
    WS_ALPHA = "www.alphavantage.co/query"
    GET_KEYS=['function','symbol','outputsize','apikey'] # Las keys son constantes
    POST_KEYS=['name','last_name','email']
    #PARAM = {'function':'TIME_SERIES_DAILY','symbol':'FB','outputsize':'compact','apikey':'X86NOH6II01P7R24'} # Ejemplo

    def __init__(self):
        """Constructor de la clase."""
        self.logger.info("Object Parametros has been created.")
        pass

    def createURL(self, param):
        URL = "https://" + self.WS_ALPHA + "?" + '&'.join([list(param.keys())[i]+'='+list(param.values())[i] for i in range(len(param))])
        self.logger.info("createURL method called.")
        return URL

    def saveParameters(self, records, key):
        """Aquí deberíamos guardar la información del usuario en base de datos junto con la key."""
        self.logger.info("saveParameters method called.")
        db = database.DataBase()
        db.saveRecord(rec=records,key=key)
    
    def checkKey(self,key):
        self.logger.info("checkKey method called.")
        db = database.DataBase()
        return db.getKey(key)
    
    def checkParameters(self,dct):
        self.logger.info("checkParameters method called.")
        return all([x in dct.keys() for x in self.GET_KEYS])       # Check if expected parmeters are passed
