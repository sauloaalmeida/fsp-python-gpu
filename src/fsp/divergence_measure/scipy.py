from scipy.spatial import distance
import numpy as np

class DivergenceMeasureScipy():

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def dm2(self):
        D_CS = 0
        #Define Na and Nb, d
        Na, d = self.A.shape
        Nb, _ = self.B.shape

        # Divergence_Measure_Case == 2
        Va = np.var(self.A, axis=0)
        Vb = np.var(self.B, axis=0)
        Va[Va<10**(-12)] = 10**(-12)
        Vb[Vb<10**(-12)] = 10**(-12)
        ha2 = ( 4/((d+2)*Na) )**(2/(d+4))
        hb2 = ( 4/((d+2)*Nb) )**(2/(d+4))
        logha2 = (2/(d+4))*( np.log(4) - np.log(d+2) - np.log(Na) )
        loghb2 = (2/(d+4))*( np.log(4) - np.log(d+2) - np.log(Nb) )
        logprodVa = np.sum(np.log(Va))
        logprodVb = np.sum(np.log(Vb))
        logprodVab = np.sum(np.log(ha2*Va+hb2*Vb))
        sum_a = np.sum(np.exp( - distance.pdist(self.A, 'mahalanobis', VI=np.linalg.inv(np.diag(Va)))**2/(4*ha2)))
        sum_b = np.sum(np.exp( - distance.pdist(self.B, 'mahalanobis', VI=np.linalg.inv(np.diag(Vb)))**2/(4*hb2)))
        sum_ab = np.sum(np.exp( - distance.cdist(self.A,self.B, 'mahalanobis', VI=np.linalg.inv(np.diag(ha2*Va+hb2*Vb)))**2/2))

        D_CS = -d*np.log(2) - (d/2)*( logha2 + loghb2 ) - (1/2)*( logprodVa + logprodVb ) + logprodVab -2*np.log(sum_ab) + np.log(Na + 2*sum_a) + np.log(Nb + 2*sum_b)
        return D_CS