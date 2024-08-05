from numbers import Number
import numpy as np
import numpy.typing as npt

def deltaR(eta1: Number, phi1: Number, eta2: Number, phi2: Number) -> float:
    """
    Computes the deltaR between two objects in eta-phi space.

    Parameters
    ----------
    eta1 : Number
        eta coordinate of the first object
    phi1 : Number
        phi coordinate of the first object
    eta2 : Number
        eta coordinate of the second object
    phi2 : Number
        phi coordinate of the second object

    Returns
    -------
    float
        deltaR between the two objects
    """
    deta = eta1 - eta2
    dphi = np.abs(phi1, phi2)
    if dphi >= np.pi:
        dphi = 2*np.pi - dphi
    return np.sqrt(deta*deta + dphi*dphi)


def norm1(data) -> npt.NDArray[np.float_]:
    norms = np.abs( data.sum(axis=1) )
    norms[norms==0] = 1
    return data/norms[:,None]
