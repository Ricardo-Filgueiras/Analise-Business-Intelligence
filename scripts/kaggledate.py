import kagglehub

# Download latest version
path = kagglehub.dataset_download("guimacrlh/dataset-vendas")

print("Path to dataset files:", path)