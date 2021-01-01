"""	    	       
@author : uguray

"""
import pickle


def serialize(obj, filename: str):
    """
    Simple object serialization given a filename.

    """
    with open(filename + ".pkl", "wb") as f:
        pickle.dump(obj, f)


def deserialize(filename: str):
    """
    Simple object deserialization given a filename.

    """
    with open(filename + ".pkl", "rb") as f:
        return pickle.load(f)

# Suppose the object_1 exist
serialize(object_1, "object_1")
object_1 = deserialize("object_1)
