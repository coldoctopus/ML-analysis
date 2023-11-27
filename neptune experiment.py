import neptune.new as neptune

# Initialize Neptune with your API token and project name
neptune.init(project="Intro-to-CS-compare/AI-compare", api_token='eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI0NTU5ODY1Ny00OTNmLTQwZGYtODlmYi01MWE4YTk5NDlhMTEifQ==')

# Create a Neptune experiment
with neptune.create_experiment(name="HOGSVM experiment"):
    # Log parameters
    neptune.log_param('learning_rate', 0.001)
    neptune.log_param('batch_size', 32)

    # Your machine learning training code here...
    # Train your model, log metrics, etc.

    # Log metrics
    neptune.log_metric('accuracy', 0.85)
    neptune.log_metric('loss', 0.2)

# Stop the experiment
neptune.stop()
