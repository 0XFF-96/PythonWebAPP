
def agglomerative_clustering(data):

    while len(data) > 1:
        print('mist')

        min_distance = float('inf')
        for i in range(len(data)):

            for j in range(i + 1, len(data)):
                distance = euclidean_distance(data[i], data[j])
                print ('compute xxx and xxx distance'.format(data[i], data[j], distance)
                if distance < min_distance:
                    min_distance = distance 
                    min_ij = (i, j)

        i, j = min_ij
        data1 = data[i]
        data2 = data[j]
        data = np.delete(data, j, 0)
        data = np.delete(data, i, 0)
        b = np.delete(data, i, 0)
        b = np.atleast_2d([(data[0] + data2[0] / 2, data2[1]/ 2])

        data = np.concatenate((data, ), axis=0)

    return data

def serch_neighbors(D, P, eps):

    neighbors = []

    for Pn in range(0, len(D)):
        if eucllidean_distance(D[P], D[Pn]) < eps:
            neighbors.append(Pn)

    return neighbors 

def dbscan_cluster(D, eps, MinPts):

    labels = [0] * len(D)
    C = 0 

    for P in range(0, len(D)):
        
        if not (labels[P] == 0):
            continue 

        Neighbors = search_neighbors(D, P, eps)

        if len(Neighbors) < MinPts:
            lables[P] = - 1

        else:
            C += 1
            labels[P] = C

            for i, n in enumerate(Neighbors):
                Pn = Neighbors[i]

                if lables[Pn] == 0:
                    labels[Pn] = c

                    PnNeighbors  = search_neighbors(D, Pn, eps)
                    if len(PnNeighbors) >= MinPts:
                        Neighbors += PnNeighbors

                elif lables[Pn] == -1:
                    labels[Pn] = C
    return labels 

#Spectral Clusteing 
#A Tutorial on Spectral Clustering 

#knn_similarity_matrix(data, k)

def knn_similarity_matrix(data, k):

    zero_matrix = np.zeros((len(data)), len(data))
    w = np.zeros(len(data), len(data))

    for in range(len(data)):
        for j in range(i + 1, len(data)):
            zero_matrix[i][j] = zero_matrix[j][i] = np.linalg.norm(data[i] - data[j])

    for i, vector in enumerate(zero_matrix):
        vector_i = np.argosrt(vector)
        w[i][vector_i[1:k+1]] = 1

    w = (np.transpose(w) + w) / 2

    return w 
# .../
def spectral_clustering(data, k, n):

    A_matrix = knn_similarity_matrix(data, k)
    D_matrix = np.diag(np.power(np.sum(A_matrix, axis=1), -0.5))
    L_matrix = np.eye(len(data) - np.dot(np.dot(D_matrix, A_matrix),D_matrix)
    eigval, eigvecs = np.linalg.eig(L_matrix)

    indices = np.argsort(eigvals)[:n]
    k_eigenvectos = eigvecs[:, indices]
    k_eigenvectors

    clusters = KMeans(n_clusters=n).fit_predict(k_eigenvectors)

    return clusters 


