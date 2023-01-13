import torch

for id_device in range(torch.cuda.device_count()):
    print(f"checking device {id_device}:")
    properties = torch.cuda.get_device_properties(id_device)
    print(properties)
