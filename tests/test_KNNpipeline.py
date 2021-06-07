from toolbox.knnimputerpipeline import knnimputer

def test_knnimputer():
    assert knnimputer('min_max', 'linear').get_params != None