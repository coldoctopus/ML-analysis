import neptune
run = neptune.init_run()

"""
model_version = neptune.init_model_version(
    model="AIC-HOGSVM",
    project="Intro-to-CS-compare/AI-compare",
    api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI0NTU5ODY1Ny00OTNmLTQwZGYtODlmYi01MWE4YTk5NDlhMTEifQ==", # your credentials
)

model_version["model"].upload("D:\GitHub\ML-analysis\face recognition.ipynb")
model_version["validation/dataset"].track_files("D:\GitHub\ML-analysis\dataset\suprise")
model_version["validation/acc"] = 0.97

model_version.change_stage("staging")"""

project = neptune.init_project(project="Intro-to-CS-compare/AI-compare", api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI0NTU5ODY1Ny00OTNmLTQwZGYtODlmYi01MWE4YTk5NDlhMTEifQ==")

project["general/data_analysis"].upload("face recognition.ipynb")
#project["project_dataset"].upload("dataset")