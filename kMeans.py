import numpy as np
import random

def obter_discantica_acordo_centroid(point, centroid):
    #RAIZ((x(point)-x(centroid) elevado 2)+(y(point)-y(centroid) elevado 2))
    return round(np.sqrt(np.sum((point - centroid)**2)), 1)

def obter_centroid_proximo(distance):
    #obtem o index do centroid que é o próximo
    index_of_minimum = min(distance, key=distance.get)
    return index_of_minimum

def printar_distancia(distance):
    print('-'*20)
    for i in distance:
        print(i)


def obter_novo_centroid(list_distance, number_centroid):
    centroids = []
    for index_centroid in range(number_centroid):
        soma_x=0
        soma_y=0
        count = 0
        for distance in list_distance:
            if distance['index'] != index_centroid:
                continue
            else:
                count += 1
                soma_x += distance['data'][0]
                soma_y += distance['data'][1]
        if count ==0:
            count =1
        media_x = round((soma_x/count),2)
        media_y = round((soma_y/count),2)
        centroids.append([media_x, media_y])
    print('Novos centroid')
    for c in range(len(centroids)):
        print(f'Centroid {c} - {centroids[c]}')
    return np.array(centroids)

def k_means(points, centroids):
    #quantidade da dados na planilha
    total_points = len(points)
    #qtd de centroid
    qtd_centroid = len(centroids)
    #variável controle
    last_index_distance_centroid = []
    while True:
        distance = []
        for index_point in range(0, total_points):
            interaction = {}
            interaction['data'] = points[index_point]

            distance_centroid = {}
            #AQUI É SALVA A DISTANCIA DE CADA CENTROID DE ACORDO A INTEREÇÃO DO MOMENTO
            for index_centroid in range(0, qtd_centroid):

                interaction[f'Distancia {index_centroid}'] = obter_discantica_acordo_centroid(points[index_point], centroids[index_centroid])
                interaction[f'centroid - {index_centroid}'] = centroids[index_centroid]
                distance_centroid[index_centroid] = interaction[f'Distancia {index_centroid}']
            interaction['index'] = obter_centroid_proximo(distance_centroid)
            distance.append(interaction)
        new_index_distance_centroid = [x['index'] for x in distance]
        printar_distancia(distance)
        if last_index_distance_centroid != new_index_distance_centroid:
            last_index_distance_centroid = new_index_distance_centroid
            centroids = obter_novo_centroid(distance, qtd_centroid)
        else:
            break


def print_label_data(result):
    print("Result of k-Means Clustering: \n")
    for data in result[0]:
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))

def create_centroids(number_centroid):
    centroids = []

    print('Primeiros centroids')
    for i in range(number_centroid):
        centroid = [random.randint(0, 100), random.randint(0, 100)]
        centroids.append(centroid)
        print(centroid)
    print('-'*20)
    return np.array(centroids)


def run(number_centroid=2):
    filename = "data.csv"
    data = np.genfromtxt(filename, delimiter=",")
    centroids = create_centroids(number_centroid)
    k_means(data, centroids)
