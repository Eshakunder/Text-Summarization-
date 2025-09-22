from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
       config = ConfigurationManager()
       model_eval_config = config.get_model_evaluationconfig()
       model_eval_config = ModelEvaluation(config=model_eval_config)
       model_eval_config.evaluate()