from socket import gethostname

import torch

torch.distributed.init_process_group(backend="gloo")
                                     #timeout=datetime.timedelta(seconds=1800),
                                     #world_size=- 1,
                                     #rank=- 1,
                                     #store=None,
                                     #group_name='',
                                     #pg_options=None)
size = torch.distributed.get_world_size()
# print("size:", size, type(size))
rank = torch.distributed.get_rank()
print(f"rank: {rank} out of {size}, running on {gethostname()}")
data = torch.tensor(1).cuda()
torch.distributed.all_reduce(data)
#print(data)
#data = torch.tensor(1)
#torch.distributed.all_reduce(data)
#print(data)