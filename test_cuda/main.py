import torch

cnt_devices = torch.cuda.device_count()
print("cuda initialized:", torch.cuda.is_initialized())
print("cnt cnt_devices:", cnt_devices)
for id_device in range(cnt_devices):
    device_name = torch.cuda.get_device_name(id_device)
    print(f"checking device {id_device} {device_name}:")
    torch.cuda.set_device(id_device)
    properties = torch.cuda.get_device_properties(id_device)
    print(properties)
    mem_size = properties.total_memory
    print("creating tensor on device")
    chunks = []
    cnt_chunks = 10
    for id_chunk in range(cnt_chunks):
        a = torch.rand(int(0.7 * mem_size / 4 / cnt_chunks), dtype=torch.float32, device=id_device)
        print(a.mean())
        chunks.append(a)

# torch.cuda.can_device_access_peer(device, peer_device)[source]
