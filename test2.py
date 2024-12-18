# Tests model accuracy metrics
import hyperparameter_tuning as ht

def test_tuning():
    tuned_model = ht.tune_hyperparameters(["test data"])
    assert "_tuned" in tuned_model
