#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import numpy as np
import numpy.ma as ma


# Receber dados do PHP
try:
    data = json.loads(sys.argv[1])
except:
    print "ERROR"
    sys.exit(1)


# Função para calcular a rotação https://arxiv.org/pdf/1406.0014.pdf
# http://link.springer.com.sci-hub.cc/article/10.1007%2Fs13246-010-0037-1
# http://iopscience.iop.org.sci-hub.cc/article/10.1088/0031-9155/57/24/N513/meta
def get_coordinates(gantry, coll, couch, SAD):

    # Rotação no Eixo Z ( Gantry )
    gantry_matrix = np.matrix([[np.cos(gantry), np.sin(gantry), 0],
                               [np.sin(gantry), np.cos(gantry), 0],
                               [0, 0, 1]])

    coll_matrix = np.matrix([[np.cos(coll), 0, np.sin(coll)],
                             [0, 1, 0],
                             [np.sin(coll), 0, np.cos(coll)]])

    couch_matrix = np.matrix([[np.cos(couch), 0, np.sin(couch)],
                              [0, 1, 0],
                              [np.sin(couch), 0, np.cos(couch)]])

        # Rotated Source point (1st gantry, 2nd couch)
    sourcePoint_bev = np.matrix([[0, -SAD, 0]])

    result = sourcePoint_bev*gantry_matrix*coll_matrix*couch_matrix

    # Convertendo a matriz Nympy para lista (lista pode ser convertida em JSON)
    resultList = result.tolist()

    return resultList

# Chamando função e Passando parametros recebidos.
# new_coordinates = get_coordinates(data['gantryAngle'], data['collAngle'], data[
 #                                 'couchAngle'], data['SAD'])
new_coordinates = get_coordinates(100, 100, 100, 100)

# enviando resultado para o PHP
print json.dumps(new_coordinates)
