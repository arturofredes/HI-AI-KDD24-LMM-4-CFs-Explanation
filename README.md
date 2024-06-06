# LLMs for Exaplaining Sets of Counterfactual Examples to Final Users
### Arturo Fredes & Jordi Vitrià | KDD 2024 Workshop HI-AI
Causality is vital for understanding true cause-and-effect relationships between varianbles within
predictive models, rather than relying on mere correlations, making them highly relevant in the field of
Explainable AI. In an automated decision-making scenario, we can analyze the underlying data-generation
process using causal inference methods, which enable us to explain a model’s decision by manipulating
features and creating counterfactual examples. These counterfactuals explore hypothetical scenarios
where a minimal number of factors are altered, providing end-users with valuable information on how
to change their situation. However, interpreting a set of multiple counterfactuals can be challenging for
end-users who are not used to analyze raw data records. In our work, we evaluate the use of Causally
Informed LLMs in the explanation generation process and guide the LLM through smaller tasks that
mimic human reasoning when explaining a decision based on counterfactual cases. We conducted
various experiments using a public dataset and proposed a method of closed-loop evaluation to assess the
coherence of the final explanation with the counterfactuals as well as the quality of the content. Finally,
we use these causally informed LLMs to check the validity of the final explanation in causal terms.

## Setup
You will neead an Open AI API key in your environment variables.
```
OPENAI_API_KEY = your_key
```
Install necessary packages
```
pip install -r requirements.txt
```
## Example Notebook
This notebook contains an example of a case that is predicted to earn less than 50k$ a year. In this notebook we go over all of the steps followed in order to generate an explanation and evaluating it.

## Train Notebook
In this notebook we train a model to predict whether a person will earn more or less than 50k$. In here we also generate the file swith the data that we will have to read in other notebooks. This data is already included in the `data/` folder and the model in `models/` so there it is not strictly necessary to run this notebook.

## Experiments Notebook
In here all the code and results for the experiments are included.