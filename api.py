"""
API for Eureka Challenge.

Author: Alejandro Rizzuto.
"""

import flask
from flask import request, jsonify
import requests
import pandas as pd
import json

# User classes
import const, functions as fc, messages as msgs, log

app = flask.Flask(__name__)
logger = log.logger

############################################################################

@app.route('/', methods=['GET'])
def home():
    """GET method for home path."""
    logger.info('************************************')
    logger.info('GET called - '+request.url_rule.rule)
    logger.info('A prototype API for Eureka challenge.')
    return 'A prototype API for Eureka challenge.\n'

############################################################################

@app.route('/stockmarket', methods=['GET'])
def get_info():
    """GET method to get market information with specific parameters."""
    logger.info('************************************')
    logger.info('GET called - '+request.url_rule.rule)
    cnst = const.Parametros()                                       # Object creation.
    msg = msgs.Messages()                                           # Object creation.

    dct = request.args.to_dict()                                    # Get arguments

    if cnst.checkParameters(dct):                                   # Check if arguments are the same as the expected ones
        if cnst.checkKey(dct['apikey']):
            logger.info("All parameters are OK.")                               
            URL=cnst.createURL(dct)                                 # URL generation to get info required
            res = requests.get(URL)                                 # Get information from URL
            result = fc.getNumberOfRowsToShow(res, request.args)    # Get number of rows if exist, else show everything
            return jsonify(result)                                  # Return information
        return msg.GETReturnErrorInKey()
    return msg.GETReturnError(cnst.GET_KEYS)

############################################################################

@app.route('/stockmarket', methods=['POST'])
def update_record():
    """POST method to get market information with specific parameters."""
    logger.info('************************************')
    logger.info('POST called - '+request.url_rule.rule)
    cnst = const.Parametros()                                       # Const object creation
    msg = msgs.Messages()                                           # Object creation.

    records = json.loads(request.data)                              # Get data from post
    check = all([x in records.keys() for x in cnst.POST_KEYS])      # Check if expected parmeters are passed

    if check:
        logger.info("All parameters are OK.")
        key = fc.getKey(records)                                    # Get new key
        logger.info("Saving user ...\n")
        cnst.saveParameters(records, key)                           # Save info in database/file
        return msg.POSTReturnSuccess(key)                           # Return success message
    return msg.POSTReturnError(cnst.POST_KEYS)                      # Else return error message

############################################################################

@app.route('/stockmarket', methods=['PUT'])
def create_record():
    """PUT method ..."""
    record = json.loads(request.data)
    return jsonify(record)

############################################################################
    
@app.route('/stockmarket', methods=['DELETE'])
def delete_record():
    """DELETE method ..."""
    record = json.loads(request.data)
    return jsonify(record)
    
############################################################################

@app.errorhandler(404)
def page_not_found(e):
    """Execute the handler for any error 404 found."""
    logger.error("The resource could not be found.")
    return "The resource could not be found.\n", 404

############################################################################



def main():
    """Execute the Main program of the API."""
    app.run(debug=True)


if __name__ == '__main__':
    main()
