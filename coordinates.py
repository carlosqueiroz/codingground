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


# Função para calcular a rotação


def get_coordinates(gantry, coll, couch, SAD):

    # Rotação no Eixo Z ( Gantry )
    gantry_matrix = np.matrix([[np.cos(gantry), np.sin(gantry), 0],
                               [np.sin(-gantry), np.cos(gantry), 0],
                               [0, 0, 1]])

    # Rotation no eixo Y  (couch)
    couch_matrix = np.matrix([[np.cos(couch), 0, np.sin(-couch)],
                              [0, 1, 0],
                              [np.sin(couch), 0, np.cos(couch)]])

    # Rotated Source point (1st gantry, 2nd couch)
    sourcePoint_bev = np.matrix([[0, -SAD, 0]])

    result = sourcePoint_bev * gantry_matrix * couch_matrix

    # Convertendo a matriz Nympy para lista (lista pode ser convertida em JSON)
    resultList = result.tolist()

    return resultList


# Chamando função e Passando parametros recebidos.
new_coordinates = get_coordinates(data['gantryAngle'], data['collAngle'], data['couchAngle'], data['SAD'])


# enviando resultado para o PHP
print json.dumps(new_coordinates)